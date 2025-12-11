# src/retrieval/pdf_extractor.py

from pypdf import PdfReader
from typing import List

def extract_pages_from_pdf(pdf_path: str) -> List[str]:
    """
    Extracts text from a PDF file and returns a list of page strings.
    Each entry corresponds to one PDF page.
    """
    reader = PdfReader(pdf_path)
    pages_text = []
    for page in reader.pages:
        text = page.extract_text()
        pages_text.append(text if text else "")
    return pages_text
