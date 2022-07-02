import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView

from ads.models import AdsModel, CategoriesModel


class StartView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class AdListView(ListView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        response = []
        for ad in self.object_list:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = AdsModel()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        try:
            ad.description = ad_data["description"]
        except KeyError as e:
            ad.description = None
        ad.address = ad_data["address"]
        try:
            ad.is_published = ad_data["is_published"]
        except KeyError as e:
            ad.is_published = False

        try:
            ad.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        ad.save()
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })


class AdDetailView(DetailView):
    model = AdsModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "address": self.object.address,
            "is_published": self.object.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CatListView(ListView):
    model = CategoriesModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        response = []
        for category in self.object_list:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)

        cat = CategoriesModel()
        cat.name = cat_data["name"]

        try:
            cat.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        cat.save()
        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })


class CatDetailView(DetailView):
    model = CategoriesModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })
