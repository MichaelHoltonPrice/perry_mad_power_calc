import os

def stru_to_arp(inputFile,outputFile):
  fin = open(inputFile, 'r')
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
  return(data)
