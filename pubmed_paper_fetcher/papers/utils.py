import re

def is_non_academic(affiliation: str) -> bool:
    """
    Heuristic to decide if affiliation is non-academic.
    Looks for company-like keywords. Rejects common academic/hospital keywords.
    """
    academic_keywords = [
        "university", "institute", "college", "school",
        "dept", "department", "faculty", "hospital", "centre", "center"
    ]
    non_academic_keywords = [
        "inc", "ltd", "llc", "corp", "corporation",
        "pharma", "biotech", "company", "technologies", "laboratories"
    ]

    text = affiliation.lower()

    # If it has a clear company keyword → non-academic
    if any(word in text for word in non_academic_keywords):
        return True

    # If it has an academic/hospital keyword → academic
    if any(word in text for word in academic_keywords):
        return False

    # If nothing matched → assume academic to be safe
    return False


def extract_emails(text: str):
    """
    Extract all email addresses from text.
    """
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)


def extract_companies(affiliation: str) -> str:
    """
    Try to extract a company name from the affiliation text.
    Uses simple keyword heuristic: returns first matching part.
    """
    non_academic_keywords = [
        "inc", "ltd", "llc", "corp", "corporation",
        "pharma", "biotech", "company", "technologies", "laboratories"
    ]

    parts = [p.strip() for p in affiliation.split(",")]

    for part in parts:
        text = part.lower()
        if any(word in text for word in non_academic_keywords):
            return part  # return matching chunk

    return "Not Found"
