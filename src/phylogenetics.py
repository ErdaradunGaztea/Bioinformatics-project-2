from os import listdir, mkdir, path

from Bio.Phylo import Consensus
from Bio import Phylo, SeqIO
from Bio.Align.Applications import MuscleCommandline

from src.similarity import cluster


def draw_sample_tree():
    """
    Task 2.b)
    Simple enough not to be worth talking about it
    """
    tree = Phylo.read("input/sample.dnd", "newick")
    Phylo.draw_ascii(tree)


def align_w_muscle(in_file, out_file):
    """
    Used to generate trees, curiously. Whatever, works like a charm.
    """
    mcl = MuscleCommandline("muscle3.8.31_i86win32.exe", input=in_file, tree1=out_file)
    mcl()


def write_by_cluster():
    """
    Splits data into separate fasta files based on cluster.
    """
    if not path.isdir("data_clustered"):
        mkdir("data_clustered")
    sequences = list(SeqIO.parse("data_renamed/all.fasta", "fasta"))
    clusters = cluster()
    for i in range(8):
        sequence_subset = [seq for seq, cl in zip(sequences, clusters) if cl == i]
        SeqIO.write(sequence_subset, "data_clustered/cluster" + str(i) + ".fasta", "fasta")


def build_trees_by_group():
    """
    Task 2.c)
    Subtask i.
    """
    if not path.isdir("trees"):
        mkdir("trees")
    files = [f for f in listdir("data_renamed") if f != "all.fasta"]
    for f in files:
        align_w_muscle("data_renamed/" + f, "trees/" + f[:-6] + ".dnd")
    return [Phylo.read("trees/" + f[:-6] + ".dnd", "newick") for f in files]


def build_trees_by_cluster():
    """
    Task 2.c)
    Subtask ii.
    """
    if not path.isdir("trees_clustered"):
        mkdir("trees_clustered")
    files = [f for f in listdir("data_clustered")]
    for f in files:
        align_w_muscle("data_clustered/" + f, "trees_clustered/" + f[:-6] + ".dnd")
    return [Phylo.read("trees_clustered/" + f[:-6] + ".dnd", "newick") for f in files]


def build_common_tree():
    """
    Task 2.c)
    Subtask iii.
    """
    if not path.isdir("tree_common"):
        mkdir("tree_common")
    align_w_muscle("data_renamed/all.fasta", "tree_common/all.dnd")
    return Phylo.read("tree_common/all.dnd", "newick")


def find_consensus(trees):
    """
    Task 2.d)
    Call with lists of trees generated in task 2.c)
    """
    return Consensus.majority_consensus(trees)
