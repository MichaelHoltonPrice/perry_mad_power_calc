import stru_to_arp
import os

gitDir = os.path.join('C:'+os.sep,'Users','mhp12','git')
projDir = os.path.join(gitDir,'perry_mad_power_calc')

inputFile = os.path.join(projDir,'data','original','PembertonEtAl2013data-G3','pembertonEtAl2013.MS5795.stru')


data = stru_to_arp.stru_to_arp(inputFile,inputFile)


#print(data[len(data)-1])
