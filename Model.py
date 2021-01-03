from LettersObj import *
import time, threading

class Letter():
    
    def __init__(self, FILLER, NAME):
        
        self.FILLER = FILLER
        self.NAME = NAME
        
    __letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    def IsExist(self):
        
        self.NAME = self.NAME.upper()
        
        return (self.NAME in self.__letters)
        
class Title():
    
    def __init__(self, LEGEND, MATRIX_HEIGHT, MATRIX_WIDTH,  MATRIX_FILLER, MATRIX_SIGN, CONSECUTIVE : True):
        
        self.LEGEND = LEGEND
        self.MATRIX_HEIGHT = MATRIX_HEIGHT
        self.MATRIX_WIDTH = MATRIX_WIDTH 
        self.MATRIX_FILLER = MATRIX_FILLER
        self.MATRIX_SIGN = MATRIX_SIGN
        self.ForQueue = CONSECUTIVE
    
    def create_matrix(self):
        matr = [[self.MATRIX_SIGN for i in range(self.MATRIX_WIDTH)] for i in range(self.MATRIX_HEIGHT)]
        
        return matr
       
    def handler(self):
        
        __letters_obj = list()  
        
        for i in self.LEGEND:
            
            Letter_obj = Letter(self.MATRIX_FILLER, i)
            
            if Letter_obj.IsExist():
                __letters_obj.append(Letter_obj)
                
        return __letters_obj
          
    def Threader(self, count, func, Letter_args):

        __letters_obj = self.handler()
        
        if count == len(__letters_obj) - 1:
            func(Letter_args[0], Letter_args[1], count * 10, False, True)
            
            if self.ForQueue:
                time.sleep(1.5)

        elif self.ForQueue:
            func(Letter_args[0], Letter_args[1], count * 10, False, False)
        else:
            thr = threading.Thread(target = func, args = (Letter_args[0], Letter_args[1], count * 10, False, False), daemon = True)
            thr.start() 
                    
    def Draw(self):
        letter_object = LetterSwitcher(self.MATRIX_HEIGHT, self.MATRIX_WIDTH)
        
        count = 0
        __letters_obj = self.handler()
        Letter_args = (self.create_matrix(), self.MATRIX_FILLER)
        
        for unit in __letters_obj:
            try: 
                self.Threader(count, letter_object.select(unit.NAME), Letter_args)
                    
                count += 1
                
            finally:
                curses.echo()
                curses.nocbreak()
                curses.endwin()     