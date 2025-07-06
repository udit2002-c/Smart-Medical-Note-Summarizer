# 🩺 Smart Medical Note Summarizer

A beginner-friendly Streamlit web app to help doctors and hospital staff quickly summarize clinical notes, extract medical keywords, and see mock ICD codes using AI.

## 🌐 Live Demo
**[Try the app online!](https://smart-medical-note-summarizer.streamlit.app)**

## Features
- **Summarize** free-form clinical notes using a pre-trained Hugging Face model (`facebook/bart-large-cnn`).
- **Extract medical keywords** and named entities (diagnosis, medication, symptoms) using spaCy.
- **Display mock ICD codes** based on extracted keywords (hardcoded mapping).
- **PDF Upload Support** - Upload PDF files containing medical notes for automatic text extraction.
- Simple, clean UI with tabbed interface for different input methods.

## Tech Stack
- Python
- Streamlit
- Hugging Face Transformers
- spaCy (with en_core_web_sm or med7)
- PyPDF2 (for PDF text extraction)
- pandas, numpy

## Setup Instructions

### Local Development
1. **Clone the repository**
   ```bash
   git clone https://github.com/udit2002-c/Smart-Medical-Note-Summarizer.git
   cd Smart-Medical-Note-Summarizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy model**
   - For basic demo:
     ```bash
     python -m spacy download en_core_web_sm
     ```
   - (Optional) For better medical NER, install [med7](https://github.com/kamalkraj/med7) following their instructions.

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

### Streamlit Cloud Deployment
1. **Fork this repository** to your GitHub account
2. **Sign up for Streamlit Cloud** at [share.streamlit.io](https://share.streamlit.io)
3. **Connect your GitHub account** and select this repository
4. **Deploy** - Streamlit Cloud will automatically detect the app and deploy it

## How to Use

### Method 1: Text Input
1. Go to the "📝 Paste Text" tab
2. Paste your clinical notes in the text area
3. Click "Analyze Text Notes"

### Method 2: PDF Upload
1. Go to the "📄 Upload PDF" tab
2. Upload a PDF file containing medical notes
3. Click "Analyze PDF Notes"
4. View the extracted text in the expander (optional)

## Example Use Case

1. **Text Input**: Paste a clinical note in the text area, e.g.:
   > The patient is a 65-year-old male with a history of diabetes and hypertension. He was admitted for shortness of breath and diagnosed with pneumonia. Started on insulin and antibiotics.

2. **PDF Upload**: Upload a PDF file containing medical notes

3. Click **Analyze Notes**.

4. The app will show:
   - A concise summary
   - Extracted medical entities (e.g., "diabetes", "hypertension", "pneumonia")
   - Mock ICD codes (e.g., "diabetes" → ICD-E11)

## File Structure
```
Smart-Medical-Note-Summarizer/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── packages.txt          # System dependencies
├── .streamlit/config.toml # Streamlit configuration
├── README.md             # Project documentation
├── test_app.py           # Test script for components
└── utils/
    ├── summarizer.py     # Summarization logic
    ├── ner_extractor.py  # NER extraction logic
    ├── icd_mapper.py     # ICD mapping logic
    └── pdf_extractor.py  # PDF text extraction logic
```

## Notes
- This project is for demo/educational purposes only. ICD mapping is mocked and not for clinical use.
- For advanced NER, consider using med7 or other medical spaCy models.
- PDF files should contain text (not scanned images) for best results.
- The app is optimized for Streamlit Cloud deployment.

---

Made with ❤️ for AI Engineer internship demo. 