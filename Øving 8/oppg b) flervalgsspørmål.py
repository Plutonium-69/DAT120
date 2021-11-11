# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:43:25 2021

@author: ajeev
"""

class question:
    def __init__(self, question, answer, options):
         self.question = question
         self.answer = answer
         self.options = options
    
    def __str__(self):
        streng = self.question
        for index,options in enumerate(self.options) :
            streng +=f"\n {index+1} {options}"
        return streng
        
    def svar(self, input):
        if input == self.answer:
            return f"Svaret var riktig!"
        elif input > 4:
            return f"That is not a option!"
        else:
            return f"Svaret var feil. Riktig svar var alternativ {self.answer}"
        
    
if __name__ == "__main__":
    question1 = question('How many legs on a horse?',2,["One","Two","Three","Four"])
    print(question1)
    svar = int(input("Skriv inn ett av alternativene: "))
    print(question1.svar(svar))
    
    question2 = question('\nWhat color is a australian swan?',2,["White","Black","Pink","Grey"])
    print(question2)
    svar = int(input("Skriv inn ett av alternativene: "))
    print(question2.svar(svar))
    
    
        
        

