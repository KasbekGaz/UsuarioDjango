from rest_framework import generics, permissions
from .models import CustomUser, Obra, Gasto
from .serializers import CustomUserSerializer, ObraSerializer, GastoSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, viewsets


#! vistas para USUARIO
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'Usuario registrado con éxito', 'user_id': user.id, 'token': token.key}, status=status.HTTP_201_CREATED)


class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        if created:
            message = "Inicio de sesión exitoso."
        else:
            message = "Sesión ya iniciada para este usuario."

        return Response({'token': token.key, 'message': message}, status=status.HTTP_200_OK)


class UserLogoutView(generics.DestroyAPIView):
    queryset = Token.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        tokens = Token.objects.filter(user=user)
        tokens.delete()
        return Response({'message': 'Cierre de sesión exitoso'}, status=status.HTTP_204_NO_CONTENT)


#! Vistas para OBRA
class ObraViewSet(viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

    # * Definimos metodos HTTP permitidos en la vista
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    # * logica para el manejo de roless

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'Admin':
            # Lógica para crear un gasto (para usuarios Admin)
            return super().create(request, *args, **kwargs)
        else:
            return Response({'detail': 'No tiene permiso para crear obras'}, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'Admin':
            # Lógica para actualizar un gasto (para usuarios Admin)
            return super().update(request, *args, **kwargs)
        else:
            return Response({'detail': 'No tiene permiso para actualizar obras'}, status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'Admin':
            # Lógica para actualizar parcialmente un gasto (para usuarios Admin)
            return super().partial_update(request, *args, **kwargs)
        else:
            return Response({'detail': 'No tiene permiso para actualizar obras'}, status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'Admin':
            # Lógica para eliminar un gasto (para usuarios Admin)
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'detail': 'No tiene permiso para eliminar obras'}, status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.rol == 'Admin':
            # Lógica para listar gastos (para usuarios Admin)
            print('Listar obras para Admin')
            return super().list(request, *args, **kwargs)
        elif request.user.is_authenticated and request.user.rol == 'Consul':
            # Lógica para listar gastos (para usuarios Consul)
            print('Listar obras para Consul')
            return super().list(request, *args, **kwargs)
        else:
            print(f'Usuario no autorizado: {request.user}')
            return Response({'detail': 'No tiene permiso para ver obras'}, status=status.HTTP_403_FORBIDDEN)


#! Vistas para GASTO
class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
