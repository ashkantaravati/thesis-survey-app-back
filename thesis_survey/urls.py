from rest_framework import routers
from main.views import (
    CreateOrganizationView,
    ResponseView,
    TeamInfoViewSet,
)
from main.stats import StatsView, DashboardView


router = routers.SimpleRouter()
router.register(
    r"teams",
    TeamInfoViewSet,
)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/organizations/", CreateOrganizationView.as_view()),
    path("api/responses/", ResponseView.as_view()),
    path("api/stats/", StatsView.as_view()),
    path("api/stats/dashboard", DashboardView.as_view()),
    path("api/", include(router.urls)),
]

urlpatterns += router.urls
