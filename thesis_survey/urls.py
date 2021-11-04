from rest_framework import routers
from main.views import (
    CreateOrganizationView,
    SurveyParticipationView,
    TeamInfoViewSet,
)
from main.stats import StatsView

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
    path("api/responses/<str:pk>", SurveyParticipationView.as_view()),
    path("api/stats/", StatsView.as_view()),
    path("api/", include(router.urls)),
]

urlpatterns += router.urls
