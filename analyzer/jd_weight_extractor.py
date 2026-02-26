import re
from .skill_extractor import SKILL_DB
from .semantic_matcher import semantic_skill_match

CRITICAL_PHRASES = [
    "must have",
    "required",
    "mandatory",
    "strong experience in"
]

PREFERRED_PHRASES = [
    "nice to have",
    "preferred",
    "good to have",
    "familiar with"
]

def extract_weighted_jd_skills(jd_groups):

    group_weights = []

    for group in jd_groups:

        # OR-group gets full importance
        if len(group) > 1:
            group_weights.append((group, 1.0))

        # Mandatory single skill
        else:
            group_weights.append((group, 0.8))

    return group_weights