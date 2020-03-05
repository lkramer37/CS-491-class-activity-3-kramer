import unittest
import tic_tac_toe


class MyTestCase(unittest.TestCase):
    # Tests for Player Class
    def test_switch_player(self):
        player = tic_tac_toe.Player()
        player.current_player = 'X'
        player.switch_player()

        self.assertEqual(player.current_player, 'O')
        player.switch_player()
        self.assertEqual(player.current_player, 'X')

    # Tests for Board Class
    def test_print_board(self):
        pass

    def test_mark_square(self):
        board = tic_tac_toe.Board()

        board.index = 0
        board.current_player = 'X'
        board.mark_square()
        self.assertEqual(board.boardArr[0], 'X')

    def test_check_if_marked(self):
        board = tic_tac_toe.Board()
        board.index = 0
        board.boardArr[0] = 'X'
        self.assertTrue(board.check_if_marked())
        board.index = 8
        self.assertFalse(board.check_if_marked())

    def test_check_if_full(self):
        board = tic_tac_toe.Board()
        board.print_board()
        self.assertFalse(board.check_if_full())

        for x in range(9):
            board.boardArr[x] = '0'
        self.assertTrue(board.check_if_full())

    def test_matching_row(self):
        board1 = tic_tac_toe.Board()
        board1.boardArr[0] = '0'
        board1.boardArr[1] = '0'
        board1.boardArr[2] = '0'
        self.assertTrue(board1.matching_row('0'))

        board_no_match = tic_tac_toe.Board()
        self.assertFalse(board_no_match.matching_row('X'))
        self.assertFalse(board_no_match.matching_row('O'))

    def test_matching_col(self):
        board1 = tic_tac_toe.Board()
        board1.boardArr[0] = 'X'
        board1.boardArr[3] = 'X'
        board1.boardArr[6] = 'X'
        self.assertTrue(board1.matching_col('X'))

        board_no_match = tic_tac_toe.Board()
        self.assertFalse(board_no_match.matching_col('X'))
        self.assertFalse(board_no_match.matching_col('O'))

    def test_matching_diag(self):
        board1 = tic_tac_toe.Board()
        board1.boardArr[0] = 'X'
        board1.boardArr[4] = 'X'
        board1.boardArr[8] = 'X'
        self.assertTrue(board1.matching_diag('X'))

        board2 = tic_tac_toe.Board()
        board2.boardArr[2] = 'X'
        board2.boardArr[4] = 'X'
        board2.boardArr[6] = 'X'
        self.assertTrue(board2.matching_diag('X'))

        board_no_match = tic_tac_toe.Board()
        self.assertFalse(board_no_match.matching_diag('X'))
        self.assertFalse(board_no_match.matching_diag('O'))

    # Tests for Game Class
    def test_get_board_index(self):
        game = tic_tac_toe.Game()
        game.get_board_index(2, 2)
        self.assertEqual(game.index, 4)

    def test_get_player_move(self):
        # Not testing I/O
        pass

    def test_check_for_winner(self):
        game = tic_tac_toe.Game()
        player = 'X'
        self.assertFalse(game.check_for_winner(player))

    def test_play(self):
        pass

    # Other Tests
    def test_out_of_bounds(self):
        pass

    def test_board_full(self):
        pass

    # ARRANGE
    # ACT
    # ASSERT


if __name__ == '__main__':
    unittest.main()
