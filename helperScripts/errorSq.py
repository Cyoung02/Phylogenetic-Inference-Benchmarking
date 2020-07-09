#!/usr/bin/env python3
import argparse
import numpy as np
import math
from scipy.special import comb
from collections import defaultdict

#parse args
parser = argparse.ArgumentParser(description="Given two tn93-format distance files, calculate the average squared error between them")
parser.add_argument("-d1", "--dists_1", required=True, help="Fist distances (tn-93)")
parser.add_argument("-d2", "--dists_2", required=True, help="Second distances (tn-93)")
args = parser.parse_args()

# read each file into a 2D dictionary
def read_file(filename):
    f = open(filename)
    lines = f.readlines()
    result = defaultdict(dict)
    for line in lines:
        try:
            data = line.split(",")
            result[data[0]][data[1]] = float(data[2].strip())
            result[data[1]][data[0]] = float(data[2].strip())
        except:
            continue
    return result
    
dict_1 = read_file(args.dists_1)
dict_2 = read_file(args.dists_2)

# compute squared error
error = 0.0
for id_1 in dict_1:
    for id_2 in dict_1[id_1]:
        error += math.pow(float(dict_1[id_1][id_2]) - float(dict_2[id_1][id_2]), 2)

error = error/(2*comb(len(dict_1), 2))
#print("Mean Error Squared: ", error)
print(error)
