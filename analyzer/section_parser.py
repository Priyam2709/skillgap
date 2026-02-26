def split_resume_sections(text):

    sections = {}

    skill_section = ""
    project_section = ""
    training_section = ""
    certificate_section = ""

    if "skills" in text:
        skill_section = text.split("skills")[1]

    if "projects" in text:
        project_section = text.split("projects")[1]

    if "training" in text:
        training_section = text.split("training")[1]

    if "certificates" in text:
        certificate_section = text.split("certificates")[1]

    sections["skills"] = skill_section
    sections["projects"] = project_section
    sections["training"] = training_section
    sections["certificates"] = certificate_section

    return sections
