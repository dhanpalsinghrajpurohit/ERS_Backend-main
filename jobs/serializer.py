from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

from .models import Jobs,Applicant,ShortlistCandidate,SelectedCandidate,Schedule

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ['id','postBy','title','description','skills','salary','vacancy']
        # optional_fields = ['postBy','title','description','skills','salary','vacancy']

class JobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

class ApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applicant
        fields = ['user','job']

class ShortlistCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortlistCandidate
        fields = ['job','user','is_shortlist']
        optionals_fields = ['is_shortlist']


class SelectedCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedCandidate
        fields = ['job','user']


class checkStatusSerializer(serializers.ModelSerializer):
    shortlist = SelectedCandidateSerializer(many=True)
    # shortlist = SelectedCandidateSerializer(many=True)
    class Meta:
        model = ShortlistCandidate
        fields = ['job','user']


class shortlistjobSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=False)
    class Meta:
        model = ShortlistCandidate
        fields = ['job','user']


class selectedlistjobSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=False)
    class Meta:
        model = SelectedCandidate
        fields = ['job','user']

class scheduleSerializer1(serializers.ModelSerializer):
    job = JobSerializer(many=False)
    class Meta:
        model = Schedule
        fields = ['job','user','schedule']

class scheduleSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=False)
    class Meta:
        model = Applicant
        fields = ['job','user']
