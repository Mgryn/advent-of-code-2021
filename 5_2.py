import numpy as np

class LineCounter:
    def __init__(self):
        self.path = 'data/5.txt'
        self.p1, self.p2 = self.load_data()
        self.board = self.create_board()
        self.board = self.calculate(self.board)

    def load_data(self):
        with open(self.path, 'r') as f:
            data = (x.replace(' -> ', ',') for x in f)
            A = np.loadtxt(data, dtype=int, delimiter=',')
            p1 = A[:, :2]
            p2 = A[:, 2:4]
        return p1, p2

    def create_board(self):
        x_max = np.max(np.concatenate((self.p1[:, 0], self.p2[:, 0]), axis=0))
        y_max = np.max(np.concatenate((self.p1[:, 1], self.p2[:, 1]), axis=0))
        board = np.zeros((x_max, y_max))
        return board
        
    def calculate(self, board):
        for (a, b) in zip(self.p1, self.p2):

            if a[0]==b[0] or a[1]==b[1]:
                points = self.get_line_points(a, b)
            else: 
                points = self.get_diagonal(a, b)

            for point in points:
                board[point[0], point[1]] += 1
                
        print('Result: ', board[board>=2].shape)
                
    def get_line_points(self, p1, p2):
        x_max, x_min = max(p1[0], p2[0]), min(p1[0], p2[0])
        y_max, y_min = max(p1[1], p2[1]), min(p1[1], p2[1])
        points = [(x, y) for x in range(x_min-1, x_max) for y in range(y_min-1, y_max)]
        return points

    def get_diagonal(self, p1, p2):
        xrange = np.linspace(p1[0]-1, p2[0]-1, abs(p1[0]-p2[0])+1)
        yrange = np.linspace(p1[1]-1, p2[1]-1, abs(p1[1]-p2[1])+1)
        points = [(int(x), int(y)) for (x, y) in zip(xrange, yrange)]
        return points

L = LineCounter()
