from click.testing import CliRunner

from sanger.assignment.cli import cli


def test_stats(
    runner: CliRunner,
    test_file_path: str,
):
    result = runner.invoke(cli, [test_file_path])

    assert result.exit_code == 0
    assert f"Nucleotid=8\n" + f"Sequences=2\n" + f"GC%=50.00%\n" == result.output
