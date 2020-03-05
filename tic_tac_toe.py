
class Player(object):
    def __init__(self):
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


class Board(Player):

    def __init__(self):
        super().__init__()
        self.col = -1
        self.row = -1
        self.index = -1
        self.boardArr = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

    def print_board(self):
        print(" ")
        print(self.boardArr[0] + self.boardArr[1] + self.boardArr[2])
        print(self.boardArr[3] + self.boardArr[4] + self.boardArr[5])
        print(self.boardArr[6] + self.boardArr[7] + self.boardArr[8])

    def mark_square(self):
        #if(index>8):
        self.boardArr[self.index] = self.current_player

    def check_if_marked(self):
        if self.boardArr[self.index] == 'X' or self.boardArr[self.index] == 'O':
            print("That spot is taken, try again player " + self.current_player)
            return 1
        else:
            return 0

    def check_if_full(self):
        count = 0

        for x in self.boardArr:
            count += 1
            if x == "_":
                break

        if count < 9:
            return False
        elif count == 9:
            return True

    def matching_row(self, player):
        if self.boardArr[0] == player and self.boardArr[1] == player and self.boardArr[2] == player:
            return 1
        if self.boardArr[3] == player and self.boardArr[4] == player and self.boardArr[5] == player:
            return 1
        if self.boardArr[6] == player and self.boardArr[7] == player and self.boardArr[8] == player:
            return 1
        else:
            return 0

    def matching_col(self, player):
        if self.boardArr[0] == player and self.boardArr[3] == player and self.boardArr[6] == player:
            return 1
        if self.boardArr[1] == player and self.boardArr[4] == player and self.boardArr[7] == player:
            return 1
        if self.boardArr[2] == player and self.boardArr[5] == player and self.boardArr[8] == player:
            return 1
        else:
            return 0

    def matching_diag(self, player):
        if self.boardArr[0] == player and self.boardArr[4] == player and self.boardArr[8] == player:
            return 1
        elif self.boardArr[2] == player and self.boardArr[4] == player and self.boardArr[6] == player:
            return 1
        else:
            return 0


class Game(Board):
    def __init__(self):
        super().__init__()

    def get_board_index(self, row_str, col_str):
        self.col = int(col_str)
        self.row = int(row_str)
        self.row -= 1
        self.col -= 1
        self.index = self.row * 3 + self.col

    def get_player_move(self):
        print("Player " + game.current_player + "'s move")
        row, col = input("Enter row, col: ").split(',')
        self.get_board_index(row, col)

    def check_for_winner(self, player):
        if self.matching_row(player):
            return 1
        elif self.matching_col(player):
            return 1
        elif self.matching_diag(player):
            return 1
        else:
            return 0

    def play(self):
        self.print_board()
        self.switch_player()
        self.get_player_move()
        while self.check_if_marked():
            self.get_player_move()
        self.mark_square()
        self.check_if_full()


if __name__ == '__main__':
    game = Game()
    while not game.check_for_winner(game.current_player):
        game.play()
    winner = game.current_player
    print("{} has won!".format(winner))
    game.print_board()
