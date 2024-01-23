# fileutils.py

import click
import typing
import requests

@click.command()
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


@click.command()
@click.argument('inputs', type=click.File('r'), nargs=-1)
@click.argument('output', type=click.File('w'))
def concat(inputs: typing.Collection[typing.IO], output: typing.IO):
    """Concatenates the contents of one or more files into an output file."""
    for f in inputs:
        for line in f:
            output.write(line)
        click.echo(f"{f.name} written to {output.name}")


@click.command()
@click.argument('inputs', nargs=-1)
def download(inputs):
    """Downloads web resources from (url, filename) input pairs
    
    Example:
      download http://xyz.com/p1.txt,page1.txt http://xyz.com/p2.txt,page2.txt

      This fetches web resources by URL and saves them locally to filename    
    """

    with click.progressbar(inputs)as bar:
        for item in bar:
            url, filename = item.split(',')
            response = requests.get(url)
            with open(filename, 'w') as fo:
                fo.write(response.text)