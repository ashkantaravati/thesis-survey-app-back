from rest_framework import routers
from main.views import CreateOrganizationView, TeamInfoViewSet

router = routers.SimpleRouter()
router.register(r"teams", TeamInfoViewSet)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("organizations", CreateOrganizationView.as_view()),
]

urlpatterns += router.urls
