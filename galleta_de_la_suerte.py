# -*- coding: utf-8 -*-
import pyttsx3
import random

class galleta:

    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-10)
        volume = self.engine.getProperty('volume')
        self.engine.setProperty('volume', volume+0.50)
        self.set_frases_num = list()
        self.loadPhrases()
        return

    def loadNums(self, size):
        set_num = list()
        while len(set_num) != size:
            num = random.randint(0,size-1)
            if num not in set_num:
                set_num.append(num)

        return set_num
    
    def reproducePhrase(self, name):
        if len(self.set_frases_num) == 0:
            self.set_frases_num = self.loadNums(len(self.frases))

        numero = self.set_frases_num.pop()
        self.engine.say(name+','+self.frases[numero-1])
        self.engine.runAndWait()
        return
        
    def loadPhrases(self):
        file = open('frases.txt','r')
        self.frases = file.readlines()
        file.close()
            
if __name__ == '__main__':
    galleta = galleta()
    galleta.reproducePhrase('Usuario')