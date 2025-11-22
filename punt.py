import math
class Punt:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, altre):
        self.__x = altre
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, altre):
        self.__y = altre

    def dist(self, altre):
        return math.sqrt((self.x - altre.x)**2 + (self.y - altre.y)**2)

    def dist_x(self, altre):
        return (self.x - altre.x)

    def dist_y(self, altre):
        return (self.y - altre.y)
    def __str__(self):
        return f"({self.x}, {self.y})"
    
if __name__ == "__main__":
    p1 = Punt(2, 3)
    p2 = Punt(3, 4)
    print("La distancia entre",p1,"i",p2," es ",p1.dist(p2))