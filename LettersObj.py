# from Model import Title

# class DrawObjects(Title):
    
#     def __init__(self, MATRIX_HEIGHT, MATRIX_WIDTH, MATRIX_FILLER, MATRIX_SIGN):
#         super().__init__(MATRIX_HEIGHT, MATRIX_WIDTH, MATRIX_FILLER, MATRIX_SIGN)
        
#     def LetterR(self):
#         matr = self.create_matrix()
#         CHANGED_SIGN = self.MATRIX_FILLER
#         matr_len = len(matr)
#         break_index1, break_index2 = 0, 0
#         break_ = False
#         timer = 0.05
        
#         for i in range(int(matr_len // 1.37)):            
            
#             for k in range(len(matr[i])):
#                 if break_index1 >= 8:
#                     break
                
#                 matr[1][k + 1] = CHANGED_SIGN
                            
#                 break_index1 = k
                
#                 self.prepare_window(timer, matr)
            
#             if i <= 7:
#                 matr[i + 1][break_index1 + 1] = CHANGED_SIGN
#                 break_index2 = i + 1
                
#                 self.prepare_window(timer, matr)
                
#             else:
#                 if not break_:
#                     for k in range(7):
#                         matr[break_index2][break_index1 - k] = CHANGED_SIGN
                        
#                         self.prepare_window(timer, matr)
                        
#                         break_ = True
                
#                 if i <= 15:
#                     matr[i + 1][1] = CHANGED_SIGN
#                 else: 
                        
#                     for k in range(9):
#                         matr[8 + k][k + 1] = CHANGED_SIGN
                        
#                         self.prepare_window(timer, matr)
                        
#                     for k in range(4):
#                         matr[1 + k][1 + k] = CHANGED_SIGN
                        
#                         self.prepare_window(timer, matr)

#                     for k in range(4):
#                         matr[4 + k][4 - k] = CHANGED_SIGN
                        
#                         self.prepare_window(timer, matr)
                
#                 self.prepare_window(timer, matr)

import curses, time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
    
def show_window(MATRIX_WIDTH, *kwargs):

    string = str()
    
    for i in kwargs:
        for k in i:
            for l in k:
                string += l
                

    count_start, count_end = 0, 26 
    
    for i in range(MATRIX_WIDTH):
        stdscr.addstr(i, 0, string[count_start:count_end])
        stdscr.refresh()
        
        count_start += 25
        count_end += 25

def prepare_window(timer, matr, MATRIX_WIDTH):
    show_window(MATRIX_WIDTH, matr)
    time.sleep(timer)

def LetterA(matr, CHANGED_SIGN, MATRIX_WIDTH):
    matr_len = len(matr)
    break_index1, break_index2 = 0, 0
    break_ = False
    timer = 0.05
    
    # for i in range(matr_len):
        

def LetterR(matr, CHANGED_SIGN, MATRIX_WIDTH, PADDING):
    matr_len = len(matr)
    break_index1, break_index2 = 0, 0
    break_ = False
    timer = 0.05
    
    for i in range(int(matr_len // 1.37)):            
        
        for k in range(len(matr[i])):
            if break_index1 >= 8:
                break
            
            matr[1][PADDING + k + 1] = CHANGED_SIGN
                        
            break_index1 = k
            
            prepare_window(timer, matr, MATRIX_WIDTH)
        
        if i <= 7:
            matr[i + 1][PADDING + break_index1 + 1] = CHANGED_SIGN
            break_index2 = i + 1
            
            prepare_window(timer, matr, MATRIX_WIDTH)
            
        else:
            if not break_:
                for k in range(7):
                    matr[break_index2][PADDING + break_index1 - k] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_WIDTH)
                    
                    break_ = True
            
            if i <= 15:
                matr[i + 1][PADDING + 1] = CHANGED_SIGN
            else: 
                    
                for k in range(9):
                    matr[8 + k][PADDING + k + 1] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_WIDTH)
                    
                for k in range(4):
                    matr[1 + k][PADDING + 1 + k] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_WIDTH)

                for k in range(4):
                    matr[4 + k][PADDING + 4 - k] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_WIDTH)
            
            prepare_window(timer, matr, MATRIX_WIDTH)