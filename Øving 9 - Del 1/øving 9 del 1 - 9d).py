# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 16:30:48 2021

@author: ajeev
"""
options = []
with open("øving_9_text.txt", "r", encoding="UTF8") as fila:
    for linje in fila:
        tekst = linje.replace(',',':').replace("[", "").replace("]", "").split(":")
#        print(tekst)
        questions = tekst[0]
        lengde = len(tekst)
        answer = tekst[1]
        for i in range(2, lengde):
            options.append(tekst[i])


    
