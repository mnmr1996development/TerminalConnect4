
#done in python 3.6.0

board = [['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ['-','-','-','-','-','-','-'],
         ]


#prints the board
def show():
    print ("0 | 1 | 2 | 3 | 4 | 5 | 6 |")
    print (board[5][0],'|',board[5][1],'|',board[5][2],'|',board[5][3],'|',board[5][4],'|',board[5][5],'|',board[5][6],'|')
    print ('---------------------------')
    print (board[4][0],'|',board[4][1],'|',board[4][2],'|',board[4][3],'|',board[4][4],'|',board[4][5],'|',board[4][6],'|')
    print ('---------------------------')
    print (board[3][0],'|',board[3][1],'|',board[3][2],'|',board[3][3],'|',board[3][4],'|',board[3][5],'|',board[3][6],'|')
    print ('---------------------------')
    print (board[2][0],'|',board[2][1],'|',board[2][2],'|',board[2][3],'|',board[2][4],'|',board[2][5],'|',board[2][6],'|')
    print ('---------------------------')
    print (board[1][0],'|',board[1][1],'|',board[1][2],'|',board[1][3],'|',board[1][4],'|',board[1][5],'|',board[1][6],'|')
    print ('---------------------------')
    print (board[0][0],'|',board[0][1],'|',board[0][2],'|',board[0][3],'|',board[0][4],'|',board[0][5],'|',board[0][6],'|')
    print ('---------------------------')
#checks if they are 4 letters that are equal to each other 
def check(char, x1,x2,x3,x4,y1,y2,y3,y4):
    if board[x1][y1] == char and board[x2][y2] == char and board[x3][y3] == char and board[x4][y4] == char:
        return True
#checks all the winning cases of the game
def checkall(char):
    if  check(char,0,1,2,3,0,0,0,0):
        return True
    if  check(char,1,2,3,4,0,0,0,0):
        return True
    if  check(char,2,3,4,5,0,0,0,0):
        return True
    if  check(char,0,1,2,3,1,1,1,1):
        return True
    if  check(char,1,2,3,4,1,1,1,1):
        return True
    if  check(char,2,3,4,5,1,1,1,1):
        return True
    if  check(char,0,1,2,3,2,2,2,2):
        return True
    if  check(char,1,2,3,4,2,2,2,2):
        return True
    if  check(char,2,3,4,5,2,2,2,2):
        return True
    if  check(char,0,1,2,3,3,3,3,3):
        return True
    if  check(char,1,2,3,4,3,3,3,3):
        return True
    if  check(char,2,3,4,5,3,3,3,3):
        return True
    if  check(char,0,1,2,3,4,4,4,4):
        return True
    if  check(char,1,2,3,4,4,4,4,4):
        return True
    if  check(char,2,3,4,5,4,4,4,4):
        return True
    if  check(char,0,1,2,3,5,5,5,5):
        return True
    if  check(char,1,2,3,4,5,5,5,5):
        return True
    if  check(char,2,3,4,5,5,5,5,5):
        return True
    if  check(char,0,1,2,3,6,6,6,6):
        return True
    if  check(char,1,2,3,4,6,6,6,6):
        return True
    if  check(char,2,3,4,6,6,6,6,6):
        return True
    if  check(char,5,4,3,2,3,4,5,6):
        return True
    if  check(char,5,4,3,2,2,3,4,5):
        return True
    if  check(char,4,3,2,1,3,4,5,6):
        return True
    if  check(char,5,4,3,2,1,2,3,4):
        return True
    if  check(char,4,3,2,1,2,3,4,5):
        return True
    if  check(char,3,2,1,0,3,4,5,6):
        return True
    if  check(char,5,4,3,2,0,1,2,3):
        return True
    if  check(char,4,3,2,1,1,2,3,4):
        return True
    if  check(char,3,2,1,0,2,3,4,5):
        return True
    if  check(char,4,3,2,1,0,1,2,3):
        return True
    if  check(char,3,2,1,0,1,2,3,4):
        return True
    if  check(char,3,2,1,0,0,1,2,3):
        return True
    if  check(char,2,3,4,5,0,1,2,3):
        return True
    if  check(char,1,2,3,4,0,1,2,3):
        return True
    if  check(char,2,3,4,5,1,2,3,4):
        return True
    if  check(char,0,1,2,3,0,1,2,3):
        return True
    if  check(char,1,2,3,4,1,2,3,4):
        return True
    if  check(char,2,3,4,5,2,3,4,5):
        return True
    if  check(char,0,1,2,3,1,2,3,4):
        return True
    if  check(char,1,2,3,4,2,3,4,5):
        return True
    if  check(char,2,3,4,5,3,4,5,6):
        return True
    if  check(char,0,1,2,3,2,3,4,5):
        return True
    if  check(char,1,2,3,4,3,4,5,6):
        return True
    if  check(char,0,1,2,3,3,4,5,6):
        return True
    if  check(char,0,0,0,0,0,1,2,3):
        return True
    if  check(char,0,0,0,0,1,2,3,4):
        return True
    if  check(char,0,0,0,0,2,3,4,5):
        return True
    if  check(char,0,0,0,0,3,4,5,6):
        return True
    if  check(char,1,1,1,1,0,1,2,3):
        return True
    if  check(char,1,1,1,1,1,2,3,4):
        return True
    if  check(char,1,1,1,1,2,3,4,5):
        return True
    if  check(char,1,1,1,1,3,4,5,6):
        return True
    if  check(char,2,2,2,2,0,1,2,3):
        return True
    if  check(char,2,2,2,2,1,2,3,4):
        return True
    if  check(char,2,2,2,2,2,3,4,5):
        return True
    if  check(char,2,2,2,2,3,4,5,6):
        return True
    if  check(char,3,3,3,3,0,1,2,3):
        return True
    if  check(char,3,3,3,3,1,2,3,4):
        return True
    if  check(char,3,3,3,3,2,3,4,5):
        return True
    if  check(char,3,3,3,3,3,4,5,6):
        return True
    if  check(char,4,4,4,4,0,1,2,3):
        return True
    if  check(char,4,4,4,4,1,2,3,4):
        return True
    if  check(char,4,4,4,4,2,3,4,5):
        return True
    if  check(char,4,4,4,4,3,4,5,6):
        return True
    if  check(char,5,5,5,5,0,1,2,3):
        return True
    if  check(char,5,5,5,5,1,2,3,4):
        return True
    if  check(char,5,5,5,5,2,3,4,5):
        return True
    if  check(char,5,5,5,5,3,4,5,6):
        return True
    

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
show()
#alternates turns between each player  
while True:
    for turn in range(41):
        if turn%2 == 0:
            inpu = int(input("select a spot 0-6: "))
            if inpu ==0:
                if a<6: 
                    board[a][inpu] = 'x'
                    a = a+1
                else:
                    print("choose another slot")
            elif inpu == 1:
                if b<6: 
                    board[b][inpu] = 'x'
                    b = b+1
                else:
                    print("choose another slot")
            elif inpu == 2:
                if c<6: 
                    board[c][inpu] = 'x'
                    c = c+1
                else:
                    print("choose another slot")
            elif inpu == 3:
                if d<6: 
                    board[d][inpu] = 'x'
                    d = d+1
                else:
                    print("choose another slot")
            elif inpu == 4:
                if e<6: 
                    board[e][inpu] = 'x'
                    e = e+1
                else:
                    print("choose another slot")
            elif inpu == 5:
                if f<6: 
                    board[f][inpu] = 'x'
                    f = f+1
                else:
                    print("choose another slot")
            elif inpu == 6:
                if g<6: 
                    board[g][inpu] = 'x'
                    g = g+1
                else:
                    print("choose another slot")
            elif inpu > 6:
                print("I said a number between 0-6")
            show()
        if checkall("x") == True:
            print("X is the winner")
            break;
        elif turn%2 == 1:
                inpu = int(input("select a spot 0-6: "))
                if inpu ==0:
                    if a<6: 
                        board[a][inpu] = 'O'
                        a = a+1
                    else:
                        print("choose another slot")
                elif inpu == 1:
                    if b<6: 
                        board[b][inpu] = 'O'
                        b = b+1
                    else:
                        print("choose another slot")
                elif inpu == 2:
                    if c<6: 
                        board[c][inpu] = 'O'
                        c = c+1
                    else:
                        print("choose another slot")
                elif inpu == 3:
                    if d<6: 
                        board[d][inpu] = 'O'
                        d = d+1
                    else:
                        print("choose another slot")
                elif inpu == 4:
                    if e<6: 
                        board[e][inpu] = 'O'
                        e = e+1
                    else:
                        print("choose another slot")
                elif inpu == 5:
                    if f<6: 
                        board[f][inpu] = 'O'
                        f = f+1
                    else:
                        print("choose another slot")
                elif inpu == 6:
                    if g<6: 
                        board[g][inpu] = 'O'
                        g = g+1
                    else:
                        print("choose another slot")
                show()
        if checkall("O") == True:
            print("O is the winner")
            break;
    break;
    
    
    
