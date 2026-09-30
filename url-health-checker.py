import requests
import click
import re
from rich.console import Console

console = Console()
def check_url(url: str) -> bool:
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
click.echo('URL Health Checker')
@click.command()
@click.argument('file')
def main(file: str):
    with open(file, 'r') as f:
        content = f.read()
    urls = re.findall'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', content)
    errors = []
    for url in urls:
        if not check_url(url):
            errors.append(url)
    if errors:
        console.print(f'[red]Errors:[/red] {len(errors)}', style='bold red')
        for error in errors:
            console.print(error, style='bold red')
    else:
        console.print('[green]No errors found![/green]', style='bold green')
if __name__ == '__main__':
    main()
