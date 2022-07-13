from typing import Optional

from rest_framework import serializers

from ads.models import Ad


# Валидатор для проверки поля is_published при создании ad
def check_is_published_false(value: Optional[bool]):
    if value:
        if value is True:
            raise serializers.ValidationError(
                f"Значение поля is_published при создании объявления не может быть {value}.")


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(default=False, validators=[check_is_published_false])

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
