import numpy as np
from collections import deque

class LanternFish:
    def __init__(self):
        path = 'data/6.txt'
        self.fishes = np.loadtxt(path, dtype=int, delimiter=',')
        self.fish_bins = self.create_fishbins()
        for i in range(256):
            self.forward()
        print('Result: ',sum(self.fish_bins))

    def create_fishbins(self):
        bins = []
        suma = 0
        for i in range(9):
            count = np.where(self.fishes == i)
            count = len(count[0])
            bins.append(count)
            suma += count
        fish_bins = deque(bins)
        return fish_bins

    def forward(self):
        self.fish_bins.rotate(-1)
        self.fish_bins[6] += self.fish_bins[-1]

l = LanternFish()