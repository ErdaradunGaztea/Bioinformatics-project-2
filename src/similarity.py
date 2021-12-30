import numpy as np
import pandas as pd
from Bio.Cluster import treecluster


def cluster():
    """
    Key part of task 1.d)
    """
    distance = np.array(pd.read_csv("input/distances.csv"))
    return treecluster(data=None, distancematrix=distance, method="a").cut(8)
