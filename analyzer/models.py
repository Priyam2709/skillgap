from django.db import models
from django.contrib.auth.models import User
class SkillAnalytics(models.Model):
    ##job_role = models.CharField(max_length=200,default="Unknown")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)
    count = models.IntegerField(default=1)
class Analysis(models.Model):
    job_role = models.CharField(max_length=200, default="Unknown")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    resume = models.FileField(upload_to='resumes/')

    job_description = models.TextField()

    matched_skills = models.JSONField()

    missing_skills = models.JSONField()

    readiness_score = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Analysis - {self.readiness_score}%"