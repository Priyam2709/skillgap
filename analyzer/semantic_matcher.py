from .skill_ontology import ONTOLOGY_MAP
from .model_loader import get_model
from .skill_embeddings import SKILL_EMBEDDINGS
from .skill_extractor import SKILL_DB
from sklearn.metrics.pairwise import cosine_similarity
import re


def split_jd_into_phrases(jd_text):
    phrases = re.split(r',|and|\n', jd_text)
    return [p.strip() for p in phrases if p.strip()]


def semantic_skill_match(jd_text, threshold=0.4):

    phrases = split_jd_into_phrases(jd_text)

    model = get_model()
    phrase_embeddings = model.encode(phrases)

    jd_groups=[]
    added=set()

    # -------- ONTOLOGY MATCH --------
    for phrase in phrases:

        phrase_lower=phrase.lower()

        for key in ONTOLOGY_MAP:

            if key.lower() in phrase_lower:

                entry=ONTOLOGY_MAP[key]
                group=tuple(entry["skills"])

                if group in added:
                    continue

                if entry["type"]=="mandatory":
                    for skill in entry["skills"]:
                        jd_groups.append([skill])
                else:
                    jd_groups.append(entry["skills"])

                added.add(group)

    # -------- EMBEDDING MATCH --------
    sim=cosine_similarity(
        phrase_embeddings,
        SKILL_EMBEDDINGS
    )

    for i,score in enumerate(sim.max(axis=0)):
        if score>=threshold:
            jd_groups.append([SKILL_DB[i]])

    return jd_groups