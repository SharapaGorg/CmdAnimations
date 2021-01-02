import curses, time

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
    
def show_window(MATRIX_HEIGHT, MATRIX_WIDTH, *kwargs):

    string = str()
    
    for i in kwargs:
        for k in i:
            for l in k:
                string += l
                

    count_start, count_end = 0, MATRIX_WIDTH + 1 
    
    for i in range(MATRIX_HEIGHT):
        stdscr.addstr(i, 0, string[count_start:count_end]) # addition variant - insstr - addstr
        stdscr.refresh()
        
        count_start += MATRIX_WIDTH
        count_end += MATRIX_WIDTH

def prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH):
    show_window(MATRIX_HEIGHT, MATRIX_WIDTH, matr)
    time.sleep(timer)

def LetterA(matr, CHANGED_SIGN, MATRIX_HEIGHT, MATRIX_WIDTH, PADDING, QUEUE : bool):
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
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)

            if k <= 8:
                matr[1][PADDING + 1 + k] = CHANGED_SIGN
                matr[8][PADDING + 1 + k] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
         
        if QUEUE:        
            time.sleep(5)
            
        break
    
def LetterD(matr, CHANGED_SIGN, MATRIX_HEIGHT, MATRIX_WIDTH, PADDING, QUEUE : bool):
    
    if not QUEUE:
        timer = 0.05
    else:
        timer = 0.005
    
    for i in range(len(matr)):
        for k in range(len(matr[i])):
            if k <= 15:
                matr[1 + k][PADDING + 1] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
                
        for k in range(len(matr[i])):
            if k <= 4:
                matr[1][PADDING + 1 + k] = CHANGED_SIGN
                matr[16][PADDING + 1 + k] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
                
        for k in range(len(matr[i])):
            if k <= 3:
                matr[2 + k][PADDING + 6 + k] = CHANGED_SIGN
                matr[15 - k][PADDING + 6 + k] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
        
        for k in range(len(matr[i])):
            if k <= 3:
                matr[5 + k][PADDING + 9] = CHANGED_SIGN
                matr[11 - k][PADDING + 9] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
        
        if QUEUE:    
            time.sleep(5)
            
        break
    
def LetterO(matr, CHANGED_SIGN, MATRIX_HEIGHT, MATRIX_WIDTH, PADDING, QUEUE : bool):

    if not QUEUE:
        timer = 0.05
    else:
        timer = 0.005

    for i in range(len(matr)):
        for k in range(len(matr[i])):
            if k <= 15:
                matr[1 + k][PADDING + 1] = CHANGED_SIGN
                matr[16 - k][PADDING + 10] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
        
        for k in range(len(matr[i])):
            if k <= 9:
                matr[1][PADDING + 1 + k] = CHANGED_SIGN
                matr[16][PADDING + 10 - k] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
         
        if QUEUE:        
            time.sleep(3)
            
        break
    
def LetterL(matr, CHANGED_SIGN, MATRIX_HEIGHT, MATRIX_WIDTH, PADDING, QUEUE : bool):
   
    if not QUEUE:
        timer = 0.05
    else:
        timer = 0.005
    
    for i in range(len(matr)):
        for k in range(len(matr[i])):
            if k <= 15:
                matr[1 + k][PADDING + 2] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
            
        for k in range(len(matr[i])):
            if k <= 9:
                matr[16][PADDING + 2 + k] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
                
        if QUEUE:        
            time.sleep(2.5)
            
        break

def LetterY(matr, CHANGED_SIGN, MATRIX_HEIGHT, MATRIX_WIDTH, PADDING, QUEUE : bool):
    
    if not QUEUE:
        timer = 0.05
    else:
        timer = 0.005
    
    for i in range(len(matr)):
        for k in range(len(matr[i])):
            if k <= 15:
                matr[16 - k][PADDING + 5] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
                
        for k in range(len(matr[i])):
            if k <= 4:
                matr[5 - k][PADDING + 5 + k] = CHANGED_SIGN
                matr[5 - k][PADDING + 5 -k] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
                
        if QUEUE:
            time.sleep(4)

        break
    
def LetterN(matr, CHANGED_SIGN, MATRIX_HEIGHT, MATRIX_WIDTH, PADDING, QUEUE : bool):
    
    if not QUEUE:
        timer = 0.05
    else:
        timer = 0.005
    
    for i in range(len(matr)):
        for k in range(len(matr[i])):
            if k <= 15:
                matr[1 + k][PADDING + 1] = CHANGED_SIGN
                matr[16 - k][PADDING + 9] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
        
        for k in range(len(matr[i])):
            if k <= 7:
                matr[4 + k][PADDING + 1 + k] = CHANGED_SIGN
                
                prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
        
        if QUEUE:
            time.sleep(3)
            
        break

def LetterR(matr, CHANGED_SIGN, MATRIX_HEIGHT, MATRIX_WIDTH, PADDING, QUEUE : bool):
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
            
            prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
        
        if i <= 7:
            matr[i + 1][PADDING + break_index1 + 1] = CHANGED_SIGN
            break_index2 = i + 1 
            
            prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
            
        else:
            if not break_:
                for k in range(7):
                    matr[break_index2][PADDING + break_index1 - k] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
                    
                    break_ = True
            
            if i <= 15:
                matr[i + 1][PADDING + 1] = CHANGED_SIGN
            else: 
                    
                for k in range(9):
                    matr[8 + k][PADDING + k + 1] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
                    
                for k in range(4):
                    matr[1 + k][PADDING + 1 + k] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)

                for k in range(4):
                    matr[4 + k][PADDING + 4 - k] = CHANGED_SIGN
                    
                    prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)
            
            prepare_window(timer, matr, MATRIX_HEIGHT, MATRIX_WIDTH)