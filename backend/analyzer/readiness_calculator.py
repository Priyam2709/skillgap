from .skill_weights import SKILL_WEIGHTS

def calculate_weighted_readiness(resume_skill_scores, jd_weighted_groups):

    total = 0
    satisfied = 0

    for group, weight in jd_weighted_groups:

        total += weight

        for skill in group:
            if skill in resume_skill_scores:
                satisfied += weight
                break

    if total == 0:
        return 0

    return round((satisfied / total) * 100, 2)