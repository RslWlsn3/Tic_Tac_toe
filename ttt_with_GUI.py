from tkinter import *
from tkinter import ttk
import tttForGui
import os
import time
from functools import partial

class TTTGui:

    def __init__(self, game):        
        self.game = game
        self.gameOver = False
        self.root = Tk()
        self.turn = 0
        self.label_text = " Player 1's turn "
        self.label = Label(self.root, text= self.label_text)
        self.label.grid(row=0, columnspan = 3)
        self.button_list = []
        self.game_mode = input("1. Single player\n2.Two player")
        self.gui()
          

    def button_pressed(self, xyList, *nothing):
        x = xyList[0]
        y = xyList[1]
        btn_num = (x*3)+y
        turn_worked = self.game.player_turn(x, y, self.game_mode)
        if self.turn % 2 == 0 and turn_worked:
            btn = self.button_list[btn_num]
            btn["text"] = ' X '
            self.label.config(text=" Player 2's turn ") 
            self.turn +=1
                                       
        elif turn_worked:
            btn = self.button_list[btn_num]
            btn["text"] = ' O '
            self.label.config(text=" Player 1's turn ")
            self.turn +=1
            
        if turn_worked == 2: #2 means game over but this isn't very clear-----------
            self.label.config(text=" Game Over ")
            self.gameOver = True 
            
        elif self.game_mode == '1' and turn_worked:
            comp_list =  self.game.computer_play()            
            btn_num = (comp_list[0]*3)+comp_list[1]
            btn = self.button_list[btn_num]
            btn["text"] = ' O '
            self.label.config(text=" Player 1's turn ")
            self.turn +=1 
            if comp_list[2] is True:
                self.label.config(text=" Game Over ")
                self.gameOver = True                      

    def gui(self):
        #b1
        self.btn_text = " _ "
        self.btn_hieght = 3
        self.btn_width = 7        
        
        for row in range(3):
            for column in range(3):
                btn = Button(self.root, text = self.btn_text, height = self.btn_hieght, width = self.btn_width)
                xyList = [row, column]            
                command = partial(self.button_pressed, xyList)
                btn.grid(row=row+1, column=column)
                btn.bind("<Button-1>", command)
                self.button_list.append(btn)

        self.root.mainloop()
    
    def setupGui(self):
        self.btn_

    

setup = tttForGui.OnePlayerMode()
play = TTTGui(setup)

