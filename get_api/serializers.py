from rest_framework import serializers
from get_api.models import PatientInfo


class PatientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = '__all__'