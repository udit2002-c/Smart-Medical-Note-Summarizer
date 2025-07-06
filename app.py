import streamlit as st
import pandas as pd
import subprocess
import sys
from utils.summarizer import summarize_text
from utils.ner_extractor import extract_medical_entities
from utils.icd_mapper import map_to_icd
from utils.pdf_extractor import extract_text_from_pdf, is_valid_pdf

# Try to install spaCy model if not available
@st.cache_resource
def setup_spacy():
    """Setup spaCy model if not available."""
    try:
        import spacy
        spacy.load("en_core_web_sm")
        return True
    except:
        try:
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_sm"
            ])
            return True
        except:
            st.warning("⚠️ spaCy model not available. Using keyword-based extraction.")
            return False

# Initialize spaCy
setup_spacy()

st.set_page_config(page_title="Smart Medical Note Summarizer", layout="centered")
st.title("🩺 Smart Medical Note Summarizer")
st.write("""
Upload a PDF or paste clinical notes below. Click **Analyze Notes** to get a summary, extract medical keywords, and see mock ICD codes.
""")

# Create tabs for different input methods
tab1, tab2 = st.tabs(["📝 Paste Text", "📄 Upload PDF"])

with tab1:
    # Text area for user input
    user_input = st.text_area("Paste clinical notes here:", height=200)
    analyze_text = st.button("Analyze Text Notes", key="analyze_text")

with tab2:
    # File uploader for PDF
    uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'], key="pdf_uploader")
    analyze_pdf = st.button("Analyze PDF Notes", key="analyze_pdf")
    
    if uploaded_file is not None:
        if is_valid_pdf(uploaded_file):
            st.success(f"✅ PDF uploaded: {uploaded_file.name}")
            # Show extracted text in an expander
            with st.expander("📄 View extracted text from PDF"):
                try:
                    extracted_text = extract_text_from_pdf(uploaded_file)
                    st.text_area("Extracted text:", value=extracted_text, height=200, disabled=True)
                except Exception as e:
                    st.error(f"Error reading PDF: {str(e)}")
        else:
            st.error("❌ Please upload a valid PDF file.")

# Analysis logic
def analyze_notes(text_input):
    """Analyze the provided text input."""
    if not text_input.strip():
        st.warning("Please provide some text to analyze.")
        return
    
    with st.spinner("Summarizing notes..."):
        summary = summarize_text(text_input)
    st.subheader("📋 Summary")
    st.success(summary)

    with st.spinner("Extracting medical entities..."):
        entities = extract_medical_entities(text_input)
    if entities:
        st.subheader("🏥 Extracted Medical Entities (NER)")
        df_entities = pd.DataFrame(entities, columns=["Entity", "Label"])
        st.dataframe(df_entities)
    else:
        st.info("No named entities found.")

    with st.spinner("Mapping to ICD codes..."):
        icd_results = map_to_icd(entities)
    if icd_results:
        st.subheader("🏷️ Mock ICD Codes")
        df_icd = pd.DataFrame(list(icd_results.items()), columns=["Entity", "ICD Code"])
        st.dataframe(df_icd)
    else:
        st.info("No ICD codes found for extracted entities.")

# Handle button clicks
if analyze_text and user_input:
    analyze_notes(user_input)

if analyze_pdf and uploaded_file is not None:
    if is_valid_pdf(uploaded_file):
        try:
            # Reset file pointer to beginning
            uploaded_file.seek(0)
            extracted_text = extract_text_from_pdf(uploaded_file)
            analyze_notes(extracted_text)
        except Exception as e:
            st.error(f"Error processing PDF: {str(e)}")
    else:
        st.error("Please upload a valid PDF file.")

st.markdown("---")
st.markdown("""
**How it works:**
- **Text Input**: Paste clinical notes directly into the text area
- **PDF Upload**: Upload PDF files containing medical notes (text will be extracted automatically)
- Uses a pre-trained model to summarize your notes
- Extracts medical keywords using spaCy NER or keyword-based extraction
- Maps keywords to mock ICD codes for demo purposes
""")

# Add some helpful tips
with st.sidebar:
    st.markdown("### 💡 Tips")
    st.markdown("""
    - **For best results**: Use clear, well-formatted medical notes
    - **PDF files**: Should contain text (not scanned images)
    - **Supported formats**: Text input or PDF upload
    - **Demo ready**: Perfect for showcasing AI/ML skills!
    """) 