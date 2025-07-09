import typer
from pubmed_paper_fetcher.papers.fetcher import fetch_pubmed_ids, fetch_pubmed_details
from pubmed_paper_fetcher.papers.parser import parse_xml
from pubmed_paper_fetcher.papers.exporter import save_to_csv

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: str = typer.Option(None, "-f", "--file", help="Filename to save output CSV"),
    debug: bool = typer.Option(False, "-d", "--debug", help="Enable debug output")
):
    if debug:
        typer.echo(f"Searching for: {query}")

    ids = fetch_pubmed_ids(query)
    if debug:
        typer.echo(f"Found {len(ids)} papers.")

    xml_data = fetch_pubmed_details(ids)
    results = parse_xml(xml_data)

    if file:
        save_to_csv(results, file)
        typer.echo(f"Saved {len(results)} results to {file}")
    else:
        for r in results:
            typer.echo(r)

if __name__ == "__main__":
    app()
