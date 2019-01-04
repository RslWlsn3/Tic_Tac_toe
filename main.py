
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
    """sets up payer's symbol, desides who's turn it is, then gets their move"""
    def __init__(self, game_board):
        self.player_one = input("Player 1, X or O?")
        if self.player_one == 'x' or self.player_one == 'X':
            self.player_two = 'O'
        else:
            self.player_two = 'X'
        self.turn = 0
        self.game_board = game_board
    
    def player_turn(self):
        valide_move = False
        #self.game_board.display_board()
        while not valide_move:
            if (self.turn % 2) == 0:
                x_move = int(input("Player one x move: "))
                y_move = int(input("y move: "))
                valide_move = self.validate_move(x_move,y_move)
                if valide_move:
                    self.game_board.edit_board(x_move, y_move, self.player_one)     #reapting code in here, may want to break up further
                    self.game_board.display_board()
                    self.turn +=1
                else:
                    print('invalid move, try again')
                    self.game_board.display_board()
            else:
                x_move = int(input("Player two x move: "))
                y_move = int(input("y move: "))
                valide_move = self.validate_move(x_move,y_move)
                if valide_move:
                    self.game_board.edit_board(x_move, y_move, self.player_two)
                    self.game_board.display_board()
                    self.turn += 1
                else:
                    print('invalid move, try again')
                    self.game_board.display_board()
    
    def validate_move(self, x, y):
        try:
            if self.game_board.board[x][y] == '_':
                return True
            else:
                return False
        except:
            return False

    def check_for_win(self):
        #check rows
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
        #check collums
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
        #check left diagonal
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
        #check right diagonal
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
        #check cat game
        _count = 0
        for row in range(self.game_board.board_size):
            for collum in range(self.game_board.board_size):
                if self.game_board.board[row][collum] == '_':
                    _count +=1
        if _count ==0:
            print("Cat game :(")
            return True

        #no winner or catgame so don't stop the game
        return False
    
    def play_game(self):
        winners = False
        while not winners:
            self.player_turn()
            winners = self.check_for_win()


tttBoard = Board()
Game = Gameflow(tttBoard)
Game.check_for_win()
Game.play_game()


