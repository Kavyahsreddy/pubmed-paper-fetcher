import requests
from typing import List

def fetch_pubmed_ids(query: str) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": "20"}
    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.json()["esearchresult"]["idlist"]

def fetch_pubmed_details(ids: List[str]) -> str:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"}
    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.text
