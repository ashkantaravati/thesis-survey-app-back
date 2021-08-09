from rest_framework.response import Response
from main.serializers.team_info_serializers import OrganizationSerializer
from rest_framework import viewsets, generics
from .models import Organization, ParticipantTeamMember, Team
from .serializers import (
    OrganizationRegistrationSerializer,
    TeamMemberParticipationSerializer,
    TeamSerializer,
)
from main import serializers


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


class SurveyParticipationView(generics.RetrieveUpdateAPIView):
    """
    A View for submitting a the answers of a participant from a team within an organization to the survey's questions
    """

    queryset = ParticipantTeamMember.objects.all()
    serializer_class = TeamMemberParticipationSerializer

class StatsView(generics.ListAPIView):
    """
    A View for listing all organizations
    """

    queryset = Organization.objects.all()
    serializer_class = OrganizationRegistrationSerializer

    def list(self, request):
        """
        This view should return a list of all the organizations for
        the user as determined by the username portion of the URL.
        """
        queryset = self.get_queryset()
        serializer = OrganizationRegistrationSerializer(queryset, many=True)
        return Response({'organizations' : len(queryset)})