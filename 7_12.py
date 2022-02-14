import numpy as np

class Crabs:
    def __init__(self):
        self.data = np.loadtxt('data/7.txt', delimiter=',')
        self.init_pose = 0
        self.searching = True
        fuel = self.search_v1()
        print('Result: ', int(fuel))

    def apply_sum(self, array):
        result = (array +1) * array/2
        return np.sum(result)

    def search_v2(self):
        while True:
            data_left = self.data + 1 
            fuel = self.apply_sum(np.abs(self.data))
            fuel_left = self.apply_sum(np.abs(data_left))
            fuel_right = self.apply_sum(np.abs(self.data  - 1))
            
            if fuel < fuel_left:
                if fuel < fuel_right :
                    return fuel
                self.data -= 1
                self.init_pose += 1
            else:
                self.data += 1
                self.init_pose -= 1

    def search_v1(self):
        while self.searching:
            data_left = self.data + 1 
            fuel = np.sum(np.abs(self.data))
            fuel_left = np.sum(np.abs(data_left))
            fuel_right = np.sum(np.abs(self.data  - 1))
            
            if fuel < fuel_left:

                if fuel < fuel_right :
                    self.search = False
                    return fuel
                self.data -= 1
                self.init_pose += 1
            else:
                self.data += 1
                self.init_pose -= 1

crabs = Crabs()  
