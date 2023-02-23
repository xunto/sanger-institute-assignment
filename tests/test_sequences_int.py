from click.testing import CliRunner

from sanger.assignment.cli import cli


def test_sequence_amount(
    runner: CliRunner,
    test_file_path: str,
):
    result = runner.invoke(cli, ["sequence-amount", test_file_path])

    assert result.exit_code == 0
    assert result.output == str(25000)
