#Import commands####################################################
import turtle
import numpy as np
        
        
#Set up world#######################################################
turtle.hideturtle()
turtle.delay(0)
turtle.speed(0)
turtle.hideturtle()
turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()
turtle.bgcolor('light slate gray')
screen = turtle.Screen()
screen.setup(800,800)
screen.setworldcoordinates(-500,-500,500,500)
screen.title('Connect 4 :)')

#Game parameters#################################################
rows = 6
columns = 7
startingxcoord = -450
startingycoord = -450 * (rows/columns)
width = startingxcoord * -2
height = startingycoord * -2

#Graphics########################################################


#Game Over Functions#############################################
def gameover_r():
  with open('amountofturns.txt', 'a') as myfile:
      myfile.write('Amount of turns taken: ' + str(click.counter) + '\n')
  screen = turtle.Screen()
  screen.setup(800,800)
  screen.setworldcoordinates(-500,-500,500,500)
  screen.title('Connect 4 :)')
  turtle.pencolor('black')
  turtle.penup()
  turtle.goto(0,200)
  turtle.pendown()
  turtle.write('Game Over', align = 'center', font =('Times New Roman', 100, 'normal'))
  turtle.pencolor('black')
  turtle.penup()
  turtle.goto(0,200)
  turtle.pendown()
  turtle.write('Game Over', align = 'center', font =('Times New Roman', 100, 'normal'))
  turtle.pencolor('maroon')
  turtle.penup()
  turtle.goto(0,-200)
  turtle.pendown()
  turtle.write('Maroon Won', align = 'center', font =('Times New Roman', 80, 'normal'))
def gameover_w():
  with open('amountofturns.txt', 'a') as myfile:
      myfile.write('Amount of turns taken: ' + str(click.counter) + '\n')
  screen = turtle.Screen()
  screen.setup(800,800)
  screen.setworldcoordinates(-500,-500,500,500)
  screen.title('Connect 4 :)')
  turtle.bgcolor('black')
  turtle.pencolor('white')
  turtle.penup()
  turtle.goto(0,200)
  turtle.pendown()
  turtle.write('Game Over', align = 'center', font =('Times New Roman', 100, 'normal'))
  turtle.penup()
  turtle.goto(0,-200)
  turtle.pendown()
  turtle.write('White Won', align = 'center', font =('Times New Roman', 80, 'normal'))
def gameover_t():
  with open('amountofturns.txt', 'a') as myfile:
      myfile.write('Amount of turns taken: ' + str(click.counter) + '\n')
  screen = turtle.Screen()
  screen.setup(800,800)
  screen.setworldcoordinates(-500,-500,500,500)
  screen.title('Connect 4 :)')
  turtle.penup()
  turtle.goto(0,200)
  turtle.pendown()
  turtle.write('Game Over', align = 'center', font =('Times New Roman', 100, 'normal'))
  turtle.penup()
  turtle.goto(0,-200)
  turtle.pendown()
  turtle.write('Its a tie!', align = 'center', font =('Times New Roman', 80, 'normal'))
  turtle.penup()
  turtle.goto(0,-270)
  turtle.pendown()
  turtle.write('I guess no one wins :(', align = 'center', font = ('Times New Roman', 50))
  
  
#Draw Board Functions#############################################
def drawboard(x,y,w,h,c):
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(c)
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()
def draw_start(): 
  def click_3(x,y):
        if x < 0 and x > -500:
                   turtle.clear()
                   screen = turtle.Screen()
                   screen.setup(800,800)
                   screen.setworldcoordinates(-500,-500,500,500)
                   drawboard(startingxcoord, startingycoord, width, height, 'black' )
                   turtle.onscreenclick(click)
                   x = -500
                   y = -300
                   x_interval = 875/7
                   y_interval = 700/6
                   for i in range(6):
                       x = -500
                       for j in range(7):
                           x += x_interval 
                           turtle.penup()
                           turtle.goto(x,y)
                           turtle.pendown()
                           turtle.pencolor('light slate gray')
                           turtle.dot(75)
                       y += y_interval
                   turtle.onscreenclick(click)
  def click_1(x,y):
       if x < 0 and x > -500:
           turtle.clear()
           screen = turtle.Screen()
           screen.setup(800,800)
           screen.setworldcoordinates(-500,-500,500,500)
           drawboard(startingxcoord, startingycoord, width, height, 'black' )
           turtle.onscreenclick(click)
           x = -500
           y = -300
           x_interval = 875/7
           y_interval = 700/6
           for i in range(6):
                x = -500
                for j in range(7):
                    x += x_interval 
                    turtle.penup()
                    turtle.goto(x,y)
                    turtle.pendown()
                    turtle.pencolor('light slate gray')
                    turtle.dot(75)
                y += y_interval
           turtle.onscreenclick(click)
       elif x >0 and x < 500:
          turtle.clear()
          screen = turtle.Screen()
          screen.setup(800,800)
          screen.setworldcoordinates(-500,-500,500,500)
          turtle.penup()
          turtle.goto(-470,300)
          turtle.pendown()
          turtle.write('Rules', font =('Times New Roman', 50, 'normal'))
          turtle.penup()
          turtle.goto(-470, 200)
          turtle.write('1. Click on which column you want to drop your piece', font =('Times New Roman', 20, 'normal'))
          turtle.penup()
          turtle.goto(-470, 160)
          turtle.write('2. Click on the red x to exit the game', font =('Times New Roman', 20, 'normal'))
          turtle.penup()
          turtle.goto(-470, 120)
          turtle.write('3. Whoever gets 4 in a row first wins', font =('Times New Roman', 20, 'normal'))
          turtle.penup()
          turtle.goto(-200,-100)
          turtle.pencolor('green')
          turtle.dot(250)
          turtle.penup()
          turtle.goto(-250,-100)
          turtle.pendown()
          turtle.pencolor('black')
          turtle.write('Start', font =('Times New Roman', 25, 'normal'))
          turtle.onscreenclick(click_3)
  screen = turtle.Screen()
  screen.setup(800,800)
  screen.setworldcoordinates(-500,-500,500,500)
  screen.title('Connect 4 :)')
  turtle.penup()
  turtle.goto(-470,300)
  turtle.pendown()
  turtle.write('Connect Four', align = 'left', font =('Times New Roman', 50, 'normal'))
  turtle.penup()
  turtle.goto(-200,-100)
  turtle.pencolor('green')
  turtle.dot(250)
  turtle.penup()
  turtle.goto(-250,-100)
  turtle.pendown()
  turtle.pencolor('black')
  turtle.write('Start', font =('Times New Roman', 25, 'normal'))
  turtle.penup()
  turtle.goto(200,-100)
  turtle.pencolor('gray')
  turtle.dot(250)
  turtle.penup()
  turtle.goto(150,-100)
  turtle.pendown()
  turtle.pencolor('black')
  turtle.write('Rules', font =('Times New Roman', 25, 'normal')) 
  turtle.onscreenclick(click_1)

draw_start()

#Checking if the game is over#########################
def checkIfWonHorizontally(row, column, board, user_symbol):
    """
    Determines if the most recently placed peice forms four in a row in the
    horizontal direction

    Parameters
    ----------
    row : integer
        The row number that the placed peice was in
    column : integer
        The column number that the placed peice was in
    board : Array
        Array of the current board with the current pieces on it
    user_symbol : string
        Symbolizes the user's move

    Returns
    -------
    bool
        If the function returns True, than there is four in a row and the
        player has won.  If the function returns False, then the player has
        not made four in a row and has not won the game yet

    """
    #horizontally
    row = board[row]
    leftmost = column
    symbols_list = []
    while(row[leftmost] == user_symbol):
        if(leftmost == 0):
            break
        elif(row[leftmost - 1] == user_symbol):
            leftmost -= 1
        else:
            break
    for i in range(5):
        if((leftmost + i) > 6):
            break
        elif(not row[leftmost + i] == user_symbol):
            break
        else:
            symbols_list.append(row[leftmost + i])
    if(i == 4):
        return True
    else:
        return False
def checkIfWonVertically(row, column, board, user_symbol):
    """
    Determines if the most recently placed peice forms four in a row in the
    vertical direction

    Parameters
    ----------
    row : integer
        The row number that the placed peice was in
    column : integer
        The column number that the placed peice was in
    board : Array
        Array of the current board with the current pieces on it
    user_symbol : string
        Symbolizes the user's move

    Returns
    -------
    bool
        If the function returns True, than there is four in a row and the
        player has won.  If the function returns False, then the player has
        not made four in a row and has not won the game yet

    """
    column_as_list = []
    symbols_list = []
    for i in range(6):
        column_as_list.append(board[5 - i][column])
    if row == 0:
        leftmost = 5
    elif row == 1:
        leftmost = 4
    elif row == 2:
        leftmost = 3
    elif row == 3:
        leftmost = 2
    elif row == 4:
        leftmost = 1
    else:
        leftmost = 0
    while(column_as_list[leftmost] == user_symbol):
        if(leftmost == 0):
            break
        elif(column_as_list[leftmost - 1] == user_symbol):
            leftmost -= 1
        else:
            break
    for i in range(5):
        if((leftmost + i) > 5):
            break
        elif(not column_as_list[leftmost + i] == user_symbol):
            break
        else:
            symbols_list.append(column_as_list[leftmost + i])
    if(i == 4):
        return True
    else:
        return False
def checkIfWonDiagonally1(row, column, board, user_symbol):
    """
    Determines if the most recently placed peice forms four in a row in the
    diagonal direction from bottom left to top right

    Parameters
    ----------
    row : integer
        The row number that the placed peice was in
    column : integer
        The column number that the placed peice was in
    board : Array
        Array of the current board with the current pieces on it
    user_symbol : string
        Symbolizes the user's move

    Returns
    -------
    bool
        If the function returns True, than there is four in a row and the
        player has won.  If the function returns False, then the player has
        not made four in a row and has not won the game yet

    """
    bottom_leftmost_row = row
    bottom_leftmost_col = column
    diagonal_list = []
    while(row < 5) and (column > 0):
        row += 1
        column -= 1
        bottom_leftmost_row = row
        bottom_leftmost_col = column
    while((row > 0) and (column < 6)):
        diagonal_list.append(board[bottom_leftmost_row][bottom_leftmost_col])
        row -= 1
        column += 1
        bottom_leftmost_row = row
        bottom_leftmost_col = column
    if(len(diagonal_list) < 4):
        return False
    else:
        for i in range(len(diagonal_list)):
            if i > (len(diagonal_list) - 4):
                return False
            for k in range(4):
                if(diagonal_list[i] == diagonal_list[i + 1] == diagonal_list[i + 2] == diagonal_list[i + 3] == user_symbol):
                    return True
def checkIfWonDiagonally2(row, column, board, user_symbol):
    top_leftmost_row = row
    top_leftmost_col = column
    diagonal_list = []
    while(row > 0) and (column > 0):
        row -= 1
        column -= 1
        top_leftmost_row = row
        top_leftmost_col = column

    while((row < 5) and (column < 6)):
        diagonal_list.append(board[top_leftmost_row][top_leftmost_col])
        row += 1
        column += 1
        top_leftmost_row = row
        top_leftmost_col = column
    diagonal_list.append(board[top_leftmost_row][top_leftmost_col])
    if(len(diagonal_list) < 4):
        return False
    else:
        for i in range(len(diagonal_list)):
            if i > (len(diagonal_list) - 4):
                return False
            for k in range(4):
                if(diagonal_list[i] == diagonal_list[i + 1] == diagonal_list[i + 2] == diagonal_list[i + 3] == user_symbol):
                    return True       

#Initial Coordinates######################################################################
x = -500
y = -300
x_interval = 875/7
y_interval = 700/6

    
moves__375 = {1:0,2:0,3:0,4:0,5:0,6:0}
moves__250 = {1:0,2:0,3:0,4:0,5:0,6:0}
moves__125 = {1:0,2:0,3:0,4:0,5:0,6:0}
moves_0 = {1:0,2:0,3:0,4:0,5:0,6:0}
moves_125 = {1:0,2:0,3:0,4:0,5:0,6:0}
moves_250 = {1:0,2:0,3:0,4:0,5:0,6:0}
moves_375 = {1:0,2:0,3:0,4:0,5:0,6:0}

arr_r = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).reshape(6,7)

arr_w = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]).reshape(6,7)


#Defining click##########################################################################
def click(x,y):
    click.counter += 1
    global c
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    if x > -500 and x < -312.5:
        x = -375
        z = -300
        k = 1
        for i in range(6):
            if moves__375[k] == 0:
                y = z
                moves__375[k] = 1
                break
            else:
                z += y_interval
            k += 1
    elif x > -312.5 and x < -187.5:
        x = -250
        z = -300
        k = 1
        for i in range(6):
            if moves__250[k] == 0:
                y = z
                moves__250[k] = 1
                break
            else:
                z += y_interval
            k += 1
    elif x > -187.5 and x < -62.5:
        x = -125
        z = -300
        k = 1
        for i in range(6):
            if moves__125[k] == 0:
                y = z
                moves__125[k] = 1
                break
            else:
                z += y_interval
            k += 1
    elif x > -62.5 and x < 62.5:
        x = 0
        z = -300
        k = 1
        for i in range(6):
            if moves_0[k] == 0:
                y = z
                moves_0[k] = 1
                break
            else:
                z += y_interval
            k += 1
    elif x > 62.5 and x < 187.5:
        x = 125
        z = -300
        k = 1
        for i in range(6):
            if moves_125[k] == 0:
                y = z
                moves_125[k] = 1
                break
            else:
                z += y_interval
            k += 1
    elif x > 187.5 and x < 312.5:
        x = 250
        z = -300
        k = 1
        for i in range(6):
            if moves_250[k] == 0:
                y = z
                moves_250[k] = 1
                break
            else:
                z += y_interval
            k += 1
    elif x > 312.5 and x < 500:
        x = 375
        z = -300
        k = 1
        for i in range(6):
            if moves_375[k] == 0:
                y = z
                moves_375[k] = 1
                break
            else:
                z += y_interval
            k += 1
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    if (click.counter % 2) == 0:
        turtle.pencolor('maroon')
        if x == -375:
            a = 0
        elif x == -250:
            a = 1
        elif x == -125:
            a = 2
        elif x == 0:
            a = 3
        elif x == 125:
            a = 4
        elif x == 250:
            a = 5
        elif x == 375:
            a = 6
        b = k - 1
        
        arr_r[b][a] = 1
        d = (checkIfWonHorizontally(b, a, arr_r, 1))
        e = (checkIfWonVertically(b, a, arr_r, 1))
        f = (checkIfWonDiagonally1(b, a, arr_r, 1))
        l = (checkIfWonDiagonally2(b, a, arr_r, 1))
        if d == True or e == True or f == True or l == True:
            turtle.clear()
            gameover_r()
    else:
        turtle.pencolor('white')
        if x == -375:
            a = 0
        elif x == -250:
            a = 1
        elif x == -125:
            a = 2
        elif x == 0:
            a = 3
        elif x == 125:
            a = 4
        elif x == 250:
            a = 5
        elif x == 375:
            a = 6
        b = k-1
        arr_w[b][a] = 1
        g = (checkIfWonHorizontally(b, a, arr_w, 1))
        h = (checkIfWonVertically(b, a, arr_w, 1))
        i = (checkIfWonDiagonally1(b, a, arr_w, 1))
        j = (checkIfWonDiagonally2(b, a, arr_w, 1))
        if g == True or h == True or i == True or j == True:
            turtle.clear()
            gameover_w()
    if click.counter == 42:
        turtle.clear()
        gameover_t()
        
    turtle.dot(75)
click.counter = 0


#FINAL COMMANDS############################################################
turtle.listen()
 
turtle.done()

    
#Read file##########################################################
#Will read the average of the amount of turns taken on users console
with open('amountofturns.txt', 'r') as readfile:
    readfile = readfile.readlines()
    totalturns = 0
    sumofturns = 0
    for i in range(len(readfile)):
        readfile[i] = readfile[i].split()
    for i in range(len(readfile)):
        totalturns += 1
        sumofturns += int(readfile[i][-1])
    ###Try and Except Statement###################
    try:
        average = sumofturns/totalturns
        print(f'The average of the turns taken on this computer is {average}')
    except:
        print('Average could not be computed')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    

    
    

    
    
    
    
    
    


  
  
