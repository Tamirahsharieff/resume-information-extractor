Approach, Assumptions, and Limitations

Approach

The system extracts text from PDF and DOCX resumes using PyMuPDF and python-docx. Regular expressions identify email addresses and phone numbers. Rule-based matching identifies skills, while text patterns and section headings help extract names, education, work experience, and professional profile links. The extracted information is returned as structured JSON.

Assumptions

- Resumes contain selectable text rather than only scanned images.
- Contact details generally follow recognizable email and phone formats.
- Skills can be identified using a predefined list of common technical skills.
- Education and work experience may be presented using recognizable headings or text patterns.

Limitations

- Unusual resume layouts may reduce extraction accuracy.
- Scanned PDFs may require OCR, which is not currently included.
- Skills outside the predefined list may not be detected.
- Education and work experience extraction may be incomplete for unconventional formats.
- Missing information may be returned as null or an empty list.

AI and External Services

The extraction process uses conventional Python libraries, regular expressions, and rule-based techniques. It does not call external LLM or Generative AI APIs.