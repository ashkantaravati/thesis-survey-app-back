from rest_framework import routers
from main.views import CreateOrganizationView, SurveyParticipationView, TeamInfoViewSet

router = routers.SimpleRouter()
router.register(r"teams", TeamInfoViewSet)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("organizations/", CreateOrganizationView.as_view()),
    path("responses/<str:pk>", SurveyParticipationView.as_view()),
]

urlpatterns += router.urls
