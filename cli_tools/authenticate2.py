# authenticate2.py

import click 

@click.command()
def auth():
    """Provides user authentication"""

    username = click.prompt("Username:")
    password = click.prompt("password", hide_input=True, confirmation_prompt=True)

    click.echo(f"Logging as {username}")
