from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer


class TeamInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet to get info about a team
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
