from rest_framework import serializers

from ads.serializers import AdDetailSerializer
from selections.models import Selection, Ad


class SelectionListSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Ad.objects.all()
    )

    def is_valid(self, raise_exception=False):
        self._items = self.initial_data.pop("items")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        selection = Selection.objects.create(**validated_data)

        for item in self._items:
            item_obj = Ad.objects.get(pk=item)
            selection.items.add(item_obj)

        selection.save()
        return selection

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdDetailSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionUpdateSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=Ad.objects.all()
    )

    def is_valid(self, raise_exception=False):
        self._items = self.initial_data.pop("items")
        self._items_del = self.initial_data.pop("items_del")
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        selection = super().save()

        for item in self._items:
            item_obj = Ad.objects.get(pk=item)
            selection.items.add(item_obj)

        for item in self._items_del:
            item_obj = Ad.objects.get(pk=item)
            selection.items.remove(item_obj)

        selection.save()
        return selection

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'
