from django.contrib import admin
from .models import Analysis,SkillAnalytics

@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):

 list_display=[
  "user",
  "job_role",
  "readiness_score",
  "created_at"
 ]

 list_filter=[
  "job_role",
  "created_at"
 ]

 search_fields=[
  "user__username",
  "job_role"
 ]


@admin.register(SkillAnalytics)
class SkillAnalyticsAdmin(admin.ModelAdmin):

 list_display=[
  "user",
  "skill",
  "count"
 ]

 search_fields=[
  "skill"
 ]