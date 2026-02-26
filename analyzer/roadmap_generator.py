COURSE_MAP = {

    "django": "Build REST APIs using Django REST Framework",

    "docker": "Learn Docker fundamentals and containerization",

    "aws": "AWS Cloud Practitioner Essentials",

    "react": "Frontend development using React",

    "sql": "Advanced SQL for backend developers",

    "machine learning": "ML model building using Scikit-learn"

}

def generate_learning_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:
        if skill in COURSE_MAP:
            roadmap.append(COURSE_MAP[skill])
        else:
            roadmap.append(f"Learn basics of {skill}")

    return roadmap
