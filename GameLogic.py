####################################################################
# Alejandro Teajada 17854
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


##seeds=40

class Board:
    """
    Mancala logic game class 
    """
    def __init__(self):
        self.board = [4,4,4,4,4,0,4,4,4,4,4,0]
        self.turns_executed = []
        self.player1points = 0
        self.player2points = 0
        self.winner = ''
        self.finish = False

    def checkForWinner(self):
        '''Check for a winner.'''
        if (self.board[0] >= 20 ):
            self.winner = 'player1'
            finish = True
        elif(self.board[6] >= 20):
            self.winner = 'player2'
            finish = True

    def printBoard(self):
        print("\nCurrent board state: ")
        print(self.board)

    def printBoard_pretty(self):
        print("\nCurrent board state: ")
        print(self.board)
        print()
        print("\======== PLAYER 2 =========/ ")
        print("/===========================\ ")
        print("|/   \| "+str(self.board[10])+"  "+str(self.board[9])+"  "+str(self.board[8])+"  "+str(self.board[7])+"  "+str(self.board[6])+" |/   \|")
        print("|| "+str(self.board[11])+" ||" + " - - - - - - - || "+str(self.board[5])+" ||")
        print("|\   /| "+str(self.board[0])+"  "+str(self.board[1])+"  "+str(self.board[2])+"  "+str(self.board[3])+"  "+str(self.board[4])+" |\   /|")
        print("\===========================/")
        print("/======== PLAYER 1 =========\ ")

    def player1Turn(self):
        '''Options for making a move in the game.'''
        print("\nMove: ")
        print("1. a")
        print("2. b")
        print("3. c")
        print("4. d")
        print("5. e\n")
        choice = read_integer()

        if(choice == 1):
            hops = self.board[0]   ##the hops to make would be 4 in the first iteration, because the hole will have 4 seeds
            print("hops: "+str(hops))
            self.board[0] = 0      ##set current hole to cero
            i=1                    ##set next position
            self.turnIterations(i,hops)
        elif(choice == 2):
            hops = self.board[1]   ##set the hops to make based on the seeds in the hole
            print("hops: "+str(hops))
            self.board[1] = 0      
            i=2
            self.turnIterations(i,hops)
        elif(choice == 3):
            hops = self.board[2]    ##set the hops to make based on the seeds in the hole
            print("hops: "+str(hops))
            self.board[2] = 0      
            i=3
            self.turnIterations(i,hops)    
        elif(choice == 4):
            hops = self.board[3]    ##set the hops to make based on the seeds in the hole
            print("hops: "+str(hops))
            self.board[3] = 0      
            i=4
            self.turnIterations(i,hops)
        elif(choice == 5):
            hops = self.board[4]    ##set the hops to make based on the seeds in the hole
            print("hops: "+str(hops))
            self.board[4] = 0      
            i=5
            self.turnIterations(i,hops)

    def turnIterations(self,i,hops):
        '''Add seeds to the next hole and return to the first hole when number of hops exceeds len(array)'''
        #for i in hops:
        hops_plus_i = (hops+i-1)             ##This is the initial value of i where the player is going to make the move
        while(i <= hops_plus_i):
            if(i > len(self.board)):
                self.board[i-len(self.board)] = self.board[i-len(self.board)]+1
            else:
                print("hole position: "+str(i))
                print("current hole old value: "+str(self.board[i]))
                self.board[i] = self.board[i]+1
                print("current hole new value: "+str(self.board[i]))
            i = i + 1




Wellcome()

mancala = Board()

def menu():
    print(" ")
    print("-----------------------------------------------------------------")
    print(" 1. My turn")
    print(" 2. Print board")
    print(" 3. Exit")
    print("__________________________________________________________________\n")

    choice = read_integer()

    if choice == 1:
        print("")
        mancala.player1Turn()
        menu()   
    elif choice == 2:
        print(" ")
        #mancala.printBoard()
        mancala.printBoard_pretty()
        menu()   
    elif choice == 3:
        print(" ")
        theEnd()

    menu()



menu()



