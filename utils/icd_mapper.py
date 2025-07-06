# Mock ICD code mapping dictionary
ICD_MAP = {
    "diabetes": "ICD-E11",
    "hypertension": "ICD-I10",
    "asthma": "ICD-J45",
    "pneumonia": "ICD-J18",
    "anemia": "ICD-D64",
    "covid": "ICD-U07.1",
    "stroke": "ICD-I63",
    "heart failure": "ICD-I50",
    "depression": "ICD-F32",
    # Add more as needed
}

def map_to_icd(entities):
    """
    Map extracted entities/keywords to mock ICD codes.
    Args:
        entities (List[Tuple[str, str]]): List of (entity, label) pairs.
    Returns:
        Dict[str, str]: Mapping of entity to ICD code (if found).
    """
    icd_results = {}
    for entity, _ in entities:
        key = entity.lower()
        for disease, icd in ICD_MAP.items():
            if disease in key:
                icd_results[entity] = icd
    return icd_results 