from users.models import UserModel, LocationModel
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = UserModel
        exclude = ['password']


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=LocationModel.objects.all(),
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self.location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = UserModel.objects.create(**validated_data)

        for location in self.location:
            location_obj, created = LocationModel.objects.get_or_create(name=location)
            user.location.add(location_obj)

        return user

    class Meta:
        model = UserModel
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = UserModel
        exclude = ['password']


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=LocationModel.objects.all(),
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self.location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save()

        for location in self.location:
            location_obj, created = LocationModel.objects.get_or_create(name=location)
            user.location.add(location_obj)

        return user

    class Meta:
        model = UserModel
        exclude = ["password"]


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
