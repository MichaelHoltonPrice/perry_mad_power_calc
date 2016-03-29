import os
import numpy as np

class Stru:
    # A class to parse and store the data in a genetic Stru file. This will
    # likely not work for all types of Stru files, but it does work with the
    # Pemberton et al. 2013 Stru file.
    def __init__(self,filePath):
        self.sampleInfoDict = dict() # A dictionary to store each sample's
	                             # Population name, location and
	                             # geographic affiliation

        numLines = sum(1 for line in open(filePath)) # Num lines in file
        self.numSamples = int((numLines-1)/2)
        self.sampleIds = list()
        #self.locusIds = list()

        fin = open(filePath, 'r')
        sampleNum = -1
        for n,line in enumerate(fin):
            if(n==0):
                self.locusIds = line.split(" ")
                self.locusIds = [x.strip() for x in self.locusIds]
                self.numLoci = len(self.locusIds)
                self.repeats = np.empty([self.numSamples,self.numLoci,2], dtype=int)
            else:
                tokens = line.split(" ")
		# Descriptors consists of (from readme file):
                # (1) Individual code number assigned by the source publication
                # (2) Population code number assigned by the source publication
                # (3) Population name
                # (4) Location
                # (5) Pre-defined geographic region affiliation
                # The individual and population code together comprise a unique
		# key for the sample dictionary
                sampleId = (tokens[0],tokens[1])
                repeatData = tokens[5:len(tokens)]
                if sampleId in self.sampleInfoDict:
                    chromosome = 1
                else:
                    chromosome = 0
                    sampleNum = sampleNum + 1
                    self.sampleIds.append(sampleId)
                    self.sampleInfoDict[sampleId] = (tokens[2],tokens[3],tokens[4])
                for locusNum,locus in enumerate(repeatData):
                    self.repeats[sampleNum,locusNum,chromosome] = int(locus)
        fin.close()
        

#class Pemberton:
#    # A class to parse and store the tandem repeat and associated data from
#    # Pemberton et al. 2013 -- Population structure in a comprehensive data
#    # set on human microsatellite variation. The data is located here:
#    #
#    # https://web.stanford.edu/group/rosenberglab/diversity.html
#    def __init__(self,dataDir):
#        # Assume the data is all stored in dataDir with the original filenames.
#        os.path.join(dataDir,"pembertonEtAl2013.MS5879.stru")
#
#    @staticmethod
#    def parse_stru_file(filePath):
#        

def stru_to_arp(inputFile,outputFile,title=""):
    # The following pdf contains a description of the target .arp file type
    # http://cmpg.unibe.ch/software/arlequin35/man/Arlequin35.pdf
    fin = open(inputFile, 'r')
    fout = open(outputFile, 'w+')
    
    fout.write("[Profile]\n")
    fout.write("\tTitle=\"" + title + "\"\n")
    fout.write("\tNbSamples=1\n")
    fout.write("\n")
    fout.write("\tGenotypicData=1\n")
    fout.write("\tGameticPhase=0\n")
    fout.write("\tRecessiveData=0\n")
    fout.write("\tDataType=MICROSAT\n")
    fout.write("\tLocusSeparator=WHITESPACE\n")
    fout.write("\tMissingData=\'?\'\n")
    fout.write("\n")
    fout.write("[Data]\n")
    fout.write("\t[[Samples]]\n")
    fout.write("\n")
    fout.write("\n")
    fout.write("\t\tSampleName=\"Sample 1\"\n")
    fout.write("\t\tSampleSize=25\n")
    fout.write("\t\tSampleData= {\n")
    #numLines = sum(1 for line in open(inputFile))
    data = []
    for n,line in enumerate(fin):
      #print(line)
      if(n>1):
        data.append(line)
        tokens = line.split(" ")
        descriptors = tokens[0:5]
        loci = tokens[5:len(tokens)]

    fin.close()
    fout.close()
    return(data)
