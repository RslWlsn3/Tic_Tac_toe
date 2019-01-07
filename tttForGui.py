import os

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

    def player_turn(self, x_move, y_move):
        """deside who's turn it is, ask for their move, check that it is valid"""                
        valide_move = self.validate_move(x_move,y_move)
        if valide_move and not self.game_over:
            if (self.turn % 2) == 0:
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
            x_counter = 0
            y_counter = 0
            for space in row:
                if space.title() == 'X':
                    x_counter +=1
                elif space.title() == 'O':
                    y_counter +=1
            if x_counter == 3:
                return True
            elif y_counter == 3:                
                return True
        return False
    
    def check_collums(self):
        for num in range(self.game_board.board_size):
            x_counter = 0
            y_counter = 0
            for collum in self.game_board.board:
                if collum[num].title() == 'X':
                    x_counter +=1
                elif collum[num].title() == 'O':
                    y_counter +=1
            if x_counter == 3:                
                return True
            elif y_counter == 3:                
                return True
        return False

    def check_upRight_diagonal(self):
        x_counter = 0
        y_counter = 0        
        for i in range(self.game_board.board_size):
            if self.game_board.board[i][self.game_board.board_size - 1 -i].title() == 'X':
                x_counter +=1
            elif self.game_board.board[i][self.game_board.board_size -1 -i].title() == 'O':
                y_counter +=1            
        if x_counter == 3:            
            return True
        elif y_counter == 3:            
            return True
        else:
            return False        
    
    def check_downLeft_diagonal(self):
        x_counter = 0
        y_counter = 0
        for i in range(self.game_board.board_size):            
            if self.game_board.board[i][i].title() == 'X':
                    x_counter +=1
            elif self.game_board.board[i][i].title() == 'O':
                    y_counter +=1
        if x_counter == 3:            
            return True
        elif y_counter == 3:            
            return True
        else:
            return False
    
    def check_catGame(self):
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
    
    




