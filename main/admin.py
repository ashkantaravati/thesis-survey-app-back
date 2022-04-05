from django.contrib import admin


from .actions import export_as_json, export_as_csv
from .models import Organization, Team, Response, OverconfidenceQuiz


class TeamInline(admin.StackedInline):
    model = Team
    can_delete = False


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rep_name", "number_of_teams")

    inlines = [
        TeamInline,
    ]


class ResponseInline(admin.StackedInline):
    model = Response
    exclude = ["organization"]
    can_delete = False


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "organization",
        "size",
        "has_participated",
        "response_rate",
        "number_of_responses",
        "mean_overconfidence_score",
        "mean_age",
        "mean_tenure",
        "mean_team_history",
        "mean_voice_behavior",
        "mean_team_coordination",
        "mean_team_effectiveness",
    )

    readonly_fields = (
        "id",
        "has_participated",
        "number_of_responses",
        "mean_age",
        "mean_tenure",
        "mean_team_history",
        "mean_voice_behavior",
        "mean_team_coordination",
        "mean_team_effectiveness",
    )


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "team",
        "is_useful",
        "sex",
        "age",
        "created_at",
    )

    readonly_fields = (
        "overconfidence_question_one_lower",
        "overconfidence_question_one_upper",
        "overconfidence_question_one_outcome",
        "overconfidence_question_two_lower",
        "overconfidence_question_two_upper",
        "overconfidence_question_three_lower",
        "overconfidence_question_three_upper",
        "overconfidence_question_four_lower",
        "overconfidence_question_four_upper",
        "overconfidence_question_five_lower",
        "overconfidence_question_five_upper",
        "overconfidence_question_six_lower",
        "overconfidence_question_six_upper",
        "overconfidence_question_seven_lower",
        "overconfidence_question_seven_upper",
        "overconfidence_question_eight_lower",
        "overconfidence_question_eight_upper",
        "overconfidence_question_nine_lower",
        "overconfidence_question_nine_upper",
        "overconfidence_question_ten_lower",
        "overconfidence_question_ten_upper",
        "team_coordination_question_one",
        "team_coordination_question_two",
        "team_coordination_question_three",
        "team_coordination_question_four",
        "team_coordination_question_five",
        "team_effectiveness_question_one",
        "team_effectiveness_question_two",
        "team_effectiveness_question_three",
        "team_effectiveness_question_four",
        "team_effectiveness_question_five",
        "team_effectiveness_question_six",
        "team_effectiveness_question_seven",
        "team_effectiveness_question_eight",
        "team_effectiveness_question_nine",
        "team_effectiveness_question_ten",
        "voice_question_one",
        "voice_question_two",
        "voice_question_three",
        "voice_question_four",
        "voice_question_five",
        "voice_question_six",
    )


class OverconfidenceQuizAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "team",
        "sex",
        "age",
        "created_at",
        "overconfidence_score",
        "overconfidence_question_one_lower",
        "overconfidence_question_one_upper",
        "overconfidence_question_two_lower",
        "overconfidence_question_two_upper",
        "overconfidence_question_three_lower",
        "overconfidence_question_three_upper",
        "overconfidence_question_four_lower",
        "overconfidence_question_four_upper",
        "overconfidence_question_five_lower",
        "overconfidence_question_five_upper",
        "overconfidence_question_six_lower",
        "overconfidence_question_six_upper",
        "overconfidence_question_seven_lower",
        "overconfidence_question_seven_upper",
        "overconfidence_question_eight_lower",
        "overconfidence_question_eight_upper",
        "overconfidence_question_nine_lower",
        "overconfidence_question_nine_upper",
        "overconfidence_question_ten_lower",
        "overconfidence_question_ten_upper",
    )

    readonly_fields = (
        "overconfidence_score",
        "overconfidence_question_1_outcome",
        "overconfidence_question_2_outcome",
        "overconfidence_question_3_outcome",
        "overconfidence_question_4_outcome",
        "overconfidence_question_5_outcome",
        "overconfidence_question_6_outcome",
        "overconfidence_question_7_outcome",
        "overconfidence_question_8_outcome",
        "overconfidence_question_9_outcome",
        "overconfidence_question_10_outcome",
    )

    fields = (
        "overconfidence_score",
        "overconfidence_question_1_outcome",
        "overconfidence_question_2_outcome",
        "overconfidence_question_3_outcome",
        "overconfidence_question_4_outcome",
        "overconfidence_question_5_outcome",
        "overconfidence_question_6_outcome",
        "overconfidence_question_7_outcome",
        "overconfidence_question_8_outcome",
        "overconfidence_question_9_outcome",
        "overconfidence_question_10_outcome",
        "overconfidence_question_one_lower",
        "overconfidence_question_one_upper",
        "overconfidence_question_two_lower",
        "overconfidence_question_two_upper",
        "overconfidence_question_three_lower",
        "overconfidence_question_three_upper",
        "overconfidence_question_four_lower",
        "overconfidence_question_four_upper",
        "overconfidence_question_five_lower",
        "overconfidence_question_five_upper",
        "overconfidence_question_six_lower",
        "overconfidence_question_six_upper",
        "overconfidence_question_seven_lower",
        "overconfidence_question_seven_upper",
        "overconfidence_question_eight_lower",
        "overconfidence_question_eight_upper",
        "overconfidence_question_nine_lower",
        "overconfidence_question_nine_upper",
        "overconfidence_question_ten_lower",
        "overconfidence_question_ten_upper",
    )


admin.site.register(OverconfidenceQuiz, OverconfidenceQuizAdmin)
admin.site.add_action(export_as_json, "export_as_json")
admin.site.add_action(export_as_csv, "export_as_csv")
