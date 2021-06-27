from rest_framework import viewsets, generics
from .models import Organization, ParticipantTeamMember, Team
from .serializers import (
    OrganizationRegistrationSerializer,
    TeamMemberParticipationSerializer,
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


class SurveyParticipationView(generics.RetrieveUpdateAPIView):
    """
    A View for submitting a the answers of a participant from a team within an organization to the survey's questions
    """

    queryset = ParticipantTeamMember.objects.all()
    serializer_class = TeamMemberParticipationSerializer
