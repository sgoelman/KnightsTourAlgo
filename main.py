from heapq import heappush, heappop  # for priority queue
import random


class KnightAlgo:
    def __init__(self):
        self.board_x = 8
        self.board_y = 8
        self.chess_board = [[0 for x in range(self.board_x)] for y in range(self.board_y)]  # chessboard
        # moves available  in each direction
        self.direction_x = [-2, -1, 1, 2, -2, -1, 1, 2]
        self.direction_y = [1, 2, 2, 1, -1, -2, -2, -1]
        # starting at a random position
        self.knight_x = random.randint(0, self.board_x - 1)
        self.knight_y = random.randint(0, self.board_y - 1)

        print("Knight's starting position X:" + str(self.knight_x) + " Y:" + str(self.knight_y))

    def algo(self):
        for k in range(self.board_x * self.board_y):
            self.chess_board[self.knight_y][self.knight_x] = k + 1
            queue = []  # queue of available neighbors
            for i in range(8):
                next_x = self.knight_x + self.direction_x[i]
                next_y = self.knight_y + self.direction_y[i]

                if 0 <= next_x and next_x < self.board_x:
                    if 0 <= next_y and next_y < self.board_y:
                        if self.chess_board[next_y][next_x] == 0:
                            # count the available neighbors of the neighbor
                            neighbours_count = 0
                            for j in range(8):
                                ex = next_x + self.direction_x[j]
                                ey = next_y + self.direction_y[j]
                                if 0 <= ex < self.board_x and 0 <= ey < self.board_y:
                                    if self.chess_board[ey][ex] == 0:
                                        neighbours_count += 1
                            heappush(queue, (neighbours_count, i))
            # move to the neighbor that has min available places
            if len(queue) > 0:
                (p, m) = heappop(queue)
                self.knight_x += self.direction_x[m]
                self.knight_y += self.direction_y[m]
            else:
                break

    def printBoard(self):
        print(str(self.chess_board))

    def testAlgo(self):
        if self.chess_board.__contains__(63):
            print("63")
        if self.chess_board.__contains__(0):
            print("not  all places where travelled ")
        else:
            print("success all places where travelled ")

        # make sure all places where travelled
        #  make sure that there are 63  steps


def runKightAlgo():
    knightAlgo = KnightAlgo()
    knightAlgo.algo()
    knightAlgo.printBoard()
    knightAlgo.testAlgo()


if __name__ == "__main__":
    runKightAlgo()
