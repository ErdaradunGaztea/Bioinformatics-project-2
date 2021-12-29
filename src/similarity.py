from itertools import chain
from os import listdir

import numpy as np
import pandas as pd
# from Bio.Align import MultipleSeqAlignment
# from Bio.Align.Applications import MuscleCommandline
from Bio.Cluster import treecluster
from Bio.SeqIO import parse, write


def merge_fasta_files():
    sequences = [parse("data/" + f, "fasta") for f in listdir("data") if f != "all.fasta"]
    sequences = list(chain.from_iterable(sequences))
    write(sequences, "data/all.fasta", "fasta")


def cluster():
    distance = np.array(pd.read_csv("input/distances.csv"))
    return treecluster(data=None, distancematrix=distance, method="a").cut(8)


# def align_w_muscle():
#     # mkdir("input")
#     mcl = MuscleCommandline("muscle3.8.31_i86win32.exe", input="data/all.fasta", out="input/aligned.fasta",
#                             tree1="input/sequences.tree")
#     mcl()
#
#
# def create_alignment():
#     sequences = parse("input/aligned.fasta", "fasta")
#     return MultipleSeqAlignment(sequences)
