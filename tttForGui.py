import os
import random

class Board:
    """Sets game board up. Also can edit and then display board"""
    def __init__(self, board_size = 3):
        self.board_size = board_size
        self.create_board()
        
    def create_board(self):
        self.board = [['_' for x in range(self.board_size)] for y in range(self.board_size)]        
    
    def edit_board(self, x, y, symbol):
        self.board[x][y] = symbol  
    

class Gameflow:
    """Tic-tack-toe logic and gameplay"""
    def __init__(self):
        self.player_one = 'X'
        self.player_two = 'O'       
        self.turn = 0
        self.game_board = Board()  
        self.game_over = False
        

    def player_turn(self, x_move, y_move, game_mode):
        """deside who's turn it is, ask for their move, check that it is valid"""                
        valide_move = self.validate_move(x_move,y_move)
        if valide_move and not self.game_over:
            if (self.turn % 2) == 0 or game_mode == '1':
                self.game_board.edit_board(x_move, y_move, self.player_one)     
            else:
                self.game_board.edit_board(x_move, y_move, self.player_two)            
            self.turn +=1
            if self.check_for_win():  #check for game over                              
                return 2    #some sort of enum here would be better
            return True
        else:
            return False
                 
    
    def validate_move(self, x, y):
        try:
            if self.game_board.board[x][y] == '_':
                return True
            else:
                return False
        except:
            return False
    
    def check_rows(self):
        for row in self.game_board.board:
            X_counter = 0
            O_counter = 0
            for space in row:
                if space.title() == 'X':
                    X_counter +=1
                elif space.title() == 'O':
                    O_counter +=1
            if X_counter == 3:
                return True
            elif O_counter == 3:                
                return True
        return False
    
    def check_collums(self):
        for num in range(self.game_board.board_size):
            X_counter = 0
            O_counter = 0
            for collum in self.game_board.board:
                if collum[num].title() == 'X':
                    X_counter +=1
                elif collum[num].title() == 'O':
                    O_counter +=1
            if X_counter == 3:                
                return True
            elif O_counter == 3:                
                return True
        return False

    def check_upRight_diagonal(self):
        X_counter = 0
        O_counter = 0        
        for i in range(self.game_board.board_size):
            if self.game_board.board[i][self.game_board.board_size - 1 -i].title() == 'X':
                X_counter +=1
            elif self.game_board.board[i][self.game_board.board_size -1 -i].title() == 'O':
                O_counter +=1            
        if X_counter == 3:            
            return True
        elif O_counter == 3:            
            return True
        else:
            return False        
    
    def check_downLeft_diagonal(self):
        X_counter = 0
        O_counter = 0
        for i in range(self.game_board.board_size):            
            if self.game_board.board[i][i].title() == 'X':
                    X_counter +=1
            elif self.game_board.board[i][i].title() == 'O':
                    O_counter +=1
        if X_counter == 3:            
            return True
        elif O_counter == 3:            
            return True
        else:
            return False
    
    def check_catGame(self):    #could just check for turn == 9
        _count = 0
        for row in range(self.game_board.board_size):
            for collum in range(self.game_board.board_size):
                if self.game_board.board[row][collum] == '_':
                    _count +=1
        if _count ==0: #cat game            
            return True
        else:
            return False
    
    def check_for_win(self):
        if self.check_rows() or self.check_collums() or self.check_downLeft_diagonal() or self.check_upRight_diagonal() or self.check_catGame():
            self.game_over = True
            return True
        else:
            return False    
    
#probably don't need new class
class OnePlayerMode(Gameflow):
        
    def computer_play(self):
        self.potential_com_move = []
        move = self.com_check_rows()
        if move: #checking rows
            move.append(self.check_for_win()) 
            return move
        move = self.com_check_collums()
        if move: #checking collums
            move.append(self.check_for_win()) 
            return move
        move = self.com_check_downLeft_diagonal()
        if move: #checking diagonal
            move.append(self.check_for_win()) 
            return move
        move = self.com_check_upRight_diagonal()
        if move: #checking other diagonal
            move.append(self.check_for_win()) 
            return move
        elif self.potential_com_move:
            self.game_board.edit_board(self.potential_com_move[0], self.potential_com_move[1], self.player_two)
            return self.potential_com_move      
        else:
            move = self.Random_play()
            Gameover = self.check_for_win()
            move.append(Gameover)
            return move

    def com_check_for_space(self, potential_move, O_counter, X_counter):
        """finds the blank space location which the computer may want play"""
        if O_counter==2 and X_counter != 1:
                self.game_board.edit_board(potential_move[0], potential_move[1], self.player_two)
                potential_move.append(True) #make this move now
                return potential_move
        elif X_counter==2 and O_counter != 1:
            #self.game_board.edit_board(potential_move[0], potential_move[1], self.player_two)
            potential_move.append(False) #wait to make this move untill we see if there are any other win opertunities                
            return potential_move
        else:
            return False

    def com_check_rows(self):
        for x, row in enumerate(self.game_board.board):
            X_counter = 0
            O_counter = 0            
            potential_move = []
            com_move = []           #I can make this simplier, should redue some logic----------------------------------
            for y, space in enumerate(row):
                if space.title() == 'X':
                    X_counter +=1
                elif space.title() == 'O':
                    O_counter +=1
                else:
                    potential_move = [x,y]
            if X_counter == 2 or O_counter == 2:           
                com_move = self.com_check_for_space(potential_move, O_counter, X_counter) 
            if com_move:
                if com_move[2] == True:
                    return com_move #win game if possible
                else:
                    self.potential_com_move = com_move #store block to play if there are no other win opurtunities
        return False
    
    def com_check_collums(self):
        for y in range(self.game_board.board_size):
            X_counter = 0
            O_counter = 0
            potential_move = []
            com_move = []
            for x, collum in enumerate(self.game_board.board):
                if collum[y].title() == 'X':
                    X_counter +=1
                elif collum[y].title() == 'O':
                    O_counter +=1
                else:
                    potential_move = [x,y]
            if X_counter ==2 or O_counter == 2:
                com_move = self.com_check_for_space(potential_move, O_counter, X_counter) 
            if com_move:
                if com_move[2] == True:
                    return com_move
                else:
                    self.potential_com_move = com_move
        return False
    
    def com_check_upRight_diagonal(self):
        X_counter = 0
        O_counter = 0
        potential_move = []
        com_move = []        
        for x in range(self.game_board.board_size):
            y = self.game_board.board_size - 1 - x
            if self.game_board.board[x][y].title() == 'X':
                X_counter +=1
            elif self.game_board.board[x][y].title() == 'O':
                O_counter +=1 
            else: 
                potential_move = [x,y]          
        if X_counter ==2 or O_counter == 2:
                com_move = self.com_check_for_space(potential_move, O_counter, X_counter) 
        if com_move:
            if com_move[2] == True:
                    return com_move
            else:
                self.potential_com_move = com_move
        return False    
    
    def com_check_downLeft_diagonal(self):
        X_counter = 0
        O_counter = 0
        potential_move = []
        com_move = []
        for x in range(self.game_board.board_size):
            y = x            
            if self.game_board.board[x][y].title() == 'X':
                X_counter +=1
            elif self.game_board.board[x][y].title() == 'O':
                O_counter +=1
            else:
                potential_move = [x,y]
        if X_counter ==2 or O_counter == 2:
                com_move = self.com_check_for_space(potential_move, O_counter, X_counter) 
        if com_move:
            if com_move[2] == True:
                    return com_move
            else:
                self.potential_com_move = com_move
        return False 
    
    def Random_play(self):
        x = random.randrange(3)    
        y = random.randrange(3)    
        while not self.validate_move(x, y): #recurtoin wasn't working here
            x = random.randrange(3)    
            y = random.randrange(3)    
        else:
            self.game_board.edit_board(x, y, self.player_two)            
            xyList = [x,y]
            return xyList
    
    


# go = OnePlayerMode()
# go.Random_play()

#will prioitize a row block over a collumn win

