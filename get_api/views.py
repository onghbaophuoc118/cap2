from get_api.models import PatientInfo
from get_api.serializers import PatientInfoSerializer
from rest_framework import viewsets


class PatientInfoViewSet(viewsets.ModelViewSet):
    queryset = PatientInfo.objects.all()
    serializer_class = PatientInfoSerializer