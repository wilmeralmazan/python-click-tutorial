# Import the 'setup' function from the 'setuptools' library, used for packaging and distribution.
from setuptools import setup

# Define the package metadata for distribution.
setup(
    name='cli_tools',  # The name of your package
    version='1.0',     # The version of your package
    py_modules=['greeter',
                'calculator',
                'authenticate',
                'authenticate2',
                'fileutils'
                ],  # List of Python modules to include in the package

    # Specify any dependencies your package requires.
    install_requires=[
        'Click',  # The 'Click' library is a dependency
        'requests'
    ],

    # Define the entry point for the command-line script.
    entry_points={
        'console_scripts': [
            'greetings=greeter:greet',
            'add=calculator:add',
            'subtract=calculator:subtract',
            'authenticate=authenticate:auth',
            'authenticate2=authenticate2:auth',
            'note=fileutils:note',
            'concat=fileutils:concat',
            'notes=notes:main',
            'download=fileutils:download'
        ]
        
    }
)
