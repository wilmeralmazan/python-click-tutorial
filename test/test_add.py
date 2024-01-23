import pytest

from click.testing import CliRunner

from cli_tools.calculator import add

def test_add():
    runner = CliRunner()

    result = runner.invoke(add, [ '10', '20'])
    assert result.exit_code == 0
    assert result.output == '30\n'

def test_add_verbose():
    runner = CliRunner()

    result = runner.invoke(add, [ '10', '20', '-v'])
    assert result.exit_code == 0
    assert result.output == '10 + 20 = 30\n'