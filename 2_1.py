
class Boat:
    def __init__(self):
        self.position = 0
        self.depth = 0
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

    def up(self, x):
        self.depth -= x

    def down(self, x):
        self.depth += x

boat = Boat()  
