def detect_skill_gap(resume_skills, jd_groups):

    resume_set = set([s.lower() for s in resume_skills])

    matched_groups = []
    missing_groups = []

    for group in jd_groups:

        # Mandatory single skill
        if isinstance(group, str):

            if group.lower() in resume_set:
                matched_groups.append([group])
            else:
                missing_groups.append([group])

        # OR group
        elif isinstance(group, list):

            satisfied = False

            for skill in group:

                if skill.lower() in resume_set:
                    matched_groups.append(group)
                    satisfied = True
                    break

            if not satisfied:
                missing_groups.append(group)

    return missing_groups, matched_groups