import os

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
