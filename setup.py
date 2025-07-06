#!/usr/bin/env python3
"""
Setup script for Smart Medical Note Summarizer.
This script installs the required spaCy model.
"""

import subprocess
import sys

def install_spacy_model():
    """Install the required spaCy model."""
    try:
        print("Installing spaCy model...")
        subprocess.check_call([
            sys.executable, "-m", "spacy", "download", "en_core_web_sm"
        ])
        print("✅ spaCy model installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install spaCy model: {e}")
        print("The app will use keyword-based extraction as fallback.")
        return False

if __name__ == "__main__":
    install_spacy_model() 