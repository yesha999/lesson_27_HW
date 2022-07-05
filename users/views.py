import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from lesson_27_homework.settings import TOTAL_ON_PAGE
from users.models import UserModel, LocationModel


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(ListView):
    model = UserModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        paginator = Paginator(self.object_list.order_by("user_name").annotate(total_ads=Count('adsmodel')),
                              TOTAL_ON_PAGE)

        try:
            page_number = int(request.GET.get("page"))
            page_obj = paginator.get_page(page_number)
        except TypeError as e:
            page_obj = paginator.get_page(1)

        response = []
        for user in page_obj:
            response.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_name": user.user_name,
                "role": user.role,
                "age": user.age,
                "location": user.location.name,
                "total_ads": user.total_ads
            })

        return JsonResponse({
            "items": response,
            "total": page_obj.paginator.count,
            "num_pages": page_obj.paginator.num_pages}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = UserModel
    fields = ["first_name", "last_name", "user_name", "password",
              "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        role = user_data.get("role")
        if not role:
            role = 'member'
        location, created = LocationModel.objects.get_or_create(name=user_data["location"])
        user = UserModel.objects.create(first_name=user_data["first_name"], last_name=user_data.get("last_name"),
                                        user_name=user_data["user_name"], password=user_data["password"], role=role,
                                        age=user_data["age"], location=location)
        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "user_name": user.user_name,
            "role": user.role,
            "age": user.age,
            "location": user.location.name
        })


class UserDetailView(DetailView):
    model = UserModel

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()
        qs = UserModel.objects.annotate(total_ads=Count('adsmodel'))
        user = get_object_or_404(qs, pk=self.object.id)
        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "user_name": self.object.user_name,
            "role": self.object.role,
            "age": self.object.age,
            "location": self.object.location.name,
            "total_ads": user.total_ads
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = UserModel
    fields = ["first_name", "last_name", "user_name", "password",
              "role", "age", "location"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        first_name = user_data.get("first_name")
        if first_name:
            self.object.first_name = first_name

        last_name = user_data.get("last_name")
        if last_name:
            self.object.last_name = last_name

        user_name = user_data.get("user_name")
        if user_name:
            self.object.user_name = user_name

        password = user_data.get("password")
        if password:
            self.object.password = password

        role = user_data.get("role")
        if role:
            self.object.role = role

        age = user_data.get("age")
        if age:
            self.object.age = age

        location = user_data.get("location")
        if location:
            location_obj, created = LocationModel.objects.get_or_create(name=location)
            self.object.location = location_obj

        try:
            self.object.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "user_name": self.object.user_name,
            "role": self.object.role,
            "age": self.object.age,
            "location": self.object.location.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = UserModel
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
