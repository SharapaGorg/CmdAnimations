from LettersObj import *
import curses, time, threading

class Letter():
    
    def __init__(self, FILLER, NAME):
        
        self.FILLER = FILLER
        self.NAME = NAME
        
    __letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    def IsExist(self):
        
        self.NAME = self.NAME.upper()
        
        if self.NAME in self.__letters:
            return True
        else:
            return False
        
class Title():
    
    def __init__(self, LEGEND, MATRIX_HEIGHT, MATRIX_WIDTH,  MATRIX_FILLER, MATRIX_SIGN, CONSECUTIVE : True):
        
        self.LEGEND = LEGEND
        self.MATRIX_HEIGHT = MATRIX_HEIGHT
        self.MATRIX_WIDTH = MATRIX_WIDTH 
        self.MATRIX_FILLER = MATRIX_FILLER
        self.MATRIX_SIGN = MATRIX_SIGN
        self.ForQueue = CONSECUTIVE
    
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    
    def create_matrix(self):
        matr = [[self.MATRIX_SIGN for i in range(self.MATRIX_WIDTH)] for i in range(self.MATRIX_HEIGHT)]
        
        return matr
    
    def show_window(self, *kwargs):
    
        string = str()
        
        for i in kwargs:
            for k in i:
                for l in k:
                    string += l
                    

        count_start, count_end = 0, 26 
        
        for i in range(self.MATRIX_WIDTH):
            self.stdscr.instr(i, 0, string[count_start:count_end])
            self.stdscr.refresh()
            
            count_start += 25           
            count_end += 25
            
    def prepare_window(self, timer : 0.05, new_matr : list):
        
        self.show_window(new_matr)
        time.sleep(timer)
       
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
            func(Letter_args[0], Letter_args[1], Letter_args[2], Letter_args[3], count * 10, True)
            
            if self.ForQueue:
                time.sleep(1.5)
            
        if self.ForQueue:
            func(Letter_args[0], Letter_args[1], Letter_args[2], Letter_args[3], count * 10, False)
        else:
            thr = threading.Thread(target = func, args = (Letter_args[0], Letter_args[1], Letter_args[2], Letter_args[3], count * 10, False), daemon = True)
            thr.start() 
                    
    def Draw(self):
        from LettersObj import LetterR, LetterA
        
        count = 0
        __letters_obj = self.handler()
        Letter_args = (self.create_matrix(), self.MATRIX_FILLER, self.MATRIX_HEIGHT, self.MATRIX_WIDTH)
        
        for unit in __letters_obj:
            try: 
                if unit.NAME == "R":
                    self.Threader(count, LetterR, Letter_args)
            
                if unit.NAME == "D":
                    self.Threader(count, LetterD, Letter_args)
                        
                if unit.NAME == "O":
                    self.Threader(count, LetterO, Letter_args)      
                        
                if unit.NAME == "L":                 
                    self.Threader(count, LetterL, Letter_args)  
                    
                if unit.NAME == "Y":
                    self.Threader(count, LetterY, Letter_args)
                
                if unit.NAME == "A":
                    self.Threader(count, LetterA, Letter_args)
                
                if unit.NAME == "N":
                    self.Threader(count, LetterN, Letter_args)
                    
                count += 1
                
            finally:
                curses.echo()
                curses.nocbreak()
                curses.endwin()     