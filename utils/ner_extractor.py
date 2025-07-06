import spacy

# Try to load med7 if available, else fall back to en_core_web_sm
try:
    nlp = spacy.load("en_core_med7_lg")  # med7 model (if installed)
except Exception:
    nlp = spacy.load("en_core_web_sm")  # fallback to default English model


def extract_medical_entities(text):
    """
    Extract named entities from text using spaCy.
    Args:
        text (str): The clinical note.
    Returns:
        List[Tuple[str, str]]: List of (entity, label) pairs.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Note: med7 provides better medical NER, but en_core_web_sm works for demo. 