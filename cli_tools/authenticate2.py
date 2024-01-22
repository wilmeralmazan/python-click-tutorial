# authenticate2.py

import click 

@click.command()
def auth():
    """Provides user authentication"""

    username = click.prompt("Username:")
    password = click.prompt("password", hide_input=True, confirmation_prompt=True)

    if click.confirm("Are you an Admin?"):
        admin_id = click.prompt("Admin ID: ", type=int, prompt_suffix='>')
        click.echo(f"Logging in admin {username} (ID {admin_id})")
    else:
        click.echo(f"Logging as {username}")
