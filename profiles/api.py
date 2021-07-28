from rest_framework import generics, permissions, serializers
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data, "token": token.key
        })

# Login API

# GET User API
