#the board described by lists

board = [[' ','1', '2', '3', '4', '5', '6', '7'],["A",' ', ' ', 1, 1, 1, ' ', ' '],["B",' ', ' ', 1, 1, 1, ' ', ' '],["C",1, 1, 1, 1, 1, 1, 1],["D",1, 1, 1, 0, 1, 1, 1],["E",1, 1, 1, 1, 1, 1, 1],["F",' ', ' ', 1, 1, 1, ' ', ' '],["G",' ', ' ', 1, 1, 1, ' ', ' ']]

def bow():
    
    #function that loops the board after each turn
    
    for i in range(8):
        for j in range(8):
            print(board[i][j], end = ' ')
        print()
bow()


def input_user():
    
    #function that registers user's input
    
    if len(user_input) == 3:
        
        #check if the input of the user has the correct length
        
        if user_input[0].upper() not in ('ABCDEFG') and user_input[1] not in (1,2,3,4,5,6,7):
            print("Something is wrong with your input!")
        else:
            if user_input[2].upper() not in ('LUDR'):
                print("Direction is not L or R or U or D!")
            else:
                return True
    else:
        print("Something is wrong with your input!")

def selected_move():
    
    #desired move of the user
    
    for i in range(8):
        for j in range(8):
            if user_input[0].upper() == board[i][0] and user_input[1] == board[0][j]:
                x = i
                y = j
                return x,y

def selected_peg():
    
    #function to check the selected peg of the user

    if board[i][j] == ' ':
        if 0<i<=7 and 0<j<=7:
            print('Given peg position is out of board!')
    elif board[i][j] == 0:
        if 0<i<=7 and 0<j<=7:
            
            #check if the user selected the peg with the value of zero
        
            print('Given peg position does not have a peg!')
    else:
        
        #check the availability of pegs regarding L move
        
        if user_input[2].upper() == "L":
            if 0<i<=7 and 0<j-1<=7 and 0<j-2<=7:
                if board[i][j-1] == 0 and board[i][j-2] == 1:
                    print("No peg at next position to jump over!")
                elif board[i][j-1] == 1 and board[i][j-2] == 1:
                    print ("Landing position is occupied!")
                elif isinstance(board[i][j-2], str):
                    print ("Moving peg will fall out of bounds!")
                else:
                    return True
        
        #check the availability of pegs regarding U move
        
        elif user_input[2].upper() == "D":
            if 0<i+1<=7 and 0<i+2<=7 and 0<j<=7:
                if board[i+1][j] == 0 and board[i+2][j] == 1:
                    print("No peg at next position to jump over!")
                elif board[i+1][j] == 1 and board[i+2][j] == 1:
                    print ("Landing position is occupied!")
                elif isinstance(board[i+2][j], str):
                    print ("Moving peg will fall out of bounds!")
                else:
                    return True
        #check the availability of pegs regarding D move
        
        elif user_input[2].upper() == "U":
            if 0<i-1<=7 and 0<i-2<=7 and 0<j<=7:
                if board[i-1][j] == 0 and board[i-2][j] == 1:
                    print("No peg at next position to jump over!")
                elif board[i-1][j] == 1 and board[i-2][j] == 1:
                    print ("Landing position is occupied!")
                elif isinstance(board[i-2][j], str):
                    print ("Moving peg will fall out of bounds!")
                else:
                    return True
        #check the availability of pegs regarding R move
        
        elif user_input[2].upper() == "R":
            if 0<i<=7 and 0<j+1<=7 and 0<j+2<=7:
                if board[i][j+1] == 0 and board[i][j+2] == 1:
                    print("No peg at next position to jump over!")
                elif board[i][j+1] == 1 and board[i][j+2] == 1:
                    print ("Landing position is occupied!")
                elif isinstance(board[i][j+2], str):
                    print ("Moving peg will fall out of bounds!")
                else:
                    return True

def moving_peg():
    if user_input[2].upper() == 'L':
        n = 0
        m = -1
        h = 0
        k = -2
        return n,m,h,k
    elif user_input[2].upper() == 'R':
        n = 0
        m = +1
        h = 0
        k = +2
        return n,m,h,k
    elif user_input[2].upper() == 'D':
        n = +1
        m = 0
        h = +2
        k = 0
        return n,m,h,k 
    elif user_input[2].upper() == 'U':
        n = -1
        m = 0
        h = -2
        k = 0
        return n,m,h,k

def moves_left():
    
    #function that checks how many moves are left for the user
    
    for i in range (1,8):
        for j in range (1,8):
            if board[i][j] == 1:
                if 0<i<=7 and 0<j-2<=7 and 0<j-1<=7:
                    if board[i][j-1] == 1 and board[i][j-2] == 0:
                        return True
                if 0<i<=7 and 0<j+2<=7 and 0<j+1<=7:    
                    if board[i][j+1] == 1 and board[i][j+2] == 0:
                        return True
                if 0<i-1<=7 and 0<i-2<=7 and 0<j<=7:    
                    if board[i-1][j] == 1 and board[i-2][j] == 0:
                        return True
                if 0<i+1<=7 and 0<i+2<=7 and 0<j<=7:    
                    if board[i+1][j] == 1 and board[i+2][j] == 0:
                        return True
    return False

def pegs_left():
    
    #function that checks how many pegs are left on the board

    h = 0
    for i in range(8):
        board[i].count(1)
        h += board[i].count(1)
    print ("No more moves. The number of remaining pegs is", h)


while moves_left() == True:
    user_input = str(input("Enter peg position followed by move (L, R, U, or D):"))
    if input_user() == True:
        i,j = selected_move()
        if selected_peg() == True:
            n,m,h,k = moving_peg()
            board[i+n][j+m] = 0
            board[i+h][j+k] = 1
            board[i][j] = 0
            bow()
pegs_left()