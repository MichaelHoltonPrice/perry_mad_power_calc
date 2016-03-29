import stru_to_arp
import os


# Set up the git directory, checking whether this is Mike Price's desktop or
# laptop machine. This could be generalized.
gitDir = os.path.join('C:'+os.sep,'Users','Michael','git')
if not os.path.isfile(gitDir):
    gitDir = os.path.join('C:'+os.sep,'Users','mhp12','git')

projDir = os.path.join(gitDir,'perry_mad_power_calc')

inputFile = os.path.join(projDir,'data','original','PembertonEtAl2013data-G3','pembertonEtAl2013.MS5795.stru')
outputFile = os.path.join(projDir,'pemberton_validation','pembertonEtAl2013.MS5795.arp')

#stru = stru_to_arp.Stru(inputFile)
stru_to_arp.stru_to_arp(inputFile,outputFile,title="PembertonEtAl2013data-G3-MS5795 for Perry Lab simulation")

#print(data[len(data)-1])
