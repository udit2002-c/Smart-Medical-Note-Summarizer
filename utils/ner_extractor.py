import spacy
import re

# Try to load spaCy models, with graceful fallback
try:
    nlp = spacy.load("en_core_web_sm")
    SPACY_AVAILABLE = True
except Exception:
    # Fallback: simple keyword-based extraction
    SPACY_AVAILABLE = False
    print("Warning: spaCy model not available. Using keyword-based extraction.")

def extract_medical_entities(text):
    """
    Extract named entities from text using spaCy or keyword-based fallback.
    Args:
        text (str): The clinical note.
    Returns:
        List[Tuple[str, str]]: List of (entity, label) pairs.
    """
    if SPACY_AVAILABLE:
        # Use spaCy for NER
        doc = nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities
    else:
        # Fallback: keyword-based extraction
        return extract_medical_keywords(text)

def extract_medical_keywords(text):
    """
    Extract medical keywords using regex patterns.
    Args:
        text (str): The clinical note.
    Returns:
        List[Tuple[str, str]]: List of (keyword, "MEDICAL") pairs.
    """
    # Medical keywords to look for
    medical_patterns = [
        r'\b(diabetes|diabetic)\b',
        r'\b(hypertension|high blood pressure)\b',
        r'\b(asthma)\b',
        r'\b(pneumonia)\b',
        r'\b(anemia)\b',
        r'\b(covid|covid-19|coronavirus)\b',
        r'\b(stroke)\b',
        r'\b(heart failure)\b',
        r'\b(depression)\b',
        r'\b(insulin)\b',
        r'\b(metformin)\b',
        r'\b(antibiotics)\b',
        r'\b(chest pain)\b',
        r'\b(shortness of breath)\b',
        r'\b(fever)\b',
        r'\b(cough)\b'
    ]
    
    entities = []
    text_lower = text.lower()
    
    for pattern in medical_patterns:
        matches = re.finditer(pattern, text_lower)
        for match in matches:
            # Get the original case from the text
            start, end = match.span()
            original_text = text[start:end]
            entities.append((original_text, "MEDICAL"))
    
    return entities

# Note: For better medical NER, install spaCy model:
# python -m spacy download en_core_web_sm 