import click
import fastq

from .nucleotides import count_nucleotides
from .sequences import count_sequences


@click.group()
def cli():
    pass


@click.command()
@click.argument("path")
def sequence_amount(path: str):
    """
    Count sequences in a FASTQ file.

    PATH is a path to a FASTQ file.
    """

    fq = fastq.read(path)

    amount = count_sequences(fq)

    click.echo(amount, nl=False)


@click.command()
@click.argument("path")
def nucleotide_amount(path: str):
    """
    Count nucleotides in a FASTQ file.

    PATH is a path to a FASTQ file.
    """

    fq = fastq.read(path)

    amount = count_nucleotides(fq)

    click.echo(amount, nl=False)


cli.add_command(sequence_amount)
cli.add_command(nucleotide_amount)
