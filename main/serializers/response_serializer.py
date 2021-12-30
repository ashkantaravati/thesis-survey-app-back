from django.db.models import fields
from rest_framework import serializers
from main.models import (
    Response,
)
from hashid_field.rest import HashidSerializerCharField
from main.models.team import Team

from main.serializers.team_info_serializers import TeamSerializer


class ResponseSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True)
    team_id = HashidSerializerCharField()

    def to_representation(self, instance):
        self.fields["team"] = TeamSerializer(read_only=True)
        return super(ResponseSerializer, self).to_representation(instance)

    def create(self, validated_data):
        team_id = validated_data.pop("team_id")
        team = Team.objects.get(id=team_id)
        response = Response.objects.create(team=team, **validated_data)

        return response

    class Meta:
        model = Response
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]
        depth = 1
