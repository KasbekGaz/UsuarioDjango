from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, telefono=None, rol='Consul'):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          telefono=telefono, rol=rol)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, telefono=None, rol='Admin'):
        user = self.create_user(username, email, password, telefono, rol)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):

    ROL_CHOICES = (
        ('Admin', 'Admin'),
        ('Consul', 'Consul'),
    )

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    rol = models.CharField(
        max_length=10, choices=ROL_CHOICES, default='Consul')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    class Meta:
        permissions = [
            ("can_view_gastos", "Puede ver gastos"),
            ("can_add_edit_delete_gastos", "Puede agregar, editar y eliminar gastos"),
        ]

    def __str__(self):
        return self.username
