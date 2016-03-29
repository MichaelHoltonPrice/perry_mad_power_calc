import os
import numpy as np

class Stru:
    # A class to parse and store the data in a genetic Stru file. This will
    # likely not work for all types of Stru files, but it does work with the
    # Pemberton et al. 2013 Stru file.
    def __init__(self,filePath,missingData=-9):
        self.missingData = missingData
        self.sampleDict = dict() # A dictionary to store each sample's
	                             # Population name, location and
	                             # geographic affiliation
        self.popDict = dict()
        self.regionDict = dict()
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
                indivId,popId,popName,location,region = tokens[0:5]
		# Descriptors consists of (from readme file):
                # (1) Individual code number assigned by the source publication
                # (2) Population code number assigned by the source publication
                # (3) Population name
                # (4) Location
                # (5) Pre-defined geographic region affiliation
                # The individual and population code together comprise a unique
		# key for the sample dictionary
                if region not in self.regionDict:
                    self.regionDict[region] = list()
                    self.regionDict[region].append(popId)
                else:
                    if popId not in self.regionDict[region]:
                        self.regionDict[region].append(popId)
                if popId not in self.popDict:
                    self.popDict[popId] = popName
                sampleId = (indivId,popId) # A unique sample identified (key)
                repeatData = tokens[5:len(tokens)]
                if sampleId in self.sampleDict:
                    chromosome = 1
                else:
                    chromosome = 0
                    sampleNum = sampleNum + 1
                    self.sampleIds.append(sampleId)
                    self.sampleDict[sampleId] = location
                for locusNum,locus in enumerate(repeatData):
                    self.repeats[sampleNum,locusNum,chromosome] = int(locus)
        fin.close()
    def getIdsOfPopulation(self,pop0):
        return([(indiv,pop) for (indiv,pop) in self.sampleIds if pop==pop0])

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
    stru = Stru(inputFile)
    numPop = len(stru.popDict)
    fout = open(outputFile, 'w+')
    
    fout.write("[Profile]\n")
    fout.write("\tTitle=\"" + title + "\"\n")
    fout.write("\tNbSamples=" + str(numPop) + "\n")
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
    pops = stru.popDict.keys()
    for pop in pops:
        ids = stru.getIdsOfPopulation(pop)
        fout.write("\t\tSampleName=\"" + pop + " " + stru.popDict[pop] + "\"\n")
        fout.write("\t\tSampleSize=" + str(len(ids)) + "\n")
        fout.write("\t\tSampleData= {\n")
        for id0 in ids: # id is a reserved keyword, so use id0
            idNum = stru.sampleIds.index(id0)
            fout.write(id0[0] + "_" + id0[1] + "\t" + "1")
            for val in stru.repeats[idNum,:,0]:
                fout.write("\t")
                if(val == stru.missingData):
                    fout.write("?")
                else:
                    fout.write(str(val))
            fout.write("\n")
            fout.write("\t\t")
            for val in stru.repeats[idNum,:,1]:
                fout.write("\t")
                if(val == stru.missingData):
                    fout.write("?")
                else:
                    fout.write(str(val))
            fout.write("\n")
        fout.write("}\n")
    pops = stru.popDict.keys() # The populations (IDs)
    
    fout.write("\n")
    fout.write("[[Structure]]\n")
    fout.write("\n")
    fout.write("\tStructureName=\"Regions\"\n")
    fout.write("\tNbGroups=" + str(len(stru.regionDict)) + "\n")
    regions = stru.regionDict.keys()
    for reg in regions:
        fout.write("\tGroup={\n")
        pops = stru.regionDict[reg]
        for pop in pops:
            fout.write("\t\t\"" + pop + " " + stru.popDict[pop] + "\"\n")
        fout.write("\t}\n")

    fout.close()
