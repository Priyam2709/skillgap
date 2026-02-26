from rest_framework import serializers
from .models import Analysis

class ResumeJDSerializer(serializers.Serializer):

    resume = serializers.FileField()
    job_description = serializers.CharField()


class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'