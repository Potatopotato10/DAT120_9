# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 18:17:14 2021

@author: Åsmund
"""
#antall_riktige_svar1 = 0
#antall_riktige_svar2 = 0

class QA:
    def __init__(self, spørsmål, alternativ, riktigsvar):
        self.spørsmål = spørsmål
        self.alternativ = alternativ
        self.riktigsvar = riktigsvar
        
    def __str__(self):
        spørsmål=f"{self.spørsmål} \n"
        for alt in range(len(self.alternativ)):
                spørsmål +=f"{alt}.{self.alternativ[alt]}\n"
        return '\n' + spørsmål
    
            
    def sjekk_svar(self, svar_spiller1, svar_spiller2):
        if str(self.riktigsvar[0][1]) == str(svar_spiller1):
            print("Riktig spiller 1!")
        else: 
            print ("Desverre spiller 1, feil!") 
        if str(self.riktigsvar[0][1]) == str(svar_spiller2):
            print("Riktig spiller 2!")
        else: 
            print ("Desverre spiller 2, feil!")
        print("Riktig svar er: " + self.riktigsvar[0][1])
        return(str(self.riktigsvar[0][1]) == str(svar_spiller1),str(self.riktigsvar[0][1]) == str(svar_spiller2))
              

def filleser():
    spm_liste = []
    with open ("sporsmaalsfil.txt", "r", encoding="utf-8") as fil:
        for line in fil:
            fields = line.split(':')
            s = fields[0]
            alternativ = fields[2].strip("[] \n").split(",")
            riktigsvar = fields[1].split(': ')
            spm_liste.append(QA(s, alternativ, riktigsvar))
        return spm_liste
            
            
if __name__ == "__main__":
    sporsmaal = filleser()
    antall_riktige_svar1 = 0
    antall_riktige_svar2 = 0
    for spm in sporsmaal:
        print('\n')
        print(str(spm))
        svar_spiller1 = int(input("Spiller1 avgi svar: "))
        svar_spiller2 = int(input("Spiller2 avgi svar: "))
        print('\n')
        (p1r, p2r) = spm.sjekk_svar(svar_spiller1, svar_spiller2)
        if p1r:    
            antall_riktige_svar1 += 1
        if p2r:
            antall_riktige_svar2 += 1
        print(f"stillingen til nå er: \n Spiller 1: {antall_riktige_svar1} \n Spiller 2: {antall_riktige_svar2}")
        
        
        


        

