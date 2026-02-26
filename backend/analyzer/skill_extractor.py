SKILL_DB = [
    "python","c++","c","java","sql","mysql",
    "django","react","node","fastapi",
    "machine learning","deep learning",
    "tensorflow","keras","pytorch",
    "scikit-learn","matplotlib",
    "huggingface","xgboost",
    "docker","aws","git","github"
]
SKILL_DB = [skill.lower() for skill in SKILL_DB]
def extract_skills(text):
    found_skills = []

    for skill in SKILL_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
