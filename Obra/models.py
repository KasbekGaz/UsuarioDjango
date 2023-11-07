from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


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


#! OBRA modelo

class Obra(models.Model):

    nombre = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    dependencia = models.CharField(max_length=255)
    fecha = models.DateField()
    p_inicial = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    #! campo que se dllenan con modelo gasto
    total_gastos = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, editable=False)
    #! campos que se llenan con modelo volumen
    # * Aun no se pondra este

    def __str__(self):
        return f"{self.nombre} ({self.total_gastos}) ({self.total_importes}) ({self.total_importes_mod})"


#! GASTO modelo


class Gasto(models.Model):
    CATEGORIAS = [
        ('Administracion', 'Administración'),
        ('Mano de obra', 'Mano de obra'),
        ('Materiales', 'Materiales'),
        ('Viaticos', 'Viáticos'),
        ('Varios', 'Varios'),
    ]

    FACTU = [
        ('Facturado', 'Facturado'),
        ('No Facturado', 'No Facturado'),
    ]

    TIPOS = [
        ('Efectivo', 'Efectivo'),
        ('Transferencia', 'Transferencia'),
    ]

    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    proveedor = models.CharField(max_length=255, null=True)
    concepto = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    categoria = models.CharField(max_length=25, choices=CATEGORIAS)
    facturado = models.CharField(
        max_length=50, choices=FACTU, default='No Facturado')
    Tipo = models.CharField(max_length=50, choices=TIPOS, default='Efectivo')
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        super(Gasto, self).save(*args, **kwargs)  # Guarda el objeto primero
        self.actualizar_total_gastos()

    def delete(self, *args, **kwargs):
        super(Gasto, self).delete(*args, **kwargs)  # Elimina el objeto primero
        self.actualizar_total_gastos()

    def actualizar_total_gastos(self):

        total_gastos = Gasto.objects.filter(obra=self.obra).aggregate(
            total_gastos=models.Sum('importe'))['total_gastos'] or 0
        self.obra.total_gastos = total_gastos
        self.obra.save()

    def __str__(self):
        return f"{self.concepto} ({self.categoria}) ({self.obra})"
