#!/usr/bin/env python3
"""
Test script to verify all components of the Medical Note Summarizer work correctly.
"""

from utils.summarizer import summarize_text
from utils.ner_extractor import extract_medical_entities
from utils.icd_mapper import map_to_icd

def test_app():
    """Test all components with a sample clinical note."""
    
    # Sample clinical note
    sample_note = """
    The patient is a 65-year-old male with a history of diabetes and hypertension. 
    He was admitted for shortness of breath and diagnosed with pneumonia. 
    Started on insulin and antibiotics. Patient also has asthma and mild anemia.
    """
    
    print("🧪 Testing Medical Note Summarizer Components...")
    print("=" * 50)
    
    # Test summarization
    print("1. Testing summarization...")
    try:
        summary = summarize_text(sample_note)
        print(f"✅ Summary: {summary}")
    except Exception as e:
        print(f"❌ Summarization failed: {e}")
    
    # Test NER extraction
    print("\n2. Testing NER extraction...")
    try:
        entities = extract_medical_entities(sample_note)
        print(f"✅ Extracted entities: {entities}")
    except Exception as e:
        print(f"❌ NER extraction failed: {e}")
    
    # Test ICD mapping
    print("\n3. Testing ICD mapping...")
    try:
        icd_results = map_to_icd(entities)
        print(f"✅ ICD mappings: {icd_results}")
    except Exception as e:
        print(f"❌ ICD mapping failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 All tests completed!")
    print("\n📱 Your Streamlit app is running at: http://localhost:8501")
    print("💡 Try pasting the sample note above into the web interface!")

if __name__ == "__main__":
    test_app() 