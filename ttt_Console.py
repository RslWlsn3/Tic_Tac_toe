
class Board:
    """Sets game board up. Also can edit and then display board"""
    def __init__(self, board_size = 3):
        self.board_size = board_size
        self.create_board()
        
    def create_board(self):
        self.board = [['_' for x in range(self.board_size)] for y in range(self.board_size)]
        self.display_board()
    
    def edit_board(self, x, y, symbol):
        self.board[x][y] = symbol
    
    def display_board(self):
        for row in self.board:
            print(row)

class Gameflow:
    """Tic-tack-toe logic and gameplay"""
    def __init__(self):
        self.player_one = input("\n\nPlayer 1, X or O?")
        if self.player_one == 'x' or self.player_one == 'X':
            self.player_two = 'O'
        else:
            self.player_two = 'X'
        self.turn = 0
        self.game_board = Board()  

    def player_turn(self):
        """deside who's turn it is, ask for their move, check that it is valid"""
        valide_move = False        
        while not valide_move:
            if (self.turn % 2) == 0:
                print("Player 1:")
            else:
                print("Player 2:")
            y_move = int(input("    x move: ")) #more intuitive for player to have it x and y to be fliped
            x_move = int(input(" (-)y move: "))
            valide_move = self.validate_move(x_move,y_move)
            if valide_move:
                if (self.turn % 2) == 0:
                    self.game_board.edit_board(x_move, y_move, self.player_one)     
                else:
                    self.game_board.edit_board(x_move, y_move, self.player_two)
                self.game_board.display_board()
                self.turn +=1
            else:
                print('invalid move, try again\n\n')
                self.game_board.display_board()       
    
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
                print('X has won the game!')
                return True
            elif y_counter == 3:
                print('O has won the game!')
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
                print('X has won the game!')
                return True
            elif y_counter == 3:
                print('O has won the game!')
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
            print('X has won the game!')
            return True
        elif y_counter == 3:
            print('O has won the game!')
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
            print('X has won the game!')
            return True
        elif y_counter == 3:
            print('O has won the game!')
            return True
        else:
            return False
    
    def check_catGame(self):
        _count = 0
        for row in range(self.game_board.board_size):
            for collum in range(self.game_board.board_size):
                if self.game_board.board[row][collum] == '_':
                    _count +=1
        if _count ==0:
            print("Cat game :(")
            return True
        else:
            return False
    
    def check_for_win(self):
        if self.check_rows() or self.check_collums() or self.check_downLeft_diagonal() or self.check_upRight_diagonal() or self.check_catGame():
            return True
        else:
            return False    
    
    def play_game(self):
        """while there are no winners or catgame, continue the game"""
        winners = False
        while not winners:
            self.player_turn()
            winners = self.check_for_win()


while True:
    Game = Gameflow()
    Game.play_game()


