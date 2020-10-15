####################################################################
# Alejandro Tejada 17854
# Diego Sevilla 17238
####################################################################
# Curso: Redes
# Programa: main_xmpp.py
# Propósito: Menu para la interaccion con el cliente
# Fecha: 09/2020
####################################################################
"""
    Mancala's logic. Simple implementation in python
"""

# ---------------ZONA DE LIBRERIAS-------------------



# --------------ZONA DE MODULOS----------------------

from Functions import *
import random

##seeds=40

class Board:
    """
    Implements Mancala logic game class 
    """
    def __init__(self):
        self.board = [4,4,4,4,4,0,4,4,4,4,4,0]
        self.turns_executed = []
        self.player1points = 0
        self.player2points = 0
        self.winner = ''
        self.finish = False
        #for randomly games
        self.player1moves = []
        self.player2moves = []
        self.tryAgainP1 = False
        self.tryAgainP2 = False


    def resetGame(self):
        self.board = [4,4,4,4,4,0,4,4,4,4,4,0]
        self.turns_executed = []
        self.player1points = 0
        self.player2points = 0
        self.winner = ''
        self.finish = False
        #for randomly games
        self.player1moves = []
        self.player2moves = []
        self.tryAgainP1 = False
        self.tryAgainP2 = False

    def checkForWinner(self):
        '''Check for a winner.'''
        if (self.board[5] >= 20 ):
            self.winner = 'player1'
            self.finish = True
        elif(self.board[11] >= 20):
            self.winner = 'player2'
            self.finish = True

    def updateScore(self):
        '''Set player 1 and player 2 points'''
        self.player1points = self.board[5]
        self.player2points = self.board[11]

    def printBoard(self):
        print("\nCurrent board state: ")
        print(self.board)
        print("length: "+str(len(self.board))+"  finalpos: "+str(self.board[11]))

    def printBoard_pretty(self):        
        print()
        print("\======== PLAYER 2 =========/ ")
        print("/===========================\ ")
        print("|/   \| "+str(self.board[10])+"  "+str(self.board[9])+"  "+str(self.board[8])+"  "+str(self.board[7])+"  "+str(self.board[6])+" |/   \|")
        if(self.board[11] > 9 and self.board[5]<9):
            print("|| "+str(self.board[11])+" |" + " - - - - - - - || "+str(self.board[5])+" ||")
        elif(self.board[5]>9 and self.board[11] < 9):
            print("|| "+str(self.board[11])+" ||" + " - - - - - - - | "+str(self.board[5])+" ||")
        elif(self.board[11] > 9 and self.board[5]>9):
            print("|| "+str(self.board[11])+" |" + " - - - - - - - | "+str(self.board[5])+" ||")
        else:
            print("|| "+str(self.board[11])+" ||" + " - - - - - - - || "+str(self.board[5])+" ||")
        print("|\   /| "+str(self.board[0])+"  "+str(self.board[1])+"  "+str(self.board[2])+"  "+str(self.board[3])+"  "+str(self.board[4])+" |\   /|")
        print("\===========================/")
        print("/======== PLAYER 1 =========\ ")
        print()

    def player1Turn(self,isRandom=False):
        '''Player 1 options for making a move in the game.'''
        if(isRandom):
            choice = random.randint(1,5)
        else:
            print("\nMove: ")
            print("1. a")
            print("2. b")
            print("3. c")
            print("4. d")
            print("5. e\n")
            choice = read_integer()

        self.player1moves.append(choice)  ##append all the moves made by the player to this array

        if(choice == 1):
            hops = self.board[0]   ##the hops to make would be 4 in the first iteration, because the hole will have 4 seeds
            if(hops == 0):         ##if hole is empty, player most try again
                self.tryAgainP1 = True
            else:                  ##if it is not empty, do the move
                print("hops: "+str(hops))
                self.board[0] = 0      ##set current hole to cero
                i=1                    ##set next position
                self.turnIterations(i,hops)
                self.tryAgainP1 = False
        elif(choice == 2):
            hops = self.board[1]   ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP1 = True
            else:
                print("hops: "+str(hops))
                self.board[1] = 0
                i=2
                self.turnIterations(i,hops)
                self.tryAgainP1 = False
        elif(choice == 3):            
            hops = self.board[2]    ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP1 = True
            else:
                print("hops: "+str(hops))
                self.board[2] = 0      
                i=3
                self.turnIterations(i,hops)    
                self.tryAgainP1 = False
        elif(choice == 4):
            hops = self.board[3]    ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP1 = True
            else:                
                print("hops: "+str(hops))
                self.board[3] = 0      
                i=4
                self.turnIterations(i,hops)
                self.tryAgainP1 = False
        elif(choice == 5):
            hops = self.board[4]    ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP1 = True
            else:                
                print("hops: "+str(hops))
                self.board[4] = 0      
                i=5
                self.turnIterations(i,hops)
                self.tryAgainP1 = False

    def turnIterations(self,i,hops):
        '''Add seeds to the next hole and return to the first hole when number of hops exceeds len(array)'''
        hops_plus_i = (hops+i-1)             ##This is the initial value of i where the player is going to make the move
        while(i <= hops_plus_i):
            if(i >= len(self.board)):
                self.board[i-len(self.board)] = self.board[i-len(self.board)]+1
            else:
                print("hole position: "+str(i))
                print("current hole old value: "+str(self.board[i]))
                self.board[i] = self.board[i]+1
                print("current hole new value: "+str(self.board[i]))
            i = i + 1

    def player2Turn(self,isRandom=False):
        '''Player 2 options for making a move in the game.'''
        if(isRandom):
            choice = random.randint(1,5)
        else:
            print("\nMove: ")
            print("1. a")
            print("2. b")
            print("3. c")
            print("4. d")
            print("5. e\n")
            choice = read_integer()
        self.player2moves.append(choice)

        if(choice == 1):
            hops = self.board[6]   ##Same logic as player one, but this time we start on the 6th position
            if(hops == 0):
                self.tryAgainP2 = True
            else:
                print("hops: "+str(hops))
                self.board[6] = 0      ##set current hole to cero
                i=7                    ##set next position
                self.turnIterations(i,hops)
                self.tryAgainP2 = False
        elif(choice == 2):
            hops = self.board[7]   ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP2 = True
            else:
                print("hops: "+str(hops))
                self.board[7] = 0      
                i=8
                self.turnIterations(i,hops)
                self.tryAgainP2 = False
        elif(choice == 3):
            hops = self.board[8]    ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP2 = True
            else:
                print("hops: "+str(hops))
                self.board[8] = 0      
                i=9
                self.turnIterations(i,hops)    
                self.tryAgainP2 = False
        elif(choice == 4):
            hops = self.board[9]    ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP2 = True
            else:
                print("hops: "+str(hops))
                self.board[9] = 0      
                i=10
                self.turnIterations(i,hops)
                self.tryAgainP2 = False
        elif(choice == 5):
            hops = self.board[10]    ##set the hops to make based on the seeds in the hole
            if(hops == 0):
                self.tryAgainP2 = True
            else:
                print("hops: "+str(hops))
                self.board[10] = 0      
                i=11
                self.turnIterations(i,hops)
                self.tryAgainP2 = False

    def letsPlayRandomly(self):
        i = 0
        while(self.finish == False):
            self.player1Turn(True)     ##player 1 makes a move
            ##if and while that force the player to choose a non empty hole               
            while(self.tryAgainP1 == True):
                self.player1Turn(True)

            self.player2Turn(True)     ##player 2 makes a move
            ##if and while that force the player to choose a non empty hole     
            while(self.tryAgainP2 == True):
                self.player2Turn(True)

            self.updateScore()
            self.checkForWinner()
            i = i+1
        print('The winner is: '+ self.winner)
        print('Player 1 moves: '+str(self.player1moves))
        print('Player 2 moves: '+str(self.player2moves))
        print('The final state of the board is:')
        self.printBoard_pretty()
        self.resetGame()

    def playWithDummyComputer(self):
        i = 0
        self.printBoard_pretty()
        while(self.finish == False):
            self.player1Turn()                ##player 1 makes a move
            ##if and while that force the player to choose a non empty hole       
            while(self.tryAgainP1 == True):
                print('You cannot take seeds from an empty hole! Try Again!')
                self.player1Turn()

            self.player2Turn(True)            ##player 2 makes a move
            ##if and while that force the player to choose a non empty hole                 
            while(self.tryAgainP2 == True):
                self.player2Turn(True)

            self.updateScore()
            self.checkForWinner()
            i = i+1
            self.printBoard_pretty()

        print('The winner is: '+ self.winner)
        print(str(i) +' moves in total!')
        print('Player 1 moves: '+str(self.player1moves))
        print('Player 2 moves: '+str(self.player2moves))
        print('The final state of the board is:')
        self.printBoard_pretty()
        self.resetGame()

Wellcome()

mancala = Board()

def menu():
    exit = 0
    print(" ")
    print("-----------------------------------------------------------------")
    print(" **********Testing**********")
    print(" 1. My turn")
    print(" 2. Player 2 Turn")
    print(" ***************************")
    print(" 3. Play with dummy computer")
    print(" 4. Print board")
    print(" 5. RandomGameComputer")
    print(" 6. Exit")
    print("__________________________________________________________________\n")

    choice = read_integer()

    if choice == 1:
        print("")
        mancala.player1Turn()
        menu()   
    elif choice == 2:
        print("")
        mancala.player2Turn()
        menu()   
    elif choice == 3:
        print(" ")
        mancala.playWithDummyComputer()
        menu() 
    elif choice == 4:
        print(" ")
        mancala.printBoard_pretty()
        menu() 
    elif choice == 5:
        print(" ")
        mancala.letsPlayRandomly()
        menu() 
    elif choice == 6:
        print(" ")
        exit = 1
        theEnd()
    if(exit == 0):
        menu()

menu()
