# sanger-institute-assignment

## Installation
The code was tested on Python 3.10, so you'll need that to run the program.
```bash
git clone git@github.com:xunto/sanger-institute-assignment.git
cd sanger-institute-assignment
pip install -e .
```

## Running
```bash
# Count the sequences
python -m sanger.assignment sequence-amount file.fastq.gz

# Count the nucleotides
python -m sanger.assignment sequence-amount file.fastq.gz
```

## Things to improve:
* Publish to PYPI repository for an easier installation.
