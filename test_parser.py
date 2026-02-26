from analyzer.resume_parser import extract_resume_text
from analyzer.skill_extractor import extract_skills
from analyzer.jd_parser import clean_jd_text
from analyzer.gap_detector import detect_skill_gap
from analyzer.readiness_calculator import calculate_readiness_score
from analyzer.roadmap_generator import generate_learning_roadmap

resume_text = extract_resume_text("sample_resume.pdf")
resume_skills = extract_skills(resume_text)

jd = """
We are looking for a backend engineer with experience in Python, Django,
Docker, AWS and Machine Learning. Knowledge of SQL is required.
"""

cleaned_jd = clean_jd_text(jd)
jd_skills = extract_skills(cleaned_jd)

missing, matched = detect_skill_gap(resume_skills, jd_skills)

score = calculate_readiness_score(resume_skills, jd_skills)

roadmap = generate_learning_roadmap(missing)

print("Matched Skills:")
print(matched)

print("\nMissing Skills:")
print(missing)

print("\nReadiness Score:")
print(score, "%")

print("\nRecommended Learning Roadmap:")
print(roadmap)
