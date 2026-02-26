from .skill_extractor import extract_skills
import re

SECTION_WEIGHTS = {
    "skills": 1.0,
    "projects": 0.7,
    "training": 0.5,
    "certificates": 0.4
}

def normalize_section_text(text):
    text = text.lower()

    # split comma-attached skills like keras,tensorflow
    text = re.sub(r',', ' ', text)

    # remove slashes & special separators
    text = re.sub(r'[/|]', ' ', text)

    # remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    return text


def extract_section_weighted_skills(sections):

    skill_scores = {}

    for section, text in sections.items():

        cleaned = normalize_section_text(text)
        extracted = extract_skills(cleaned)

        for skill in extracted:

            weight = SECTION_WEIGHTS.get(section, 0.3)

            if skill not in skill_scores:
                skill_scores[skill] = weight
            else:
                skill_scores[skill] = max(skill_scores[skill], weight)

    return skill_scores