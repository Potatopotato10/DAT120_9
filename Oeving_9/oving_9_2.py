# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:17:14 2021

@author: Åsmund
"""

#sliste = []
#svaralternativ = []
#riktigsvarliste = []

class QA:
    def __init__(self, spørsmål, alternativ, riktigsvar):
        self.spørsmål = spørsmål
        self.alternativ = alternativ
        self.riktigsvar = riktigsvar
        
    def __str__(self):
        spørsmål = f"""{self.spørsmål}
        alt.1: {self.alternativ[0]}
        alt.2: {self.alternativ[1]}
        alt.3: {self.alternativ[2]}
        alt.4: {self.alternativ[3]}
        alt.5: {self.alternativ[4]}"""
        return '\n' + spørsmål
    
        
        
    #def sjekk_svar(self, svar_spiller1):
        #if str(self.riktigsvar[0]) == str(svar_spiller1):
            #print("Riktig spiller 1!")
        #else: 
            #print ("Desverre spiller 1, feil!")
            
    def sjekk_svar(self, svar_spiller1, svar_spiller2):
        if str(self.riktigsvar[0][1]) == str(svar_spiller1):
            print("Riktig spiller 1!")
        else: 
            print ("Desverre spiller 1, feil!")
        if str(self.riktigsvar[0][1]) == str(svar_spiller2):
            print("Riktig spiller 2!")
        else: 
            print ("Desverre spiller 2, feil!")

def filleser():
    #s_liste = []
    #svaralternativ_liste = []
    #riktigsvar_liste = []
    spm_liste = []
    with open ("sporsmaalsfil.txt", "r", encoding="utf-8") as fil:
        for line in fil:
            fields = line.split(':')
            s = fields[0]
            alternativ = fields[2].split(',')
            riktigsvar = fields[1].split(': ')
            spm_liste.append(QA(s, alternativ, riktigsvar))
        return spm_liste
            
            
if __name__ == "__main__":
    sporsmaal = filleser()
    
    for spm in sporsmaal:
        print('\n')
        print(str(spm))
        #print('\n')
        svar_spiller1 = int(input("Spiller1 avgi svar: "))
        svar_spiller2 = int(input("Spiller2 avgi svar: "))
        print('\n')
        spm.sjekk_svar(svar_spiller1, svar_spiller2)
        #spm.sjekk_svar(svar_spiller2)


        

