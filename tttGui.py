from tkinter import *
from tkinter import ttk
import tttForGui
import os
import time

class TTTGui:

    def __init__(self, game):        
        self.game = game
        self.gameOver = False
        self.root = Tk()
        self.turn = 0
        self.label_text = " Player 1's turn "
        self.label = Label(self.root, text= self.label_text)
        self.label.grid(row=0, columnspan = 3)
        self.gui()
        

    def go(self, x, y, btn_num):
        turn_worked = self.game.player_turn(x, y)
        if self.turn % 2 == 0 and turn_worked:
            btn_num["text"] = ' X '
            self.label.config(text=" Player 2's turn ") 
            self.turn +=1                           
        elif turn_worked:
            btn_num["text"] = ' O '
            self.label.config(text=" Player 1's turn ")
            self.turn +=1
        if turn_worked == 2:
             self.label.config(text=" Game Over ")
             self.gameOver = True             
                     

    def gui(self):
        #b1
        btn_text = " _ "
        btn_hieght = 3
        btn_width = 7
        B1 = Button(self.root, text = btn_text, height = 3, width = btn_width)
        command= lambda x: self.go(0, 0, B1)
        B1.grid(row=1, column=0)
        B1.bind("<Button-1>", command)
        #b2
        B2 = Button(self.root, text=" _ ", height = 3, width = btn_width)
        command= lambda x: self.go(0,1, B2)
        B2.grid(row=1, column=1)
        B2.bind("<Button-1>", command)
        #b3
        B3 = Button(self.root, text=" _ ", height = 3, width = btn_width)
        command= lambda x: self.go(0,2, B3)
        B3.grid(row=1, column=2)
        B3.bind("<Button-1>", command)
        #b4
        B4 = Button(self.root, text=" _ ", height = 3, width = btn_width)
        command= lambda x: self.go(1,0, B4)
        B4.grid(row=2, column=0)
        B4.bind("<Button-1>", command)
        #b5
        B5 = Button(self.root, text=" _ ", height = 3, width = btn_width)
        command= lambda x: self.go(1, 1, B5)
        B5.grid(row=2, column=1)
        B5.bind("<Button-1>", command)
        #b6
        B6 = Button(self.root, text=" _ ", height = 3, width = btn_width)
        command= lambda x: self.go(1, 2, B6)
        B6.grid(row=2, column=2)
        B6.bind("<Button-1>", command)
        #b7
        B7 = Button(self.root, text=" _ ",height = 3, width = btn_width)
        command= lambda x: self.go(2, 0, B7)
        B7.grid(row=3, column=0)
        B7.bind("<Button-1>", command)
        #b8
        B8 = Button(self.root, text=" _ ", height = 3, width = btn_width)
        command= lambda x: self.go(2, 1, B8)
        B8.grid(row=3, column=1)
        B8.bind("<Button-1>", command)
        #b9
        B9 = Button(self.root, text=" _ ", height = 3, width = btn_width)
        command= lambda x: self.go(2, 2, B9)
        B9.grid(row=3, column=2)
        B9.bind("<Button-1>", command)

        self.root.mainloop()

    def __del__(self):
        print("deleted")

setup = tttForGui.Gameflow()
play = TTTGui(setup)

