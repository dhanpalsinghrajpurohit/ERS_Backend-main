from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import HRProfile, userProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    email = serializers.CharField()
    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = payload
        # token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # first_name = validated_data.pop('first_name',None)
        # email = validated_data.pop('email', None)
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        # if first_name is not None:
        #     instance.set_first_name(first_name)
        # if email is not None:
        #     instance.set_email(email)
        print(instance)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password','first_name','email')


class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRProfile
        fields = ['user','company','description']


class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = ['user','contactNumber','degree','college','experience','skills','ResumeLink','fullname','email']
        optionals_fields = ['user','contactNumber','degree','college','experience','skills','ResumeLink','fullname','email']

class insert_Profile(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = "__all__"


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({'username':self.user.username})
        return data
