DOMAIN_MAP = {
    "Python":["python"],
    "SQL":["sql","mysql","postgres"],
    "Visualization":["matplotlib","seaborn","tableau","powerbi"],
    "Statistics":["regression","probability","hypothesis"],
    "ML":["scikit-learn","tensorflow","keras","pytorch"]
}

MAX_EXPECTED_WEIGHT = 5   # adjust if your extractor uses higher values

def compute_domain_scores(resume_skill_scores):

    domain_scores={}

    for domain,skills in DOMAIN_MAP.items():

        score=0
        count=0

        for s in skills:
            if s in resume_skill_scores:
                score+=resume_skill_scores[s]
                count+=1

        if count>0:
            avg = score/count
            normalized = round((avg/MAX_EXPECTED_WEIGHT)*100,2)
            domain_scores[domain]=normalized
        else:
            domain_scores[domain]=0

    return domain_scores