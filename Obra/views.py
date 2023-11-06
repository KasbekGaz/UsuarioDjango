from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


#! vistas
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
