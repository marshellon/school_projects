import re
import sys

# Constants
PATTERN_FEATURES = re.compile("^[\s]{5}[a-z_A-Z]{0,}[\s]{0,}[0-9]{0,9}[\.]{2}[0-9]{0,}") #pattern voor herkennenen wanneer features begint 
PATTERN_POLYSTAAART = re.compile("^[\s]{5}[a-zA-Z_]{0,}[\s]{0,}[0-9]{0,}$") # poly A staarten zijn net iets anders dus andere string voor 
NUCLEOTIDES = ["a","c","t","g"] # hiermee zorg ik er later voor dat alleen letters die in a,t,g,c zitten uit de sequencie worden gehaald 


# functie voor het extracten van de juiste informatie

class Find_dna_Feutures:
    def __init__(self,filename):
        self.filename = self

    def cluster_features(filename):
        definition = ""
        features = []
        dna_sequencie = []


        with open(filename) as file:
            for line in file:
                line = line.strip("\n")
                if "DEFINITION" in line:
                    definition = "".join(map(str,line[0:])) # maken van top stri ,Definition
                if PATTERN_FEATURES.search(line):
                    features.append(line) # alle features opslaan 
                if PATTERN_POLYSTAAART.search(line):
                    features.append(line) # poly A staart feautere
                else:



# main functie voor het runnen van het hele script

def main():

    Find_dna_Feutures.cluster_features("")

main()