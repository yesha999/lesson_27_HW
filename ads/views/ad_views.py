from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, UpdateView
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.permissions import AdUpdatePermission, AdDeletePermission
from ads.serializers import AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, AdDeleteSerializer
from lesson_27_homework.settings import TOTAL_ON_PAGE


class StartView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        cat = request.GET.get('cat', None)
        if cat:
            self.object_list = self.object_list.filter(category__id__exact=cat)

        text = request.GET.get('text', None)
        if text:
            self.object_list = self.object_list.filter(name__icontains=text)

        location = request.GET.get('location', None)
        if location:
            self.object_list = self.object_list.filter(author__location__name__icontains=location)

        price_from = request.GET.get('price_from', None)
        if price_from:
            price_from = int(price_from)
            self.object_list = self.object_list.filter(price__gte=price_from)

        price_to = request.GET.get('price_to', None)
        if price_to:
            price_to = int(price_to)
            self.object_list = self.object_list.filter(price__lte=price_to)

        paginator = Paginator(
            self.object_list.order_by("-price").select_related("author", "category"),
            TOTAL_ON_PAGE)
        try:
            page_number = int(request.GET.get("page"))
            page_obj = paginator.get_page(page_number)
        except TypeError as e:
            page_obj = paginator.get_page(1)

        response = []
        for ad in page_obj:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author.pk,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image.url if ad.image else None,
                "category": ad.category.pk

            })

        return JsonResponse({
            "items": response,
            "total": page_obj.paginator.count,
            "num_pages": page_obj.paginator.num_pages}, safe=False)


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


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["name", "image"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        try:
            self.object.image = request.FILES["image"]
        except KeyError as e:
            pass

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.pk,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "category": self.object.category.pk
        })
