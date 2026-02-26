from django.urls import path
from .views import (
    SkillGapAnalyzerView,
    AnalysisHistoryView,
    SendAnalysisEmailView,
    AnalyticsView,
    readiness_trend
)
from .auth_views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('analyze/', SkillGapAnalyzerView.as_view()),
    path('history/', AnalysisHistoryView.as_view()),
    path('send-email/', SendAnalysisEmailView.as_view()),
    path('analytics/',AnalyticsView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('trend/',readiness_trend),
]