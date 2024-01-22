# fileutils.py

import click
import typing

@click.command
@click.argument('fo', type=click.File('a'))
def note(fo):
    """Write notes input to given file."""

    click.echo("Enter lines of text below and CTRL+C to exit")
    try:
        while True:
            value = click.prompt("", prompt_suffix=">")
            fo.write(f"{value}\n")
    except click.Abort:
        click.echo(f"\nOutput written to file {fo.name}")