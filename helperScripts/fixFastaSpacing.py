#!/usr/bin/env python3
import argparse

#parse args
parser = argparse.ArgumentParser(description="remove extraneous spaces from MAFFT file")
parser.add_argument("-i", "--input", required=True, help="input fasta")
args = parser.parse_args()

f = open(args.input, "r")
lines = f.readlines()
f.close()

f = open(args.input, "w")

#process lines
for line in lines:
    if ">" in line:
        f.write(line.strip())
        f.write("\n")
    else:
        f.write(line)
