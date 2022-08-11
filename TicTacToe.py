
import time
import pygame
pygame.init()

fps =30
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
size = height

if(height>width):
    size=width
size=size/1.5



screen = pygame.display.set_mode((size,size))
turn =0
rows, cols = (3, 3)
gameBoard = [[0 for i in range(cols)] for j in range(rows)]
BoardXCoords = [size/6,size/2,size*5/6]
BoardYCoords = [size/6,size/2,size*5/6]
winStart=0,0
winEnd=0,0
hasWin=False
hasDraw =False

# loading the images as python object
x_img = pygame.image.load("Ximg.svg")
y_img = pygame.image.load("Oimg.svg")
  
  
# resizing images
x_img = pygame.transform.scale(x_img, (size/3, size/3))
o_img = pygame.transform.scale(y_img, (size/3, size/3))

pygame.display.set_caption('Tic Tac Toe')
def drawBoard():
    screen.fill((255, 255, 255))
    pygame.draw.line(screen,(0,0,0), (size/3, 0), (size/3, size) ,int(size*0.01))#vertical #1
    pygame.draw.line(screen,(0,0,0), (size*2/3, 0), (size*2/3, size) ,int(size*0.01))#vertical #2
    pygame.draw.line(screen,(0,0,0), (0, size/3), (size, size/3) ,int(size*0.01))#horizontal #1
    pygame.draw.line(screen,(0,0,0), (0, size*2/3), (size, size*2/3) ,int(size*0.01))#horizontal #2
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j]==1:
                screen.blit(x_img, (size*i/3,size*j/3 ))
            if gameBoard[i][j]==2:
                screen.blit(o_img, (size*i/3,size*j/3 ))
    if hasWin==True:
        drawWinLine(winStart,winEnd)
    pygame.display.flip()

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win):      
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('arial', int(size/30))
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

pvpButton = button((70,129,244),size/15 ,size/4,size/3,size/4,'Player Vs Player')
pvcX = button((70,129,244),size*14/15-size/3,size/4,size/3,size/8-int(size/80),"Start as X")
pvcO = button((70,129,244),size*14/15-size/3,size/4+size/8+int(size/80),size/3,size/8-int(size/80),'Start as O')




def playerTurn(x,y):
    global turn
    if gameBoard[findPos(x,y)[0]][findPos(x,y)[1]]==0:
        if turn%2==0:
            gameBoard[findPos(x,y)[0]][findPos(x,y)[1]]=1
        else:
            gameBoard[findPos(x,y)[0]][findPos(x,y)[1]]=2
        turn=turn+1
    isWin()

def isWin():
    global winStart
    global winEnd
    global hasWin
    global hasDraw
    for i in range(3):
        if gameBoard[0][i] == gameBoard[1][i] and gameBoard[1][i] ==gameBoard[2][i] and gameBoard[2][i]!=0:
            winStart=(BoardXCoords[0]-size*0.1,BoardYCoords[i])
            winEnd=(BoardXCoords[2]+size*0.1,BoardYCoords[i])
            hasWin=True
    for i in range(3):
        if gameBoard[i][0]== gameBoard[i][1] and gameBoard[i][1]== gameBoard[i][2] and gameBoard[i][2]!=0:
            winStart=(BoardXCoords[i],BoardYCoords[0]-size*0.1)
            winEnd=(BoardXCoords[i],BoardYCoords[2]+size*0.1)
            hasWin=True
    if gameBoard[2][0] == gameBoard[1][1] and gameBoard[1][1] ==gameBoard[0][2] and gameBoard[0][2]!=0:
        winStart=(BoardXCoords[2]+size*0.1,BoardYCoords[0]-size*0.1)
        winEnd=(BoardXCoords[0]-size*0.1,BoardYCoords[2]+size*0.1)
        hasWin=True

    if gameBoard[0][0] == gameBoard[1][1] and gameBoard[1][1]== gameBoard[2][2] and gameBoard[2][2]!=0:
        winStart=(BoardXCoords[0]-size*0.1,BoardYCoords[0]-size*0.1)
        winEnd=(BoardXCoords[2]+size*0.1,BoardYCoords[2]+size*0.1)
        hasWin=True

    if(isDraw()==True):
        hasDraw=True

    if hasWin==True or hasDraw==True:
        pygame.display.set_caption('Click again to play')
def drawWinLine(start,end):
    pygame.draw.line(screen,(0,0,0), start,end ,int(size*0.045))

def reset():
    global computer
    computer =""
    global opponent
    opponent=""
    global winStart
    winStart = 0,0
    global winEnd
    winEnd=0,0
    global hasWin
    hasWin=False
    global hasDraw
    hasDraw =False
    global gameBoard
    gameBoard = [[0 for i in range(cols)] for j in range(rows)]
    global turn
    turn =0
    startScreen()
def isDraw():
    for i in range(3):
        for j in range(3):
            if gameBoard[i][j] == 0:
                return False
    return True

def findPos(x,y):
    if x<size/3:
        returnX=0
    if x>size/3 and x<size*2/3:
        returnX=1
    if x>size*2/3 and x<size:
        returnX=2

    if y<size/3:
        returnY=0
    if y>size/3 and y<size*2/3:
        returnY=1
    if y>size*2/3 and y<size:
        returnY=2
    return returnX, returnY

def isMovesLeft(gameBoard) :
 
    for i in range(3) :
        for j in range(3) :
            if (gameBoard[i][j] == 0) :
                return True
    return False

def evaluate(b) :
   
    # Checking for Rows for X or O victory.
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
            if (b[row][0] == computer) :
                return 10
            elif (b[row][0] == opponent) :
                return -10
 
    # Checking for Columns for X or O victory.
    for col in range(3) :
      
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
            if (b[0][col] == computer) :
                return 10
            elif (b[0][col] == opponent) :
                return -10
 
    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
        if (b[0][0] == computer) :
            return 10
        elif (b[0][0] == opponent) :
            return -10
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == computer) :
            return 10
        elif (b[0][2] == opponent) :
            return -10
 
    # Else if none of them have won then return 0
    return 0

def minimax(gameBoard, depth, isMax) :
    score = evaluate(gameBoard)
 
    # If Maximizer has won the game return his/her
    # evaluated score
    if (score == 10) :
        return score
 
    # If Minimizer has won the game return his/her
    # evaluated score
    if (score == -10) :
        return score
 
    # If there are no more moves and no winner then
    # it is a tie
    if (isMovesLeft(gameBoard) == False) :
        return 0
 
    # If this maximizer's move
    if (isMax) :    
        best = -1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (gameBoard[i][j]==0) :
                 
                    # Make the move
                    gameBoard[i][j] = computer
 
                    # Call minimax recursively and choose
                    # the maximum value
                    best = max( best, minimax(gameBoard,
                                              depth + 1,
                                              not isMax) )
 
                    # Undo the move
                    gameBoard[i][j] = 0
        return best
 
    # If this minimizer's move
    else :
        best = 1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (gameBoard[i][j] == 0) :
                 
                    # Make the move
                    gameBoard[i][j] = opponent
 
                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(gameBoard, depth + 1, not isMax))
 
                    # Undo the move
                    gameBoard[i][j] = 0
        return best


def computerTurn(gameBoard):

    global turn
    turn =turn +1
    bestVal = -1000
    bestMove = (-1, -1)
 
    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3) :    
        for j in range(3) :
         
            # Check if cell is empty
            if (gameBoard[i][j] == 0) :
             
                # Make the move
                gameBoard[i][j] = computer
 
                # compute evaluation function for this
                # move.
                moveVal = minimax(gameBoard, 0, False)
 
                # Undo the move
                gameBoard[i][j] = 0
 
                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

def startPVP(): #start player vs player(pvp)
    running = True
    while running:
        drawBoard()
        if(hasWin==True or hasDraw==True):
            time.sleep(1)
            reset()
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            playerTurn(pos[0], pos[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
pygame.font.init()
my_font = pygame.font.SysFont('arial', int(size/20))
my_font2 = pygame.font.SysFont('arial', int(size/30))
def startScreen():
    running = True
    while running:
        screen.fill((255, 255, 255))
        pvpButton.draw(screen)
        pvcX.draw(screen)
        pvcO.draw(screen)
        text_surface = my_font.render("Welcome To Idan's Tic Tac Toe", 1, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(size/2,size/10))

        chooseText = my_font2.render("Player Vs Computer", 1, (0, 0, 0))
        screen.blit(text_surface, text_rect)
        screen.blit(chooseText, (size*14/15-size/3,size/4-int(size/24)))
        pygame.display.update()
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if pvpButton.isOver(pos):
                running=False
                startPVP()
            if pvcO.isOver(pos):
                running=False
                startCVP("o")
            if pvcX.isOver(pos):
                running=False
                startCVP("x")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

def startCVP(userTurn):#start computer vs player(cvp)
    global opponent 
    global computer
    global turn
    if userTurn=="o":
        opponent = 2
        computer = 1
    else:
        computer = 2
        opponent = 1
    running = True
    while running:
        drawBoard()
        if(hasWin==True or hasDraw==True):
            time.sleep(1)
            reset()

        if computer==1 and turn%2==0:
            bestMove = computerTurn(gameBoard)
            gameBoard[bestMove[0]][bestMove[1]]= 1
            isWin()
        elif turn%2==1 and computer==2:
            bestMove = computerTurn(gameBoard)
            gameBoard[bestMove[0]][bestMove[1]]= 2
            isWin()
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            playerTurn(pos[0], pos[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

startScreen()

