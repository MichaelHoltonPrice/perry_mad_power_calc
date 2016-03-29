import stru_to_arp
import os

gitDir = os.path.join('C:'+os.sep,'Users','mhp12','git')
#gitDir = os.path.join('C:'+os.sep,'Users','Michael','git')
projDir = os.path.join(gitDir,'perry_mad_power_calc')

inputFile = os.path.join(projDir,'data','original','PembertonEtAl2013data-G3','pembertonEtAl2013.MS5795.stru')
outputFile = os.path.join(projDir,'data','original','abc_toolbox','pembertonEtAl2013.MS5795.arp')

stru = stru_to_arp.Stru(inputFile)
#data = stru_to_arp.stru_to_arp(inputFile,outputFile,title="PembertonEtAl2013data-G3 for Perry Lab simulation")


#print(data[len(data)-1])
