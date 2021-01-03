import curses, time

class LetterSwitcher():

    def __init__(self, MATRIX_HEIGHT, MATRIX_WIDTH):

        self.MATRIX_HEIGHT = MATRIX_HEIGHT
        self.MATRIX_WIDTH = MATRIX_WIDTH

    def select(self, letter_):
        method_name = "Letter" + letter_
        method = getattr(self, method_name)

        return method

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    
    def show_window(self, *kwargs):

        string = str()
        
        for i in kwargs:
            for k in i:
                for l in k:
                    string += l
                    

        count_start, count_end = 0, self.MATRIX_WIDTH + 1 
        
        for i in range(self.MATRIX_HEIGHT):
            self.stdscr.addstr(i, 0, string[count_start:count_end]) # additional variant - insstr - addstr
            self.stdscr.refresh()
            
            count_start += self.MATRIX_WIDTH
            count_end += self.MATRIX_WIDTH

    def prepare_window(self, timer, matr):
        self.show_window(matr)
        time.sleep(timer)

    def LetterA(self, matr : list, CHANGED_SIGN : str, PADDING : int, QUEUE : bool, LAST : bool):
        matr_len = len(matr)
        
        if QUEUE:
            timer = 0.005
        else:
            timer = 0.05
        
        for i in range(matr_len):
            for k in range(len(matr[i])):
                
                if k <= 15:
                    matr[1 + k][PADDING + 1] = CHANGED_SIGN
                    matr[1 + k][PADDING + 9] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)

                if k <= 8:
                    matr[1][PADDING + 1 + k] = CHANGED_SIGN
                    matr[8][PADDING + 1 + k] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
            
            if QUEUE or LAST:     
                time.sleep(5)
                
            break
        
    def LetterD(self, matr : list, CHANGED_SIGN : str, PADDING : int, QUEUE : bool, LAST : bool):
        
        if not QUEUE:
            timer = 0.05
        else:
            timer = 0.005
        
        for i in range(len(matr)):
            for k in range(len(matr[i])):
                if k <= 15:
                    matr[1 + k][PADDING + 1] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
                    
            for k in range(len(matr[i])):
                if k <= 4:
                    matr[1][PADDING + 1 + k] = CHANGED_SIGN
                    matr[16][PADDING + 1 + k] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
                    
            for k in range(len(matr[i])):
                if k <= 3:
                    matr[2 + k][PADDING + 6 + k] = CHANGED_SIGN
                    matr[15 - k][PADDING + 6 + k] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
            
            for k in range(len(matr[i])):
                if k <= 3:
                    matr[5 + k][PADDING + 9] = CHANGED_SIGN
                    matr[11 - k][PADDING + 9] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
            
            if QUEUE or LAST:   
                time.sleep(5)
                
            break
        
    def LetterO(self, matr : list, CHANGED_SIGN : str, PADDING : int, QUEUE : bool, LAST : bool):

        if not QUEUE:
            timer = 0.05
        else:
            timer = 0.005

        for i in range(len(matr)):
            for k in range(len(matr[i])):
                if k <= 15:
                    matr[1 + k][PADDING + 1] = CHANGED_SIGN
                    matr[16 - k][PADDING + 10] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
            
            for k in range(len(matr[i])):
                if k <= 9:
                    matr[1][PADDING + 1 + k] = CHANGED_SIGN
                    matr[16][PADDING + 10 - k] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
            
            if QUEUE or LAST:        
                time.sleep(3)
                
            break
        
    def LetterL(self, matr : list, CHANGED_SIGN : str, PADDING : int, QUEUE : bool, LAST : bool):
    
        if not QUEUE:
            timer = 0.05
        else:
            timer = 0.005
        
        for i in range(len(matr)):
            for k in range(len(matr[i])):
                if k <= 15:
                    matr[1 + k][PADDING + 2] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
                
            for k in range(len(matr[i])):
                if k <= 9:
                    matr[16][PADDING + 2 + k] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
                    
            if QUEUE or LAST:        
                time.sleep(2.5)
                
            break

    def LetterY(self, matr : list, CHANGED_SIGN : str, PADDING : int, QUEUE : bool, LAST : bool):
        
        if not QUEUE:
            timer = 0.05
        else:
            timer = 0.005
        
        for i in range(len(matr)):
            for k in range(len(matr[i])):
                if k <= 15:
                    matr[16 - k][PADDING + 5] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
                    
            for k in range(len(matr[i])):
                if k <= 4:
                    matr[5 - k][PADDING + 5 + k] = CHANGED_SIGN
                    matr[5 - k][PADDING + 5 -k] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
                    
            if QUEUE or LAST:
                time.sleep(4)

            break
        
    def LetterN(self, matr : list, CHANGED_SIGN : str, PADDING : int, QUEUE : bool, LAST : bool):
        
        if not QUEUE:
            timer = 0.05
        else:
            timer = 0.005
        
        for i in range(len(matr)):
            for k in range(len(matr[i])):
                if k <= 15:
                    matr[1 + k][PADDING + 1] = CHANGED_SIGN
                    matr[16 - k][PADDING + 9] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
            
            for k in range(len(matr[i])):
                if k <= 7:
                    matr[4 + k][PADDING + 1 + k] = CHANGED_SIGN
                    
                    self.prepare_window(timer, matr)
            
            if QUEUE or LAST:
                time.sleep(3)
                
            break

    def LetterR(self, matr : list, CHANGED_SIGN : str, PADDING : int, QUEUE : bool, LAST : bool):
        matr_len = len(matr)
        break_index1, break_index2 = 0, 0
        break_ = False
        
        if not QUEUE:
            timer = 0.05
        else:
            timer = 0.005
        
        for i in range(int(matr_len // 1.37)):            
            
            for k in range(len(matr[i])):
                if break_index1 >= 8:
                    break
                
                matr[1][PADDING + k + 1] = CHANGED_SIGN
                            
                break_index1 = k
                
                self.prepare_window(timer, matr)
            
            if i <= 7:
                matr[i + 1][PADDING + break_index1 + 1] = CHANGED_SIGN
                break_index2 = i + 1 
                
                self.prepare_window(timer, matr)
                
            else:
                if not break_:
                    for k in range(7):
                        matr[break_index2][PADDING + break_index1 - k] = CHANGED_SIGN
                        
                        self.prepare_window(timer, matr)
                        
                        break_ = True
                
                if i <= 15:
                    matr[i + 1][PADDING + 1] = CHANGED_SIGN
                else: 
                        
                    for k in range(9):
                        matr[8 + k][PADDING + k + 1] = CHANGED_SIGN
                        
                        self.prepare_window(timer, matr)
                        
                    for k in range(4):
                        matr[1 + k][PADDING + 1 + k] = CHANGED_SIGN
                        
                        self.prepare_window(timer, matr)

                    for k in range(4):
                        matr[4 + k][PADDING + 4 - k] = CHANGED_SIGN
                        
                        self.prepare_window(timer, matr)
                
                self.prepare_window(timer, matr)