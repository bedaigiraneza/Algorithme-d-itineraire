# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:12:43 2019

@author: igiraneb
"""

class Reseau:
    
    def __init__(self):
        self.listeLignes = []
    
    # ================================================    
    def addLine(self, ligne):
        self.listeLignes.append(ligne)
    
    # ================================================
    def getListeLignes(self):
        return self.listeLignes