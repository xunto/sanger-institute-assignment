from os import path

import pytest
from _pytest.fixtures import SubRequest
from click.testing import CliRunner


CURRENT_DIR = path.dirname(path.abspath(__file__))


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture(params=["test.fastq", "test.fastq.gz"])
def test_file_path(request: SubRequest) -> str:
    return path.abspath(path.join(CURRENT_DIR, "fixtures", request.param))
