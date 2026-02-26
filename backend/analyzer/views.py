from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .domain_mapper import compute_domain_scores
from .serializers import ResumeJDSerializer, AnalysisSerializer
from .models import Analysis, SkillAnalytics
from .resume_parser import extract_resume_text
from .section_parser import split_resume_sections
from .section_weighted_extractor import extract_section_weighted_skills
from .report_service import send_analysis_report
from .jd_parser import clean_jd_text
from .semantic_matcher import semantic_skill_match
from .jd_weight_extractor import extract_weighted_jd_skills

from .gap_detector import detect_skill_gap
from .readiness_calculator import calculate_weighted_readiness
from .response_formatter import format_output
from .roadmap_generator import generate_learning_roadmap

from .skill_extractor import SKILL_DB

import os


# -----------------------------
# ANALYZE RESUME + JD
# -----------------------------
class SkillGapAnalyzerView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ResumeJDSerializer(data=request.data)

        if serializer.is_valid():

            resume_file = serializer.validated_data['resume']
            jd_text = serializer.validated_data['job_description']

            file_path = f"media/{resume_file.name}"

            with open(file_path, 'wb+') as destination:
                for chunk in resume_file.chunks():
                    destination.write(chunk)

            # -----------------------------
            # RESUME PROCESSING
            # -----------------------------
            resume_text = extract_resume_text(file_path)
            sections = split_resume_sections(resume_text)

            resume_skill_scores = extract_section_weighted_skills(sections)
            resume_skills = list(resume_skill_scores.keys())

            # -----------------------------
            # JD PROCESSING
            # -----------------------------
            cleaned_jd = clean_jd_text(jd_text)

            # OR-group JD requirements
            jd_groups = semantic_skill_match(cleaned_jd)

            # Assign weight per requirement
            jd_weighted_groups = extract_weighted_jd_skills(jd_groups)

            # -----------------------------
            # GAP DETECTION
            # -----------------------------
            missing_groups, matched_groups = detect_skill_gap(
                resume_skills,
                jd_groups
            )

            matched, missing = format_output(
                matched_groups,
                missing_groups,
                resume_skill_scores
            )

           # -----------------------------
            # READINESS SCORE
            # -----------------------------
            score = calculate_weighted_readiness(
                resume_skill_scores,
                jd_weighted_groups
            )

            # -----------------------------
            # DOMAIN COMPETENCY
            # -----------------------------
            domain_scores = compute_domain_scores(resume_skill_scores)
            
            # -----------------------------
            # ROADMAP
            # -----------------------------
            roadmap = generate_learning_roadmap(missing)
            for skill in missing:

                obj,created = SkillAnalytics.objects.get_or_create(
                    user=request.user,
                    skill=skill
                )

                if not created:
                    obj.count += 1
                    obj.save()
            os.remove(file_path)

            # -----------------------------
            # SAVE ANALYSIS
            # -----------------------------
            analysis = Analysis.objects.create(
                user=request.user,
                resume=resume_file,
                job_role=cleaned_jd[:50],
                job_description=jd_text,
                matched_skills=matched,
                missing_skills=missing,
                readiness_score=score
            )

            return Response({
                "analysis_id":analysis.id,
                "matched_skills": matched,
                "missing_skills": missing,
                "readiness_score": score,
                "learning_roadmap": roadmap,
                "skill_breakdown": domain_scores
            })

        return Response(serializer.errors)


# -----------------------------
# HISTORY VIEW
# -----------------------------
class AnalysisHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        analyses = Analysis.objects.filter(
            user=request.user
        ).order_by('-created_at')

        serializer = AnalysisSerializer(
            analyses,
            many=True
        )

        return Response(serializer.data)
    


# -----------------------------
# SEND RESULT TO EMAIL
# -----------------------------
class SendAnalysisEmailView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self,request):

        analysis_id = request.data.get("analysis_id")
        email = request.data.get("email")

        try:
            analysis = Analysis.objects.get(
                id=analysis_id,
                user=request.user
            )
        except Analysis.DoesNotExist:
            return Response({"error":"Analysis not found"},status=404)

        send_analysis_report(email,analysis)

        return Response({"message":"Report sent successfully"})
class AnalyticsView(APIView):

    permission_classes=[IsAuthenticated]

    def get(self,request):

        data = SkillAnalytics.objects.filter(
            user=request.user
        )

        result={}

        for d in data:
            result[d.skill]=d.count

        return Response(result)
@api_view(['GET'])
    
def readiness_trend(request):

    if not request.user.is_authenticated:
        return Response({"error":"Unauthorized"},status=401)

    history = Analysis.objects.filter(
        user=request.user
    ).order_by("created_at")

    trend_data = [
        {
            "date":h.created_at.strftime("%d-%m"),
            "score":h.readiness_score
        }
        for h in history
    ]

    return Response(trend_data)