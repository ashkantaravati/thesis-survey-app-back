from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Organization, ParticipantTeamMember, Team

TARGET = 70


class StatsView(APIView):
    """
    A View to get stats
    """

    def get(self, request, format=None):
        """
        Returns stats object
        """
        orgs = Organization.objects.all()
        teams = Team.objects.all()
        participants = ParticipantTeamMember.objects.all()

        participated_teams = [team for team in teams if team.has_participated]
        participated_participants = [
            participant for participant in participants if participant.has_participated
        ]
        participated_orgs = [org for org in orgs if org.has_participated]
        stats = {
            "overall": {
                "target_team_size": TARGET,
                "number_of_registered_teams": len(teams),
                "number_of_participated_teams": len(participated_teams),
                "number_of_registered_participants": len(participants),
                "number_of_participated_participants": len(participated_participants),
                "number_of_registered_organizations": len(orgs),
                "number_of_participated_organizations": len(participated_orgs),
            },
            "registered_organizations": [
                {
                    "id": org.id.hashid,
                    "name": org.name,
                    "number_of_teams": len(org.teams.all()),
                }
                for org in orgs
            ],
        }
        return Response(stats)
