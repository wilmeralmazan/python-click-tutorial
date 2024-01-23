import pytest

from click.testing import CliRunner

from cli_tools.authenticate2 import auth


def test_non_admin_auth():
    # Arrange
    runner = CliRunner()
    prompt_inputs = "\n".join([
        'wilmer',
        'test',
        'test',
        'N'
    ])

    # Act
    result = runner.invoke(auth, input=prompt_inputs)

    # Asserts
    assert result.exit_code == 0

    expected_output = "\n".join([
        'Username:: wilmer',
        'password: ',
        'Repeat for confirmation: ',
        'Are you an Admin? [y/N]: N',
        'Logging as wilmer',
    ]) + "\n"

    assert result.output == expected_output

def test_admin_auth():
    # Arrange
    runner = CliRunner()
    prompt_inputs = "\n".join([
        'wilmer',
        'test',
        'test',
        'y',
        '100'
    ])

    # Act
    result = runner.invoke(auth, input=prompt_inputs)

    # Asserts
    assert result.exit_code == 0

    expected_output = "\n".join([
        'Username:: wilmer',
        'password: ',
        'Repeat for confirmation: ',
        'Are you an Admin? [y/N]: y',
        'Admin ID: > 100',
        'Logging in admin wilmer (ID 100)'
    ]) + "\n"

    assert result.output == expected_output