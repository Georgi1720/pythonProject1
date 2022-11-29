class TicTacToeBoard:
    count = 0
        
    def __init__(self):
        self.board  = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.game_over = 0
        self.winner = ''

    def new_game(self):
        self.board  = [['-','-','-'],['-','-','-'],['-','-','-']]
        self.game_over = 0
        self.winner = ''


    def get_field(self):
        print(*self.board,sep='\n')
 
        
    def chek_field(self):
        if self.winner == 'x': print('x') 
        elif self.winner == 'o': print ('o')
        elif '-' not in self.board[0] and '-' not in self.board[1] and '-' not in self.board[2]: print('D') 
        else: print(None) 
        

    def make_move(self, row,col):
        self.count += 1
        if self.game_over == 5:
            print(f'Игра уже завершена,победил игрок {self.winner}')
        else:
            if self.board[row-1][col-1] != '-':
                self.count -= 1
                print('клетка уже занята' )  
            else:
                if self.count % 2 != 0:
                    self.board[row-1][col-1] = 'x' 
                    print("Игра продолжается")
                else:
                    self.board[row-1][col-1] = 'o' 
                    print("Игра продолжается" )    
            if self.board[0].count(self.board[0][0]) == 3 and self.board[0][0] != '-':
                self.game_over = 5
                self.winner = self.board[0][0]
            elif self.board[1].count(self.board[1][0]) == 3 and self.board[1][0]!= '-':
                self.game_over = 5
                self.winner = self.board[1][0]
            elif self.board[2].count(self.board[2][0]) == 3 and self.board[2][0] != '-':
                self.game_over = 5
                self.winner = self.board[2][0]
            elif self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != '-':
                self.game_over = 5
                self.winner = self.board[0][0]
            elif self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != '-':
                self.game_over = 5
                self.winner = self.board[0][1]
            elif self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != '-':
                self.game_over = 5
                self.winner = self.board[0][2]
            elif self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '-':
                self.game_over = 5
                self.winner = self.board[0][0]
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '-':
                self.game_over = 5
                self.winner = self.board[0][2]


board = TicTacToeBoard()
board.get_field()
board.make_move(1, 1)
board.get_field()
board.make_move(1, 1)
board.make_move(1, 2)
board.get_field()
board.make_move(2, 1)
board.make_move(2, 2)
board.get_field()
board.make_move(3, 1)
board.make_move(2, 2)
board.get_field()
