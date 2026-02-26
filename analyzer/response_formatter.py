def unique_list(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def format_output(matched, missing, resume_skill_scores):

    flat_matched = []
    flat_missing = []

    # matched groups → pick best skill from group
    for group in matched:

        best = None
        best_score = 0

        for skill in group:
            if skill in resume_skill_scores:
                if resume_skill_scores[skill] > best_score:
                    best = skill
                    best_score = resume_skill_scores[skill]

        if best:
            flat_matched.append(best)

    # missing groups → show representative skill
    for group in missing:
        for skill in group:
            if skill not in resume_skill_scores:
                flat_missing.append(skill)
                break

    flat_matched = unique_list(flat_matched)
    flat_missing = unique_list(flat_missing)

    return flat_matched, flat_missing