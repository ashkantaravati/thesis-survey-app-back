from rest_framework import viewsets, generics

from main.models.response import Response
from main.serializers.response_serializer import ResponseSerializer

from .models import Organization, Team
from .serializers import (
    OrganizationRegistrationSerializer,
    TeamSerializer,
)


class TeamInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet to get info about a team
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class CreateOrganizationView(generics.ListCreateAPIView):
    """
    A View for submitting an organization, its teams and initial data for team members
    """

    queryset = Organization.objects.all()
    serializer_class = OrganizationRegistrationSerializer


class ResponseView(generics.ListCreateAPIView):
    """
    A View for submitting a the answers of a participant from a team within an organization to the survey's questions
    """

    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
