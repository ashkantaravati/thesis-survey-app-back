from rest_framework import routers
from main.views import TeamInfoViewSet

router = routers.SimpleRouter()
router.register(r"teams", TeamInfoViewSet)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls
