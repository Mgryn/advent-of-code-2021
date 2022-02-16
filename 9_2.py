import numpy as np

class Cave:
    def __init__(self):
        self.data = self.get_data()
        self.explored = np.zeros(self.data.shape, dtype=int)
        self.basins = []
        self.basin_size = 0

        shape = self.data.shape

        for x in range(shape[0]):
            for y in range(shape[1]):
                bs = self.explore((x, y), shape)
                if bs > 0:
                    self.basins.append(bs)

        self.basins = sorted(self.basins)    
        print('Result: ', self.basins[-3]*self.basins[-2]*self.basins[-1])

    def explore(self, point, dims):

        if self.explored[point]:
            return 0
        self.explored[point] = 1

        if self.data[point] == 9:
            return 0

        basin_size = 1
        shifts = [[-1,0], [0, 1], [1, 0], [0, -1]]
        indexes = [(point[0]+shift[0], point[1]+shift[1]) for shift in shifts if self.check_dims(dims, point, shift)]

        for ind in indexes:
            basin_size += self.explore(ind, dims)

        return basin_size

    def get_data(self):
        array = np.zeros((100, 100), dtype=int)
        row =0
        with open('data/9.txt', 'r') as f:

            for line in f:
                line = line.strip()

                for ind, s in enumerate(line):
                    array[row, ind] = int(s)
                row += 1
        return array

    def is_minimum(self, point, dims):
        shifts = [[-1,0], [0, 1], [1, 0], [0, -1]]
        indexes = [(point[0]+shift[0], point[1]+shift[1]) for shift in shifts if self.check_dims(dims, point, shift)]
        val = self.data[point]

        for ind in indexes:
            if val >= self.data[ind]:
                return False
        print(val, point)
        return True

    def check_dims(self, dims, point, shift):
        if point[0]+shift[0] < 0 or point[0]+shift[0] > dims[0]-1 or point[1]+shift[1] < 0 or point[1]+shift[1] > dims[1]-1:
            return False
        return True

c = Cave()
