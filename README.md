Resume Information Extraction System

Overview

A Python-based resume information extraction system that extracts structured information from PDF and DOCX resumes without using Large Language Models (LLMs) or Generative AI APIs.

Features

- Extracts full name, email address, and phone number.
- Identifies skills using rule-based techniques.
- Extracts education and work experience where available.
- Identifies LinkedIn and GitHub profile links.
- Returns structured JSON output.
- Supports PDF and DOCX resume files.

Technologies Used

- Python 3
- Regular Expressions
- PyMuPDF (fitz) for PDF parsing
- python-docx for DOCX parsing
- unittest for automated testing

Project Structure

- "src/extractor.py" — Resume extraction logic
- "src/main.py" — Command-line interface
- "samples/" — Sample resumes
- "outputs/" — Extracted JSON results
- "tests/" — Sample generator and automated tests

Setup

Create and activate a virtual environment.

On Windows PowerShell:

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

Usage

Extract information from a PDF resume:

python src/main.py samples/resume_john.pdf --output outputs/john.json

Extract information from a DOCX resume:

python src/main.py samples/resume_priya.docx --output outputs/priya.json

Run Tests

python -m unittest discover -s tests -p "test_*.py" -v

Limitations

This system uses rule-based extraction and regular expressions. Results may vary depending on resume formatting, and scanned PDFs may require OCR support. Some optional fields may be missing when the resume does not contain recognizable information.

AI Usage

The extraction system does not call external LLM or Generative AI APIs. It uses conventional Python parsing and rule-based techniques.