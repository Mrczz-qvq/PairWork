import random

class Map():

    def __init__(self):
        self.imgMap = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        self.winMap = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]

    def click(self, x, y):
        flag = 0
        if y - 1 >= 0 and (self.imgMap)[y - 1][x] == 8:
            (self.imgMap)[y][x], (self.imgMap)[y - 1][x] = (self.imgMap)[y - 1][x], (self.imgMap)[y][x]
            flag = 1
        elif y + 1 <= 2 and (self.imgMap)[y + 1][x] == 8:
            (self.imgMap)[y][x], (self.imgMap)[y + 1][x] = (self.imgMap)[y + 1][x], (self.imgMap)[y][x]
            flag = 1
        elif x - 1 >= 0 and (self.imgMap)[y][x - 1] == 8:
            (self.imgMap)[y][x], (self.imgMap)[y][x - 1] = (self.imgMap)[y][x - 1], (self.imgMap)[y][x]
            flag = 1
        elif x + 1 <= 2 and (self.imgMap)[y][x + 1] == 8:
            (self.imgMap)[y][x], (self.imgMap)[y][x + 1] = (self.imgMap)[y][x + 1], (self.imgMap)[y][x]
            flag = 1

        return flag

    def randMap(self):
        for i in range(1000):
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            Map.click(self, x, y)