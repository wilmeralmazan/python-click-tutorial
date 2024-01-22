# greeter.py

# Import the 'click' library, which is used for creating command-line interfaces.
import click

# Define a command-line command using the 'click.command()' decorator.
# This command takes two arguments: 'firstname' and 'lastname'.
@click.command()
@click.argument('firstname')
@click.argument('lastname')
def greet(firstname, lastname):
    """Displays a greeting to the user."""
    
    # Use the 'click.echo()' function to print a greeting message.
    # The message includes the values of 'firstname' and 'lastname'.
    click.echo(f"Hello {firstname} {lastname}")
