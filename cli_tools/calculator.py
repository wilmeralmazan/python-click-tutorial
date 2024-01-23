# calculator.py

import click

@click.command()
@click.argument('xs', type=int, nargs=-1)
@click.option('-v',
              '--verbose',
              help="Show Additional Output",
              is_flag=True)
def add(xs, verbose):
    """Adds numbers."""

    if verbose:
        click.echo(f"{' + '.join(str(x) for x in xs)} = { sum(xs)}")
    else:
        click.echo(sum(xs))

@click.command()
@click.argument('xs', type=int, nargs=-1)
@click.option('-v',
              '--verbose',
              help="Show Additional Output",
              is_flag=True)
def subtract(xs,verbose):
    """Adds numbers."""
    results = xs[0]

    for x in xs[1:]:
        results -=x
    
    if verbose:
        click.echo(f" {'-'.join(str(x) for x in xs)} = { results }")
    
    click.echo(results)
