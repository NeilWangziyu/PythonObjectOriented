import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)

class Polygon:
    def __init__(self, points=[]):
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append((point))

    def perimeter(self):
        periometer = 0
        points = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            periometer += points[i].distance(points[i+1])
        return periometer


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)



class Silly:
    def _get_silly(self):
        print("a")
        return self._silly

    def _set_silly(self, value):
        print('B')
        self._silly = value

    def _del_silly(self):
        print('C')
        del self._silly

    silly = property(_get_silly, _set_silly, _del_silly, "This is a silly property.")

# 使用装饰器改写
class Silly_r:
    @property
    def silly(self):
        "Thii is a class use decorator"
        print("a")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("B")
        self.__silly = value

    @silly.deleter
    def silly(self):
        print("C")
        del self.__silly








if __name__ == '__main__':
    c = Color('#0000ff', 'bright red')
    print(c.name)
    c.name = 'red'
    print(c.name)

    s = Silly()
    s.silly = 'funny'
    print(s.silly)
    del s.silly


