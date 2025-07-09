import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = [
        "university", "institute", "college", "school",
        "dept", "department", "faculty", "hospital", "centre", "center"
    ]
    non_academic_keywords = [
        "inc", "ltd", "llc", "corp", "corporation",
        "pharma", "biotech", "company", "technologies", "laboratories"
    ]

    text = affiliation.lower()

    if any(word in text for word in non_academic_keywords):
        return True

    if any(word in text for word in academic_keywords):
        return False

    # If no clear signal, assume possible company!
    return True

def extract_emails(text: str):
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

def extract_companies(affiliation: str) -> str:
    non_academic_keywords = [
        "inc", "ltd", "llc", "corp", "corporation",
        "pharma", "biotech", "company", "technologies", "laboratories"
    ]

    parts = [p.strip() for p in affiliation.split(",")]

    for part in parts:
        text = part.lower()
        if any(word in text for word in non_academic_keywords):
            return part  # found company-like chunk

    return affiliation  # fallback → whole affiliation
