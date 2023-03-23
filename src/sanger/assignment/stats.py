from typing import Iterator, NamedTuple

from fastq import fastq_object


class Stats(NamedTuple):
    nuc_amount: int
    seq_amount: int
    gc_percent: float

def count_gc(body: str) -> int:
    return body.count("G") + body.count("C")

def collect_stats(fq: Iterator[fastq_object]) -> Stats:
    nuc_amount = 0
    seq_amount = 0
    gc_count = 0

    for v in fq:
        nuc_amount += len(v.body)
        seq_amount += 1
        gc_count += count_gc(v.body)

    gc_percent = (gc_count / nuc_amount) * 100

    return Stats(
        nuc_amount=nuc_amount,
        seq_amount=seq_amount,
        gc_percent=gc_percent,
    )
