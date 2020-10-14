####################################################################
# Diego Sevilla 17238
####################################################################
# Curso: Redes
# Programa: main_xmpp.py
# Propósito: Menu para la interaccion con el cliente
# Fecha: 09/2020
####################################################################
"""
    Mancala's logic simple implementation in python
"""

# ---------------ZONA DE LIBRERIAS-------------------



# --------------ZONA DE MODULOS----------------------

from Functions import *




# ------------VARIABLES

seeds = 40

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
        self.finish = false

    def checkForWinner(self):
        i=0
        for i in len(self.board):
            if (self.board[0] >= 20 ):
                self.winner = 'player1'
                finish = true
            elif(self.board[6] >= 20):
                self.winner = 'player2'
                finish = true

    def player1_Turn(self):
        print("Move: ")
        print("1. a")
        print("2. b")
        print("3. c")
        print("4. d")
        print("5. e")
        choice = read_integer()

        if(choice == 1):
            hops = self.board[1]   ##the hops to make would be 4 in the first iteration
            self.board[1] = 0      ##set current hole to cero
            i=1                    ##set next position
            for i in hops:
                self.board[i] = self.board[i]+1


        elif(choice == 2):

        elif(choice == 3):
    
        elif(choice == 4):

        elif(choice == 5):

        elif(choice == 6):

        






            




#----------------Funciones




Wellcome()

def menu():
    print(" ")
    print(" -----------------------------------------------------------------")
    print(" 1. My turn")
    print(" 2. Exit")
    print("__________________________________________________________________")

    choice = read_integer()

    if choice == 1:
        print("")
 
        menu()   
    elif choice == 12:
        print(" ")
        theEnd()

    menu()

menu()

