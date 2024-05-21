from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
