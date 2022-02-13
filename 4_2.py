import numpy as np
import operator
from functools import reduce

class Bingo:
    def __init__(self):
        self.file = 'data/4.txt'
        self.load_data()
        self.won = False
        self.wins = 0
        self.losing_boards = [i for i in range(100)]
        self.run()
        
    def load_data(self):
        self.numbers = np.loadtxt(self.file, dtype=int, delimiter=',', max_rows=1)
        tabs = np.loadtxt(self.file, dtype=int, skiprows=2)
        self.board_nr = len(tabs) // 5
        self.boards = [tabs[i*5:i*5+5, :] for i in range(self.board_nr)]
        self.board_bool = [np.full(board.shape, False, dtype=bool) for board in self.boards]

    def check_win_cond(self, board):
        for i in range(5):
            if reduce(operator.and_, board[i, :]) or reduce(operator.and_, board[:, i]):
                return True
        return False

    def find_score(self, number, board, board_bool):
        unmarked = board[board_bool == False]
        suma = sum(unmarked)
        return number * suma

    def run(self):
        picked_numbers = []
        temp_losing_boards = []

        for number in self.numbers:
            picked_numbers.append(number)

            for ind in self.losing_boards:
                result = np.where(self.boards[ind] == number)
                self.board_bool[ind][result[0], result[1]] = True
                self.won = self.check_win_cond(self.board_bool[ind])

                if self.won:
                    if self.wins == 99:
                        print('picked_numbers: ', picked_numbers)
                        result = self.find_score(number, self.boards[ind], self.board_bool[ind])
                        print('Riddle result: ',result)

                    self.wins += 1 
                    temp_losing_boards.append(ind)

            self.losing_boards = [x for x in self.losing_boards if x not in temp_losing_boards]
            temp_losing_boards = []
            
bingo = Bingo()
