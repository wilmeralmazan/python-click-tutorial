# Import the 'setup' function from the 'setuptools' library, used for packaging and distribution.
from setuptools import setup

# Define the package metadata for distribution.
setup(
    name='cli_tools',  # The name of your package
    version='1.0',     # The version of your package
    py_modules=['greeter'],  # List of Python modules to include in the package

    # Specify any dependencies your package requires.
    install_requires=[
        'Click'  # The 'Click' library is a dependency
    ],

    # Define the entry point for the command-line script.
    entry_points={
        'console_scripts': 'greetings=greeter:greet'
        # This means that the 'greetings' command will be mapped to the 'greet' function in the 'greeter' module
    }
)
