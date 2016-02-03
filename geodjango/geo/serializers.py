from django.contrib.auth.models import User
from geo.models import Municipality, Game, MunicipalityOwner, RiskProfile
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.serializers import GeometryField
from rest_framework_gis.serializers import GeoModelSerializer


class MunicipalityOwnerSerializer(ModelSerializer):
    class Meta:
        model = MunicipalityOwner


class MunicipalitySerializer(GeoModelSerializer):
    # owner = MunicipalityOwnerSerializer()
    center = GeometryField()

    class Meta:
        model = Municipality
        geo_field = 'mpoly'
        # exclude = ('mpoly',)


class GameSerializer(ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Game


class RiskProfileSerializer(ModelSerializer):
    class Meta:
        model = RiskProfile
        field = ('game',)
        exclude = ('user',)


class UserSerializer(ModelSerializer):
    risk_profile = RiskProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name',
                  'email', 'risk_profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('risk_profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        RiskProfile.objects.create(user=user, **profile_data)
        return user
