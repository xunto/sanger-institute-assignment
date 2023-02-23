import click
import fastq

from sanger.assignment.nucleotides import count_nucleotides
from sanger.assignment.sequences import count_sequences


@click.group()
def cli():
    pass


@click.command()
@click.argument("path")
def sequence_amount(path: str):
    fq = fastq.read(path)

    amount = count_sequences(fq)

    click.echo(amount)


@click.command()
@click.argument("path")
def nucleotide_amount(path: str):
    fq = fastq.read(path)

    amount = count_nucleotides(fq)

    click.echo(amount)


cli.add_command(sequence_amount)
cli.add_command(nucleotide_amount)
