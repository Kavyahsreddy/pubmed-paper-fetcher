import re

def is_non_academic(affiliation: str) -> bool:
    """
    Heuristic to decide if affiliation is non-academic.
    """
    academic_keywords = [
        "university", "college", "school", "institute",
        "department", "centre", "center", "faculty", "hospital"
    ]

    # if any academic word matches, treat as academic
    affil_lower = affiliation.lower()
    if any(word in affil_lower for word in academic_keywords):
        return False

    # if it has @, consider email => more likely non-academic
    if "@" in affiliation:
        return True

    # fallback: if length is short, assume company name
    if len(affiliation.split()) <= 5:
        return True

    # else treat as non-academic if no academic words found
    return True

def extract_emails(text: str):
    """
    Extract email addresses from text.
    """
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)


def extract_companies(affiliation: str) -> str:
    """
    Try to extract company name heuristically.
    """
    company_keywords = [
        "Inc", "Ltd", "LLC", "Corporation", "Corp", "Biotech",
        "Pharma", "Technologies", "Labs", "Laboratories",
        "Therapeutics", "Diagnostics", "Solutions", "Industries",
        "Research", "Bio", "Genomics", "Biosciences",
        "Life Sciences", "Medical", "Healthcare", "Systems"
    ]

    parts = [part.strip() for part in affiliation.split(",")]

    for part in parts:
        for keyword in company_keywords:
            if keyword.lower() in part.lower():
                return part

    return ""
