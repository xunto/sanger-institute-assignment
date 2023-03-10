from typing import Iterator

from fastq import fastq_object


def count_nucleotides(fq: Iterator[fastq_object]) -> int:
    """Count nucleotides in fastq data."""

    # NOTE: Generator is processing 1 item at a time,
    # so there is constant memory usage.
    return sum(len(v.body) for v in fq)
