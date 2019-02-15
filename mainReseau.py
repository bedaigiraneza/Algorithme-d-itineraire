# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:20:21 2019

@author: igiraneb
"""

from reseau import Reseau
from ligne import Ligne


def main():
    
    SIBRA = Reseau()
    
    SIBRA.addLine(Ligne("1_Poisy-ParcDesGlaisins.txt"))
#    SIBRA.addLine(Ligne("2_Piscine-Patinoire_Campus.txt"))
    #SIBRA.getListeLignes()[0].afficher()
    print(SIBRA.getListeLignes()[0].afficherDetailsLigne())

    

# Calls the main function
if __name__ == "__main__":
    main() 