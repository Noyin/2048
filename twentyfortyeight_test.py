from twentyfortyeight import Game
from tile import Tile
import unittest


class TestTwentyFortyEight(unittest.TestCase):

    def test_initialization(self):
        print("\nTesting game initialization...")

        game = Game(boardsize=4)

        self.assertEqual(game.state,"Play","Game state is not set to Play - Failed")
        self.assertEqual(game.boardsize, 4, "Game board size is incorrect - Failed")

        print("Game succesfully initialized - Ok")

    def test_move_up(self):
        print("\nTesting move up...")

        game = Game(boardsize=4)

        game.board[0][0] = Tile(value=2)
        game.board[0][1] = Tile(value=2)
        game.board[0][3] = Tile(value=2)
        game.board[1][0] = Tile(value=4)
        game.board[1][1] = Tile(value=2)
        game.board[1][2] = Tile(value=4)
        game.board[1][3] = Tile(value=4)

        game.move_up()

        self.assertEqual(game.board[0][0].value, 2,
                         "Tile at position ({},{}) has value of {} instead of 2 - Failed".format(0, 0, game.board[0][
                             0].value))
        self.assertEqual(game.board[0][1].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(0, 1, game.board[0][
                             1].value))
        self.assertEqual(game.board[0][2].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(0, 2, game.board[0][
                             2].value))
        self.assertEqual(game.board[0][3].value, 2,
                         "Tile at position ({},{}) has value of {} instead of 2 - Failed".format(0, 3, game.board[1][
                             3].value))
        self.assertEqual(game.board[1][0].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(1, 0, game.board[1][
                             0].value))
        self.assertEqual(game.board[1][3].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(1, 3, game.board[1][
                             3].value))


        print("move up successful - Ok")


    def test_move_down(self):
        print("\nTesting move down...")

        game = Game(boardsize=4)

        game.board[0][0] = Tile(value=2)
        game.board[0][1] = Tile(value=2)
        game.board[0][3] = Tile(value=2)
        game.board[1][0] = Tile(value=4)
        game.board[1][1] = Tile(value=2)
        game.board[1][2] = Tile(value=4)
        game.board[1][3] = Tile(value=4)

        game.move_down()

        self.assertEqual(game.board[2][0].value, 2,
                         "Tile at position ({},{}) has value of {} instead of 2 - Failed".format(2, 0, game.board[2][
                             0].value))
        self.assertEqual(game.board[2][3].value, 2,
                         "Tile at position ({},{}) has value of {} instead of 2 - Failed".format(2, 3, game.board[2][
                             3].value))
        self.assertEqual(game.board[3][0].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(3, 0, game.board[3][
                             0].value))
        self.assertEqual(game.board[3][1].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(3, 1, game.board[3][
                             1].value))
        self.assertEqual(game.board[3][2].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(3, 2, game.board[3][
                             2].value))
        self.assertEqual(game.board[3][3].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(3, 3, game.board[3][
                             3].value))

        print("move down successful - Ok")


    def test_move_left(self):
        print("\nTesting move left...")

        game = Game(boardsize=4)

        game.board[0][0] = Tile(value=2)
        game.board[0][1] = Tile(value=2)
        game.board[0][3] = Tile(value=4)
        game.board[1][0] = Tile(value=4)
        game.board[1][1] = Tile(value=2)
        game.board[1][2] = Tile(value=4)
        game.board[1][3] = Tile(value=4)
        game.board[2][0] = Tile(value=2)
        game.board[2][1] = Tile(value=2)
        game.board[2][3] = Tile(value=2)

        game.move_left()

        self.assertEqual(game.board[0][0].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(0,0,game.board[0][0].value))
        self.assertEqual(game.board[0][1].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(0,1,game.board[0][1].value))
        self.assertEqual(game.board[1][0].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(1,0,game.board[1][0].value))
        self.assertEqual(game.board[1][1].value, 2,
                         "Tile at position ({},{}) has value of {} instead of 2 - Failed".format(1,1,game.board[1][1].value))
        self.assertEqual(game.board[1][2].value, 8,
                         "Tile at position ({},{}) has value of {} instead of 8 - Failed".format(1,2,game.board[1][2].value))
        self.assertEqual(game.board[2][0].value, 4,
                         "Tile at position ({},{}) has value of {} instead of 4 - Failed".format(2,0,game.board[2][0].value))
        self.assertEqual(game.board[2][1].value, 2,
                         "Tile at position ({},{}) has value of {} instead of 2 - Failed".format(2,1,game.board[2][1].value))

        print("move left successful - Ok")

    def test_move_right(self):
        print("\nTesting move right..")

        game = Game(boardsize=4)

        game.board[0][0] = Tile(value=4)
        game.board[0][1] = Tile(value=2)
        game.board[0][3] = Tile(value=2)
        game.board[1][0] = Tile(value=4)
        game.board[1][1] = Tile(value=2)
        game.board[1][2] = Tile(value=4)
        game.board[1][3] = Tile(value=4)
        game.board[2][0] = Tile(value=2)
        game.board[2][1] = Tile(value=2)
        game.board[2][3] = Tile(value=2)

        game.move_right()


        self.assertEqual(game.board[0][2].value, 4,"Tile at position ({},{}) has value of {} instead of 4 - Failed".format(0, 2, game.board[0][2].value))
        self.assertEqual(game.board[0][3].value, 4,"Tile at position ({},{}) has value of {} instead of 4 - Failed".format(0, 3, game.board[0][3].value))
        self.assertEqual(game.board[1][1].value, 4,"Tile at position ({},{}) has value of {} instead of 4 - Failed".format(1, 1, game.board[1][1].value))
        self.assertEqual(game.board[1][2].value, 2,"Tile at position ({},{}) has value of {} instead of 2 - Failed".format(1, 2, game.board[1][2].value))
        self.assertEqual(game.board[1][3].value, 8,"Tile at position ({},{}) has value of {} instead of 8 - Failed".format(1, 3, game.board[1][3].value))
        self.assertEqual(game.board[2][2].value, 2,"Tile at position ({},{}) has value of {} instead of 2 - Failed".format(2, 2, game.board[2][2].value))
        self.assertEqual(game.board[2][3].value, 4,"Tile at position ({},{}) has value of {} instead of 4 - Failed".format(2, 3, game.board[2][3].value))

        print("move right successful - Ok")

    def test_insert_tile_after_initialization(self):

        print("\nTesting number of inserted tiles after game initialized...")

        game = Game(boardsize=4)
        game.start()

        count = 0

        for row in range(game.boardsize):
            for column in range(game.boardsize):
                if game.board[row][column] != 0:
                    count += 1
        self.assertEqual(count,2,"Incorrect number of tiles inserted- {} tile(s) inserted instead of 2".format(count))
        print("Inserted 2 tiles successfully - Ok")

    def test_insert_tile_during_gameplay(self):

        print("\nTesting number of inserted tile during game play...")

        game = Game(boardsize=4)
        game.start()
        game.add_tile()

        count = 0

        for row in range(game.boardsize):
            for column in range(game.boardsize):
                if game.board[row][column] != 0:
                    count += 1

        self.assertEqual(count, 3, "Incorrect number of tiles inserted- {} tile(s) inserted instead of 3".format(count))
        print("Inserted 1 tile successfully - Ok")

    def test_win_state(self):

        print("\nTesting win state...")

        game = Game(boardsize=4)

        game.board[0][0] = Tile(value=2048)
        game.board[1][0] = Tile(value=32)
        game.board[1][1] = Tile(value=32)
        game.board[2][0] = Tile(value=2)
        game.board[2][1] = Tile(value=64)
        game.board[2][2] = Tile(value=128)
        game.board[2][3] = Tile(value=2)
        game.board[3][0] = Tile(value=4)
        game.board[3][1] = Tile(value=8)
        game.board[3][2] = Tile(value=2)
        game.board[3][3] = Tile(value=4)

        game.update_state()

        self.assertEqual(game.state,"Won","Incorrect game state - current game state is {}".format(game.state))
        print("Successfully tested game win state - Ok")

    def test_loss_state(self):

        print("\nTesting lost state...")

        game = Game(boardsize=4)

        game.board[0][0] = Tile(value=4)
        game.board[0][1] = Tile(value=2)
        game.board[0][2] = Tile(value=8)
        game.board[0][3] = Tile(value=16)
        game.board[1][0] = Tile(value=32)
        game.board[1][1] = Tile(value=32)
        game.board[1][2] = Tile(value=256)
        game.board[1][3] = Tile(value=512)
        game.board[2][0] = Tile(value=2)
        game.board[2][1] = Tile(value=64)
        game.board[2][2] = Tile(value=128)
        game.board[2][3] = Tile(value=2)
        game.board[3][0] = Tile(value=4)
        game.board[3][1] = Tile(value=8)
        game.board[3][2] = Tile(value=2)
        game.board[3][3] = Tile(value=4)

        game.update_state()

        self.assertEqual(game.state, "Lost", "Incorrect game state - current game state is {}".format(game.state))

        print("Successfully tested game lost state - Ok")


if __name__ == '__main__':
    unittest.main()