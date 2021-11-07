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


class DashboardView(APIView):
    def post(self, request):
        email = request.data.get("email")
        token = request.data.get("token")
        if email and token:
            org = authenticate_organization_rep(email, token)
            if org:
                org_stats = {
                    "name": org.name,
                    "rep_name": org.rep_name,
                    "has_participated": org.has_participated,
                    "date_registered": org.created_at,
                    "number_of_participated_teams": org.number_of_participated_teams,
                    "teams": [
                        {
                            "id": team.id.hashid,
                            "name": team.name,
                            "size": team.number_of_members,
                            "has_participated": team.has_participated,
                            "participated_count": team.number_of_participated_members,
                            "members": [
                                {
                                    "name": member.name,
                                    "has_participated": member.has_participated,
                                    "date_participated": member.updated_at,
                                }
                                for member in team.members.all()
                            ],
                        }
                        for team in org.teams.all()
                    ],
                }
                return Response(org_stats)
            else:
                return Response({"error": "اطلاعات وارد شده اشتباه است."}, status=403)
        return Response(status=400)


def authenticate_organization_rep(email, token):
    org = Organization.objects.get(rep_email=email, id=token)
    if org:
        return org
