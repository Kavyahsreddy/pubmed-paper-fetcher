import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "institute", "college", "school", "dept", "department"]
    return not any(word in affiliation.lower() for word in academic_keywords)

def extract_emails(text: str):
    return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)

def extract_companies(affiliation: str) -> str:
    return affiliation.split(",")[0].strip()
