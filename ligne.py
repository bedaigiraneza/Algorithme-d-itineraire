# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:02:41 2019

@author: igiraneb
"""
from arret import Arret

class Ligne:
    
    # ================================================
    def __init__(self, nomDuFichier):        
        self.bus = int(nomDuFichier[0])
        self.listeArrets = []
        self.listeHoraires = []
        
        # -- Parcours du fichier
        fichier = open(nomDuFichier, "r")
        ligneDuFichier = []
        for l in fichier:
            ligneDuFichier.append(l)
        fichier.close()
        
        #-- On remplit la liste des arrets
        self.remplirListeArret(ligneDuFichier[0])
        
        #-- On remplit la liste des horaires
        self.remplirListeHoraires(ligneDuFichier)
        
    # ================================================
    def getListeArrets(self):
        return self.listeArrets
    
    # ================================================
    def getListeHoraires(self):
        return self.listeHoraires
    
    # ================================================
    def setBus(self, numeroBus):
        self.bus = numeroBus
        
    # ================================================
    def afficherDetailsLigne(self):
        for i in range(len(self.listeArrets)):
            print(self.listeArrets[i].getName()," : ")
            print(self.listeHoraires[i], "\n")
 
    # ================================================       
    def afficherListeArrets(self):
        for l in self.listeArrets:
            print(l.getName(), " ")
        print("\n")
    
# ================================================       
# ================================================       
#    LES HORAIRES CLASSIQUE
# ================================================       
# ================================================       

    
    def remplirListeArret(self, list):
        tmp = []
        i = 0
        while i < len(list):
            if list[i] != ' ' and list[i] != '\n':
                tmp.append(list[i])
            else:
                stopName = ''.join(tmp) 
                # -- On cree l'arret correspondant au nom "stopName"
                arret = Arret(stopName)
                # -- On ajoute l'objet "arret" a notre liste
                self.listeArrets.append(arret)                
                #self.listeArrets.append(Arret(stopName))
                tmp = []
                i += 2
            # -- End if
            i += 1
        # -- End While
    
    # ================================================
    def remplirListeHoraires(self, liste):
        indice = 0 # -- poisition dans la liste des arrets
        numLigne = 2 # -- Position dans le fichier
        tmp = [] # -- Va recuperer l'horaire (hh:mm) de passage
        timeList = [] # -- liste de tous les horaires pour chaque bus
        while indice < len(self.listeArrets):
            arret = liste[numLigne + indice]
            
            # on se position apres le nom de l'arret
            i = len(self.listeArrets[indice].getName()) 
            
            while i < len(arret):
                if arret[i] != ' ' and arret[i] != '-' and arret[i] != '\n':
                    tmp.append(arret[i])
                else:
                    if (len(tmp) != 0):
                        heureMinute = ''.join(tmp)
                        timeList.append(heureMinute)
                        tmp = []
                i += 1 
            # -- End while
            
            # -- On remplir la liste des horaires
            self.listeHoraires.append(timeList)
            timeList = []
            indice +=1
        # -- End while
        
        # -------------------------- On recupere les horaires dans le sens invrese
        indice -= 1
        nTmp = 2
        while indice >= 0:
            arret = liste[numLigne + nTmp] # -- Ligne du fichier qui correspond a l'arret
            
            # on se position apres le nom de l'arret
            i = len(self.listeArrets[indice].getName()) 
            
            while i < len(arret):
                if arret[i] != ' ' and arret[i] != '-' and arret[i] != '\n':
                    tmp.append(arret[i])
                else:
                    if (len(tmp) != 0):
                        heureMinute = ''.join(tmp)
                        timeList.append(heureMinute)
                        tmp = []
                i += 1 
            # -- End while
            
            # -- On remplir la liste des horaires
            self.listeHoraires.append(timeList)
            timeList = []
            indice -= 1
            nTmp += 1 
        # -- End while
            
# ================================================       
# ================================================       
#    LES HORAIRES CLASSIQUE
# ================================================       
# ================================================       