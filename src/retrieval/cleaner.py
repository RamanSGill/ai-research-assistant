# src/retrieval/cleaner.py
import re
import string
from typing import List

PRINTABLE = set(string.printable)

def clean_page_text(page_text: str) -> str:
    """Clean a single page's extracted text."""
    if not page_text:
        return ""
    # remove non-printable characters
    page_text = "".join(ch for ch in page_text if ch in PRINTABLE)
    # normalize whitespace (tabs, multiple spaces)
    page_text = re.sub(r"[ \t]+", " ", page_text)
    # collapse multiple newlines into max two (preserves paragraph breaks)
    page_text = re.sub(r"\n{3,}", "\n\n", page_text)
    # strip leading/trailing whitespace
    return page_text.strip()

def clean_full_text(pages: List[str]) -> str:
    """
    Accepts a list of page strings (or a single big string split by pages),
    cleans each page, and returns a single cleaned string.
    """
    cleaned_pages = [clean_page_text(p) for p in pages if p and p.strip()]
    # join pages with a clear page separator (optional)
    return "\n\n---PAGE BREAK---\n\n".join(cleaned_pages)
