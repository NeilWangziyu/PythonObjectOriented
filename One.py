import math
class Point:
    'represents a point in two dimensional space'
    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point'''
        self.move(x,y)

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)


# p1 = Point()
# # p2 = Point()
# # p1.reset()
# # p2.move(5, 0)
# # print(p2.calculate_distance(p1))
point = Point(3, 5)
print(point.x, point.y)