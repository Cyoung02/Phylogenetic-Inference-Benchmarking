#!/usr/bin/env python3
import argparse
import subprocess
import os
import numpy as np
import math
from scipy.special import comb
from collections import defaultdict
from skbio.stats.distance import mantel

# parse args
parser = argparse.ArgumentParser(description="Given two tn93-format distance files, calculate the mantel correlation between them")
parser.add_argument("-d1", "--dists_1", required=True, help="Fist distances (tn-93)")
parser.add_argument("-d2", "--dists_2", required=True, help="Second distances (tn-93)")
parser.add_argument("-c", "--correlation", required=False, default="spearman", help="correlation coefficient to be used in mantel test (default: spearman)")
args = parser.parse_args()

# check valid correlation
if args.correlation != "spearman" and args.correlation != "pearson":
    raise ValueError("Invalid correlation: %s\n* Valid Options: pearson, spearman" % args.correlation)

# read each file into a 2D dictionary 
def read_file(filename):
    f = open(filename)
    lines = f.readlines()
    result = defaultdict(dict)

    # add lines to dictionary
    for line in lines:
        try:
            data = line.split(",")
            result[data[0]][data[1]] = float(data[2].strip())
            result[data[1]][data[0]] = float(data[2].strip())
        except:
            continue

    # add redundant distances
    for name in result:
        if name not in result[name]:
            result[name][name] = 0

    return result

dict_1 = read_file(args.dists_1)
dict_2 = read_file(args.dists_2)

array_1 = np.empty([len(dict_1), len(dict_1)])
array_2 = np.empty([len(dict_2), len(dict_2)])

# convert dictionaries into numpy arrays
curr_row = 0
for id_1 in sorted(dict_1.keys()):
    curr_col = 0
    for id_2 in sorted(dict_1.keys()):
        array_1[curr_row][curr_col] = dict_1[id_1][id_2]
        array_2[curr_row][curr_col] = dict_2[id_1][id_2]
        curr_col += 1
    curr_row += 1

# calculate mantel correlation
coeff, p_value, n = mantel(array_1, array_2, method=args.correlation, permutations=0)
print("Mantel Correlation Statistic (", args.correlation, "):", coeff)
#print("p-Value: %f" % p_value)
