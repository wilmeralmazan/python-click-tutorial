# greeter.py

import click


@click.command()
@click.argument('name')
@click.option( '-l',
               '--lang', 
               help='Specify language English (en) or Spanish (es)',
               default='en',
               type=click.Choice(['es', 'en']))
@click.option('--say-it',
            type=int,
            default=1,
            help="Number of times to say greeting")
def greet(name, lang, say_it):
    """Displays a greeting to the user."""

    greetings = "Hello" if lang == 'en' else "Hola"

    for _ in range(say_it):
        click.echo(f"{greetings} {name}")
