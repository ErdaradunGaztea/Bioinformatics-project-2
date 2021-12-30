import re
from itertools import chain
from os import listdir, path, mkdir

from Bio import SeqIO


def reset_id(sequence, protein):
    """
    Simplifies descriptions for tree printing purposes.
    """
    organism = re.search(r"\[(.*)\]", sequence.description).groups()[0].replace(" ", "-")
    sequence.id = protein + "_" + organism
    sequence.name = sequence.id
    sequence.description = sequence.id
    return sequence


def rename_sequences():
    """
    It is enough to run it once.
    """
    if not path.isdir("data_renamed"):
        mkdir("data_renamed")
    for f in listdir("data"):
        if f != "all.fasta":
            sequences = [reset_id(s, f[:-6]) for s in SeqIO.parse("data/" + f, "fasta")]
            SeqIO.write(sequences, "data_renamed/" + f, "fasta")


def merge_fasta_files(directory="data"):
    """
    Run for all data folders where merged data is necessary.
    """
    sequences = [SeqIO.parse(directory + "/" + f, "fasta") for f in listdir(directory) if f != "all.fasta"]
    sequences = list(chain.from_iterable(sequences))
    SeqIO.write(sequences, directory + "/all.fasta", "fasta")
