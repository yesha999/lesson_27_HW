from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import UserModel, LocationModel
from users.serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer, \
    UserDeleteSerializer, LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = LocationModel.objects.all()
    serializer_class = LocationSerializer


class UserListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserCreateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDetailSerializer


class UserUpdateView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserDeleteSerializer
