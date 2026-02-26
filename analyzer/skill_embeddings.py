from .model_loader import get_model
from .skill_extractor import SKILL_DB

model = get_model()

print("Generating skill embeddings... (only once)")

SKILL_EMBEDDINGS = model.encode(SKILL_DB)