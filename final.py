import re
import sys

# Constants
PATTERN_FEATURES = re.compile("^[\s]{5}[a-z_A-Z]{0,}[\s]{0,}[0-9]{0,9}[\.]{2}[0-9]{0,}")
PATTERN_POLYSTAAART = re.compile("^[\s]{5}[a-zA-Z_]{0,}[\s]{0,}[0-9]{0,}$")
PATTERN_DNA = re.compile("ORIGIN")
NUCLEOTIDES = ["a","c","t","g"]


def cluster(filename):
    definition = ""
    features = []
    dna_sequencie = []


    with open(filename) as file:
        for line in file:
            line = line.strip("\n")
            if "DEFINITION" in line:
                definition = "".join(map(str,line[0:]))
            if PATTERN_FEATURES.search(line):
                features.append(line)
            if PATTERN_POLYSTAAART.search(line):
                features.append(line)
            if PATTERN_DNA.search(line):
                dna_sequencie = [x.strip() for x in PATTERN_DNA.findall(line)]
   




    print(features)
    print(definition)
    print(dna_sequencie)

            
            



            

def main():
    cluster("CFTR_mRNA.gb")

main()