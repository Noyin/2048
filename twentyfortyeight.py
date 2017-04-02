from tile import Tile
import random


class Game:
    def __init__(self,boardsize=4):

        """

        :param boardsize: represents the size of the board. default set to 4
        :variable state: represents current state of the game
        :variable board: a list representing the game board with location set to 0
        :variable array: a list to containing 2's (90% probability) and 4's (10% probability)

        """


        self.state = "Play"
        self.boardsize = boardsize
        self.board = [[0 for row in range(self.boardsize)] for column in range(self.boardsize)]
        self.array = []
        self.array += [2] * 90
        self.array += [4] * 10
        random.shuffle(self.array)

    def __insert_tile(self,number=2):

        """
        :param number: number of tiles to insert into board
        :variable board: a list representing the game board.method inserts tiles into board

        """

        number_of_tiles_set = 0
        while number_of_tiles_set < number:
            row = random.randint(0, self.boardsize-1)
            column = random.randint(0, self.boardsize-1)
            if self.board[row][column] == 0:
                self.board[row][column] = Tile(value=self.array[random.randint(0, 100-1)])
                number_of_tiles_set += 1



    def update_state(self):

        """
        :method: updates state of the game

        """

        count = 0
        for row in range(0, self.boardsize):
            for column in range(0,self.boardsize):
                if self.board[row][column] != 0:
                    if self.board[row][column].value == 2048:
                        self.state = "Won"
                        break
                    count += 1

            if self.state == "Won":
                print("Game Won")
                break
        if count == (self.boardsize * self.boardsize):
            self.state = "Lost"
            print("Game Lost")


    def start(self):

        """
        :method: inserts two tiles into board

        """
        self.__insert_tile()

    def add_tile(self):

        """
        :method: inserts one tile into board

        """

        self.__insert_tile(number=1)


    def move_up(self):
        """
        :method: moves tiles up and merges tiles if they have the same value.

        """
        self.clear_merge()
        if self.state == "Play":
            for row in range(0, self.boardsize):
                for column in range(0,self.boardsize):
                    next_row = row - 1
                    if 0 <= next_row <= self.boardsize - 1:
                        if self.board[row][column] != 0 and self.board[next_row][column] == 0:
                            previous_row = row
                            while (0 <= next_row <= self.boardsize - 1) and self.board[next_row][column] == 0:
                                self.board[next_row][column] = self.board[previous_row][column]
                                self.board[previous_row][column] = 0
                                if 0 < next_row:
                                    previous_row = next_row
                                    next_row -= 1

                                if self.board[previous_row][column] != 0 and self.board[next_row][column] != 0 and self.board[next_row][column].merged == False:
                                    if self.board[previous_row][column].value == self.board[next_row][column].value:
                                        self.board[next_row][column].value += self.board[previous_row][column].value
                                        self.board[previous_row][column] = 0

                        if self.board[row][column] != 0 and self.board[next_row][column] != 0 and self.board[next_row][column].merged == False:
                            if self.board[row][column].value == self.board[next_row][column].value:
                                self.board[next_row][column].value += self.board[row][column].value
                                self.board[row][column] = 0

            self.update_state()


    def move_down(self):
        """
        :method: moves tiles down and merges tiles if they have the same value.

        """

        self.clear_merge()
        if self.state == "Play":
            for row in range(self.boardsize-1, -1,-1):
                for column in range(0, self.boardsize):
                    next_row = row + 1

                    if 0 <= next_row <= self.boardsize - 1:
                        if self.board[row][column] != 0 and self.board[next_row][column] == 0:
                            previous_row = row
                            while (0 <= next_row <= self.boardsize-1) and self.board[next_row][column] == 0:
                                self.board[next_row][column] = self.board[previous_row][column]
                                self.board[previous_row][column] = 0

                                if next_row < self.boardsize -1:
                                    previous_row = next_row
                                    next_row += 1

                                if self.board[previous_row][column] != 0 and self.board[next_row][column] != 0 and self.board[next_row][column].merged == False:
                                    if self.board[previous_row][column].value == self.board[next_row][column].value:
                                        self.board[next_row][column].value += self.board[previous_row][column].value
                                        self.board[next_row][column].merged = True
                                        self.board[previous_row][column] = 0

                        if self.board[row][column] != 0 and self.board[next_row][column] != 0 and self.board[next_row][column].merged == False:
                            if self.board[row][column].value == self.board[next_row][column].value:
                                self.board[next_row][column].value += self.board[row][column].value
                                self.board[next_row][column].merged = True
                                self.board[row][column] = 0

            self.update_state()



    def move_left(self):
        """
        :method: moves tiles to the left and merges tiles if they have the same value.

        """
        self.clear_merge()
        if self.state == "Play":
            for row in range(0, self.boardsize):
                for column in range(0, self.boardsize):
                    next_column = column - 1

                    if 0 <= next_column <= self.boardsize - 1:
                        if self.board[row][column] != 0 and self.board[row][next_column] == 0:
                            previous_column = column
                            while (0 <= next_column <= self.boardsize-1) and self.board[row][next_column] == 0:
                                self.board[row][next_column] = self.board[row][previous_column]
                                self.board[row][previous_column] = 0

                                if next_column < self.boardsize -1:
                                    previous_column = next_column
                                    next_column -= 1

                                if self.board[row][previous_column] != 0 and self.board[row][next_column] != 0 and self.board[row][next_column].merged == False:

                                    if self.board[row][previous_column].value == self.board[row][next_column].value:
                                        self.board[row][next_column].value += self.board[row][previous_column].value
                                        self.board[row][next_column].merged = True
                                        self.board[row][previous_column] = 0


                        if self.board[row][column] != 0 and self.board[row][next_column] != 0 and self.board[row][next_column].merged == False:

                            if self.board[row][column].value == self.board[row][next_column].value:
                                self.board[row][next_column].value += self.board[row][column].value
                                self.board[row][next_column].merged = True
                                self.board[row][column] = 0

            self.update_state()


    def move_right(self):
        """
        :method: moves tiles to the right and merges tiles if they have the same value.

        """
        self.clear_merge()
        if self.state == "Play":
            for row in range(0, self.boardsize):
                for column in range(self.boardsize-1, -1, -1):
                    next_column = column + 1

                    if 0 <= next_column <= self.boardsize - 1:
                        if self.board[row][column] != 0 and self.board[row][next_column] == 0:
                            previous_column = column
                            while (0 <= next_column <= self.boardsize - 1) and self.board[row][next_column] == 0:
                                self.board[row][next_column] = self.board[row][previous_column]
                                self.board[row][previous_column] = 0

                                if next_column < self.boardsize - 1:
                                    previous_column = next_column
                                    next_column += 1


                                if self.board[row][previous_column] != 0 and self.board[row][next_column] != 0 and self.board[row][next_column].merged == False:
                                    if self.board[row][previous_column].value == self.board[row][next_column].value:
                                        self.board[row][next_column].value += self.board[row][previous_column].value
                                        self.board[row][next_column].merged = True
                                        self.board[row][previous_column] = 0

                        if self.board[row][column] != 0 and self.board[row][next_column] != 0 and self.board[row][next_column].merged == False:

                            if self.board[row][column].value == self.board[row][next_column].value:
                                self.board[row][next_column].value += self.board[row][column].value
                                self.board[row][next_column].merged = True
                                self.board[row][column] = 0

            self.update_state()


    def clear_merge(self):
        """
        :method: negates all tile's "merged" property in board

        """
        for row in range(0, self.boardsize):
            for column in range(0, self.boardsize):
                if self.board[row][column] != 0:
                    self.board[row][column].merged = False

    def print_board(self):
        """
        :method: prints board

        """
        board = []
        for row in range(0, self.boardsize):
            for column in range(0, self.boardsize):
                if self.board[row][column] != 0:
                    board.append(self.board[row][column].value)
                else:
                    board.append(self.board[row][column])
        print(board)
