import xmltodict
from typing import List, Dict
from .utils import is_non_academic, extract_emails, extract_companies

def parse_xml(xml_data: str) -> List[Dict]:
    parsed = xmltodict.parse(xml_data)
    articles = parsed["PubmedArticleSet"]["PubmedArticle"]
    if not isinstance(articles, list):
        articles = [articles]

    results = []

    for article in articles:
        try:
            article_data = article["MedlineCitation"]
            article_info = article_data["Article"]
            pubmed_id = article_data["PMID"]["#text"] if isinstance(article_data["PMID"], dict) else article_data["PMID"]
            title = article_info["ArticleTitle"]
            date = article_info["Journal"]["JournalIssue"]["PubDate"].get("Year", "Unknown")
            authors = article_info.get("AuthorList", {}).get("Author", [])

            if not isinstance(authors, list):
                authors = [authors]

            non_academic_authors = []
            company_names = []
            emails = []

            for author in authors:
                affiliation = author.get("AffiliationInfo", [{}])[0].get("Affiliation", "")
                if is_non_academic(affiliation):
                    name = f"{author.get('ForeName', '')} {author.get('LastName', '')}".strip()
                    non_academic_authors.append(name)
                    emails += extract_emails(affiliation)

                    company = extract_companies(affiliation)
                    if company:
                        company_names.append(company)

            if non_academic_authors:
                results.append({
                    "PubmedID": pubmed_id,
                    "Title": title,
                    "Publication Date": date,
                    "Non-academic Author(s)": "; ".join(non_academic_authors),
                    "Company Affiliation(s)": "; ".join(set(company_names)) if company_names else "Not Found",
                    "Corresponding Author Email": ", ".join(set(emails)) if emails else "Not Found"
                })
        except Exception:
            continue

    return results
