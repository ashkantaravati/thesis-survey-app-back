from rest_framework.response import Response as APIResponse
from rest_framework.views import APIView

from main.models import response
from .models import Organization, Response, Team

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
        responses = Response.objects.all()

        participated_teams = [team for team in teams if team.has_participated]

        participated_orgs = [org for org in orgs if org.has_participated]
        stats = {
            "overall": {
                "target_team_size": TARGET,
                "number_of_registered_teams": len(teams),
                "number_of_participated_teams": len(participated_teams),
                "number_of_submitted_responses": len(responses),
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
        return APIResponse(stats)


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
                    "teams": [
                        {
                            "id": team.id.hashid,
                            "name": team.name,
                            "size": team.size,
                            "has_participated": team.has_participated,
                            "stats": {
                                "number_of_responses": len(team.responses.all()),
                                "mean_age": team.mean_age,
                                "mean_tenure": team.mean_tenure,
                                "mean_team_history": team.mean_team_history,
                                "mean_voice_behavior": team.mean_voice_behavior,
                                "mean_team_coordination": team.mean_team_coordination,
                                "mean_team_effectiveness": team.mean_team_effectiveness,
                            },
                            "respondants": [
                                {"sex": response.sex, "age": response.age}
                                for response in team.responses.all()
                            ],
                        }
                        for team in org.teams.all()
                    ],
                }
                return APIResponse(org_stats)
            else:
                return APIResponse(
                    {"error": "اطلاعات وارد شده اشتباه است."}, status=403
                )
        return APIResponse(status=400)


def authenticate_organization_rep(email, token):
    org = Organization.objects.get(rep_email=email, id=token)
    if org:
        return org
