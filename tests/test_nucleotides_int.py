from click.testing import CliRunner

from sanger.assignment.cli import cli


def test_nucleotide_amount(
    runner: CliRunner,
    test_file_path: str,
):
    result = runner.invoke(cli, ["nucleotide-amount", test_file_path])

    assert result.exit_code == 0
    assert result.output == str(2525000)
