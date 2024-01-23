import pytest

from pathlib import Path
from click.testing import CliRunner

from cli_tools.fileutils import concat


def test_concat_2_files():
    runner = CliRunner()

    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as fo:
            fo.write('this is file 1')
        with open('file2.txt', 'w') as fo:
            fo.write('this is file 2')
        
        result = runner.invoke(concat, ['file1.txt', 'file2.txt', 'combined.txt'])

        assert result.exit_code == 0
        assert Path('combined.txt').exists()

        exptect_contents = ['this is file 1this is file 2']
        with open('combined.txt') as fo:
            actual_contents = fo.readlines()
        

        assert actual_contents == exptect_contents

