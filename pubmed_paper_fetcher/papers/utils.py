import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = [
        "university", "college", "school", "institute", "department",
        "hospital", "centre", "center", "faculty", "clinic"
    ]
    affil_lower = affiliation.lower()
    return not any(word in affil_lower for word in academic_keywords)


def extract_emails(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)


def extract_companies(affiliation: str) -> str:
    company_keywords = [
        "Inc", "Ltd", "LLC", "Corporation", "Corp", "Biotech",
        "Pharma", "Technologies", "Labs", "Laboratories",
        "Therapeutics", "Diagnostics", "Solutions", "Industries", "Research"
    ]

    parts = [p.strip() for p in affiliation.split(",")]
    for part in parts:
        for keyword in company_keywords:
            if keyword.lower() in part.lower():
                return part
    return ""
