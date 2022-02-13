
class Boat:
    def __init__(self):
        self.position = 0
        self.depth = 0
        self.aim = 0
        with open('data/2.txt', 'r') as f:
            self.data = f.readlines()

        for line in self.data:
            x = line[-2]
            func = getattr(self, line[0:-3])
            func(int(x))

        print('depth: ', self.depth)
        print('horizontal: ', self.position)
        print('result: ', self.depth * self.position)

    def forward(self, x):
        self.position += x
        self.depth += x * self.aim

    def up(self, x):
        self.aim -= x

    def down(self, x):
        self.aim += x

boat = Boat()  
