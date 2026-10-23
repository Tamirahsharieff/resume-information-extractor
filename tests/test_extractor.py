import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from extractor import (
    extract_email,
    extract_phone,
    extract_skills,
    extract_resume,
)


class TestResumeExtractor(unittest.TestCase):

    def test_email_extraction(self):
        self.assertEqual(
            extract_email("Contact: test@example.com"),
            "test@example.com"
        )

    def test_missing_email(self):
        self.assertIsNone(extract_email("No email provided"))

    def test_phone_extraction(self):
        phone = extract_phone("Phone: +91 9876543210")
        self.assertEqual(phone, "+919876543210")

    def test_skill_extraction(self):
        skills = extract_skills("Python, SQL and Machine Learning")
        self.assertIn("Python", skills)
        self.assertIn("SQL", skills)
        self.assertIn("Machine Learning", skills)

    def test_pdf_resume(self):
        result = extract_resume(ROOT / "samples" / "resume_john.pdf")
        self.assertEqual(result["name"], "JOHN DOE")
        self.assertEqual(result["email"], "john.doe@example.com")
        self.assertIn("Python", result["skills"])

    def test_docx_resume(self):
        result = extract_resume(ROOT / "samples" / "resume_priya.docx")
        self.assertEqual(result["name"], "PRIYA SHARMA")
        self.assertEqual(result["email"], "priya.sharma@example.org")
        self.assertIn("SQL", result["skills"])


if __name__ == "__main__":
    unittest.main()