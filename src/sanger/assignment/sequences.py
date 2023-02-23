from typing import Any, Iterator

from fastq import fastq_object


def _iterator_length(iterator: Iterator[Any]):
    """Space efficient way of calculating iterator length."""

    return sum(1 for _ in iterator)


def count_sequences(fq: Iterator[fastq_object]) -> int:
    """Count sequences in fastq data."""

    return _iterator_length(fq)
