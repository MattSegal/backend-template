from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
# router.register('foo', views.FooViewSet)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("auth/", include("rest_registration.api.urls")),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("api/", include(router.urls)),
]
