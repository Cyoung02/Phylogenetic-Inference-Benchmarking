#!/usr/bin/env python3
import argparse

#parse args
parser = argparse.ArgumentParser(description="convert phylip MSA into FASTA format")
parser.add_argument("-i", "--input", required=True, help="input phylip")
parser.add_argument("-o", "--output", required=True, help="output FASTA")
args = parser.parse_args()

f = open(args.input)
lines = f.readlines()
del lines[0]
f.close()

f = open(args.output, "w")

#process lines
for line in lines:
    if line == "\n":
        break
    f.write(">")
    index = 0
    while line[index] != " ":
        f.write(line[index])
        index += 1
    f.write("\n")
    while line[index] == " ":
        index += 1
    f.write(line[index:])

