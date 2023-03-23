import click
import fastq

from .stats import collect_stats


@click.command()
@click.argument("path")
def cli(path: str):
    """
    Collect stats for a FASTQ file.

    PATH is a path to a FASTQ file.
    """

    fq = fastq.read(path)
    stats = collect_stats(fq)

    click.echo(f"Nucleotid={stats.nuc_amount}")
    click.echo(f"Sequences={stats.seq_amount}")
    click.echo(f"GC%={stats.gc_percent:.2f}%")
