from django.http import JsonResponse
from django.views import View
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.permissions import AdUpdatePermission, AdDeletePermission
from ads.serializers import AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, AdDeleteSerializer, \
    AdListSerializer


class StartView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, AdUpdatePermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDeleteSerializer
    permission_classes = [IsAuthenticated, AdDeletePermission]
