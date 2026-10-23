from pathlib import Path

import fitz
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
SAMPLES = ROOT / "samples"
SAMPLES.mkdir(exist_ok=True)

john = """JOHN DOE
john.doe@example.com
+91 9876543210
LinkedIn: https://www.linkedin.com/in/johndoe
GitHub: https://github.com/johndoe

SKILLS
Python, SQL, Java, Machine Learning, Git, Flask

EDUCATION
B.Tech - ABC University

WORK EXPERIENCE
Software Development Intern - Example Technologies
Developed Python scripts and tested REST APIs.
"""

priya = """PRIYA SHARMA
priya.sharma@example.org
+91 9123456780
GitHub: https://github.com/priyasharma

SKILLS
Python, Pandas, NumPy, SQL, Power BI, Data Analysis

EDUCATION
B.E. - XYZ Institute of Technology

WORK EXPERIENCE
Data Analyst Intern - Sample Analytics
Prepared reports and cleaned datasets using Python.
"""

alex = """ALEX MORGAN
alex.morgan@example.net
+1 415 555 0134
LinkedIn: https://www.linkedin.com/in/alexmorgan

SKILLS
JavaScript, React, HTML, CSS, Git, REST APIs

EDUCATION
Bachelor's - Example College

WORK EXPERIENCE
Web Development Intern - Demo Web Labs
Built and tested responsive web pages.
"""


def create_pdf(filename, content):
    path = SAMPLES / filename

    with fitz.open() as pdf:
        page = pdf.new_page()
        page.insert_textbox(
            fitz.Rect(50, 50, 550, 750),
            content,
            fontsize=11
        )
        pdf.save(path)

    print(f"Created {filename}")


def create_docx(filename, content):
    document = Document()

    for line in content.splitlines():
        if line.strip():
            document.add_paragraph(line)

    document.save(SAMPLES / filename)
    print(f"Created {filename}")


if __name__ == "__main__":
    print("Starting sample creation...")

    create_pdf("resume_john.pdf", john)
    create_docx("resume_priya.docx", priya)
    create_pdf("resume_alex.pdf", alex)

    print("All three sample resumes are ready!")