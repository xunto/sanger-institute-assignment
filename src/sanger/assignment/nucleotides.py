from pprint import pprint
from typing import Iterator

from fastq import fastq_object


def count_nucleotides(fq: Iterator[fastq_object]) -> int:
    pprint(list(fq))
    return 0
