import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import AdsModel, CategoriesModel, UserModel
from lesson_27_homework.settings import TOTAL_ON_PAGE


class StartView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        paginator = Paginator(self.object_list.order_by("-price"), TOTAL_ON_PAGE)

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


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = AdsModel
    fields = ["name", "author", "price", "description",
              "is_published", "category"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        author = get_object_or_404(UserModel, pk=ad_data["author"])

        description = ad_data.get("description")
        try:
            is_published = ad_data["is_published"]
        except KeyError as e:
            is_published = False
        category = get_object_or_404(CategoriesModel, pk=ad_data["category"])
        ad = AdsModel.objects.create(name=ad_data["name"], author=author,
                                     price=ad_data["price"], description=description,
                                     is_published=is_published, category=category)
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.pk,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "category": ad.category.pk
        })


class AdDetailView(DetailView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

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


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = AdsModel
    fields = ["name", "price", "description",
              "is_published", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)

        name = ad_data.get("name")
        if name:
            self.object.name = name

        price = ad_data.get("price")
        if price:
            self.object.price = price

        description = ad_data.get("description")
        if description:
            self.object.description = description

        is_published = ad_data.get("is_published")
        if is_published:
            self.object.is_published = is_published

        category = ad_data.get("category")
        if category:
            self.object.category = get_object_or_404(CategoriesModel, pk=category)

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


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = AdsModel
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = AdsModel
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
