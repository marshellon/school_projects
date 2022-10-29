import re
import sys


# Constants
PATTERN_FEATURES = re.compile("^[\s]{5}[a-z_A-Z]{0,}[\s]{0,}[0-9]{0,9}[\.]{2}[0-9]{0,}") # pattern voor herkennenen wanneer features begint 
PATTERN_POLYSTAAART = re.compile("^[\s]{5}[a-zA-Z_]{0,}[\s]{0,}[0-9]{0,}$") # poly A staarten zijn net iets anders dus andere string voor 
NUCLEOTIDES = ["a","c","t","g"] # hiermee zorg ik er later voor dat alleen letters die in a,t,g,c zitten uit de sequencie worden gehaald 


class Find_dna_Feutures:
    def __init__(self,filename):
        self.filename = self
    
    def index_dna(filename):
        line_count_index = 0 # telt hoeveel lines de file heeft
        origin_index = 0
        with open(filename) as file:
            for line in file:
                line = line.strip("\n")
                line_count_index = line_count_index + 1
                if "ORIGIN" in line:
                    origin_index = origin_index + line_count_index
            return origin_index
    
    def find_DNA(filename,index):
        with open (filename) as file:
            DNA_sequence_list = []
            line_count_index = 0 # telt hoeveel lines de file heeft
            for line in file:
                line = line.strip("\n")
                line_count_index = line_count_index + 1
                if line_count_index > index:
                    DNA_sequence_list.append(line)
        return DNA_sequence_list
                    
    def find_definition(filename):

        definition = ""

        with open(filename) as file:
           for line in file:
                line = line.strip("\n")
                if "DEFINITION" in line:
                    definition = "".join(map(str,line[0:])) # maken van top string: Definition 
        return definition

    def cluster_features(filename):
        features = []
        with open(filename) as file:
            for line in file:
                line = line.strip("\n")
                if PATTERN_FEATURES.search(line):
                    features.append(line) # alle features opslaan 
                if PATTERN_POLYSTAAART.search(line):
                    features.append(line) # poly A staart features
                else:
                    continue    
        return features
            



# main functie laat het scripts draaien

def main():

    features = Find_dna_Feutures.cluster_features("CFTR_mRNA.gb")

    DNA_index = Find_dna_Feutures.index_dna("CFTR_mRNA.gb")

    DNA_sequence = Find_dna_Feutures.find_DNA("CFTR_mRNA.gb",DNA_index)



main()