import time, sys, curses
from Model import Title

DEFAULT_SIGN = "."
CHANGED_SIGN = "#"
SIZE = 25
CENTER = SIZE // 2

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

def ShowWindow(*kwargs):
    
    string = str()
    
    for i in kwargs:
        for k in i:
            for l in k:
                string += l
                

    count_start, count_end = 0, 26 
    
    for i in range(SIZE):
        stdscr.addstr(i, 0, string[count_start:count_end])
        stdscr.refresh()
        
        count_start += 25
        count_end += 25
   
def DropWindow():
    for i in range(len(matr)):
        for k in range(len(matr[i])):
            matr[i][k] = DEFAULT_SIGN
            
def PrepareWindow(timer : float, new_matr : list):
    
    ShowWindow(new_matr)
    time.sleep(timer)
    
matr = [[DEFAULT_SIGN for i in range(SIZE)] for i in range(SIZE)]

ShowWindow()

def Cross():
    for i in range(len(matr)):
        matr[i][i] = CHANGED_SIGN
        matr[i][len(matr[i]) - 1 - i] = CHANGED_SIGN

        PrepareWindow(0.5, matr)
        
def Arrow():
    while True:
        for k in range(len(matr)):
            
            matr[1][k] = CHANGED_SIGN
            matr[1][0] = DEFAULT_SIGN
            matr[1][len(matr) - 1] = DEFAULT_SIGN
            
            matr[-k][len(matr) - 2] = CHANGED_SIGN
            matr[1][len(matr) - 1] = DEFAULT_SIGN
            matr[len(matr) - 1][len(matr) - 2] = DEFAULT_SIGN
            matr[0][len(matr) - 2] = DEFAULT_SIGN
            
            matr[len(matr) - 1 - k][k] = CHANGED_SIGN
            matr[0][len(matr) - 1] = DEFAULT_SIGN
                        
            PrepareWindow()
            
            if k == len(matr) - 1:
                DropWindow()
            
def Square(size : int):
    while True:
        for i in range(size // 2 + 1):
            
            """ TOP """
            try :
                for k in range(i + 1):  
                    matr[CENTER - i][CENTER + i - k] = CHANGED_SIGN 
                    matr[CENTER - i][CENTER - i + k] = CHANGED_SIGN
            except: pass
                    
            """ BOTTOM """
            try :
                for k in range(i + 1):
                    matr[CENTER + i][CENTER + i - k] = CHANGED_SIGN
                    matr[CENTER + i][CENTER - i + k] = CHANGED_SIGN
            except : pass
            
            """ LEFT """
            try : 
                for k in range(i + i):
                    matr[CENTER + i - k][CENTER - i] = CHANGED_SIGN
            except : pass
            
            """ RIGHT """
            try : 
                for k in range(i + 1):
                    matr[CENTER - i + k][CENTER + i] = CHANGED_SIGN # right top
                    matr[CENTER + i - k][CENTER + i] = CHANGED_SIGN # right bottom
            except: pass
            
            if i == size // 2:
                DropWindow()
                
            PrepareWindow(0.1, matr)
            
def Radolyn():
    
    matr_len = len(matr)
    break_index1, break_index2 = 0, 0
    break_ = False
    timer = 0.05
    
    try:
        for i in range(int(matr_len // 1.37)):            
            
            for k in range(len(matr[i])):
                if break_index1 >= 8:
                    break
                
                matr[1][k + 1] = CHANGED_SIGN
                            
                break_index1 = k
                
                PrepareWindow(timer, matr)
            
            if i <= 7:
                matr[i + 1][break_index1 + 1] = CHANGED_SIGN
                break_index2 = i + 1
                
                PrepareWindow(timer, matr)
                
            else:
                if not break_:
                    for k in range(7):
                        matr[break_index2][break_index1 - k] = CHANGED_SIGN
                        
                        PrepareWindow(timer, matr)
                        
                        break_ = True
                
                if i <= 15:
                    matr[i + 1][1] = CHANGED_SIGN
                else: 
                        
                    for k in range(9):
                        matr[8 + k][k + 1] = CHANGED_SIGN
                        
                        PrepareWindow(timer, matr)
                        
                    for k in range(4):
                        matr[1 + k][1 + k] = CHANGED_SIGN
                        
                        PrepareWindow(timer, matr)

                    for k in range(4):
                        matr[4 + k][4 - k] = CHANGED_SIGN
                        
                        PrepareWindow(timer, matr)
                
                PrepareWindow(timer, matr)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()

# Radolyn()

Radolyn = Title("R", 20, 25, "#", ".")

Radolyn.Draw()