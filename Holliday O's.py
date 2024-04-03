# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:24:57 2024

@author: benja
"""

import numpy as np

HollidaySkill=2.5
LangfordSkill=2.5
CarterSkill=2.5
KeithSkill=1.8
RaffaelaSkill=1.8

HollidayPT=600
LangfordPT=600
CarterPT=600
KeithPT=600
RaffaelaPT=600

HollidayROY=0
HollidaySecond=0
HollidayWARTot=0
HBad=0


for i in range(1000000):
    HollidayWAR=(HollidaySkill+2*np.random.normal())*HollidayPT/600
    LangfordWAR=(LangfordSkill+2*np.random.normal())*LangfordPT/600
    CarterWAR=(LangfordSkill+2*np.random.normal())*CarterPT/600
    KeithWAR=(KeithSkill+2*np.random.normal())*KeithPT/600
    RaffaelaWAR=(RaffaelaSkill+2*np.random.normal())*RaffaelaPT/600
    
    WARGrid=np.array([HollidayWAR,LangfordWAR,CarterWAR,KeithWAR,RaffaelaWAR])
    highest=np.max(WARGrid)
    second_highest=np.partition(WARGrid,1)[1]
   
    if HollidayWAR==highest:
        HollidayROY+=1
    elif HollidayWAR==second_highest:
        HollidaySecond+=1
    HollidayWARTot+=HollidayWAR
    if HollidayWAR<=1.5:
        HBad+=1
      
ROYRatio=round(HollidayROY/1000000,2)
SecondRatio=round(HollidaySecond/1000000,2)
TotalAwards=round(ROYRatio+SecondRatio,2)

print("Holliday Win Odds are "+str(ROYRatio))
print("Holliday Second Odds are "+str(SecondRatio))
print("Total Top 2s are "+str(TotalAwards))
print("Holliday WAR is "+str(round(HollidayWARTot/1000000,2)))
