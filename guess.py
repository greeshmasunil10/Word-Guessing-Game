'''
Created on May 19, 2019

@author: Greeshma
'''
from msvcrt import getch


class guess(object):
    
    def __init__(self):
        self.gameobjects=[]
        
    def _newgame(self):
        self.gobj= game()
        base=stringDatabase()
        base._readwords()
        self.gameword= base._loadword()
        self.gobj._setword(self.gameword)
        print('')
        self.found='----'
        print ("** The great guessing game **")
        print('Current Guess: ----')
        self._greet()
        
        
    def _greet(self):
        print('')
        print ('g = guess, t = tell me, l for a letter, and q to quit')
        self.inp = input()
        if self.inp == 'g':
            word= input('Enter the guessed word:')
            if word==self.gameword:
                print("You guessed the word!")
                self.gobj._setstatus("Success")
                self._storegame()
            else :
                self.gobj._incbadguess() 
                self._greet()   
              
        if self.inp == 't':
            print('The word was:',self.gameword)
            self.gobj._setstatus("Gave Up")
            self._storegame()
            
        if self.inp == 'l':
            print('Enter a letter:')
            self.letter=input()
            self._guessletter()
            
        if self.inp == 'q':    
            print('')
            print("Game over")
            self.gameobjects.append(self.gobj)
#             self.gameobjects= self.gameobjects+ self.gobj
            self._results()
            
            
        else:
            self._greet()
            
            
    def _guessletter(self):
        tempword=self.gameword
        if(self.letter  in self.gameword) :
            count=0
            while self.letter  in tempword:
                index=tempword.find(self.letter)
                self.found = self.found[:index]+self.letter+self.found[index+1:]
                tempword=tempword[:index]+'*'+tempword[index+1:]
                count=count+1
            print("You found",count,"letters")    
            print("Current guess:",self.found)
            if '-' not in self.found:
                print("You have guessed the word!")
                self.gobj._setstatus("Success")
                self._storegame()
        else :
            print('Wrong guess')   
            self.gobj._incmissed()
        
        self._greet()   
        
    def _storegame(self):
            input('Press any key for new game')
            self.gameobjects.append(self.gobj)
#             self.gameobjects= self.gameobjects+ self.gobj
            for x in self.gameobjects :
                print('gameobj',x.word)
            self._newgame()
      
    def _results(self):
#         print("size:",len(self.gameobjects))
        print('%-12s%-12s%-12s%-12s%-12s%-12s' %('Game', 'Word','Status','Bad Guesses','Missed Letters','Score') )
        count=1
        for x in self.gameobjects:
            print('%-12s%-12s%-12s%-12s%-12s%-12s' % (count,x._retword(),x._retstatus(),x._retbadguess(),x._retmissed(),x._retscore()) )
            count= count+1 
                
            
class stringDatabase(object):
    def _readwords(self):
        file= open("four_letters.txt","r")
        self.wordlist=[]
        import re
        for line in file:
            word=re.split('\\s|\n|,',line) 
            self.wordlist+= word
        
        for x in self.wordlist:
            if len(x)==0:
                self.wordlist.remove(x)
        #`print(self.wordlist)  
        self.no_of_words= len(self.wordlist)       
       
    def _loadword(self):
        import random
        self.ourword=self.wordlist[random.randint(0,self.no_of_words)]
        print(self.ourword)
        return self.ourword
        
class game(object):
    def __init__(self):
        self.badguess=0
        self.missed=0
        self.score=0
        self.word=""
        self.gamestatus='Gave Up'

    def _setword(self,par):
        self.word=par
    def  _retword(self):
        return self.word 
     
    def _setstatus(self,par):
        self.gamestatus=par
    def _retstatus(self):
        return self.gamestatus
    
    def _incbadguess(self):
        self.badguess= self.badguess+1
    def _retbadguess(self):
        return self.badguess
    
    def _incmissed(self):
        self.missed = self.missed+1
    def _retmissed(self):
        return self.missed
    
    def _setscore(self,par):
        self.score=par
    def _retscore(self):
        return self.score       
    
            

                                  
menu= guess()    
menu._newgame()