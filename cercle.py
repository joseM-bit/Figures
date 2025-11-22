from figura import Figura
from punt import Punt
import math
class Cercle(Figura):
    def __init__(self, centre, radi, color):
        super().__init__(centre, color)
        self.__radi = radi
    @property
    def radi(self):
        return self.__radi
    @radi.setter
    def radi(self, altre):
        self.__radi = altre

    def area(self):
        return math.pi * (self.__radi ** 2)

    def perimetre(self):
        return 2 * math.pi * self.__radi

    def __str__(self):
        return f"Cercle situada en centre {self.pos} i radi {self.__radi} de color {self.color}"
    def toXML(self):
        return f'<circle cx="{self.pos.x}" cy="{self.pos.y}" fill="{self.color}" r="{self.__radi}"/>'
    
if __name__ == "__main__":
    p1=Punt(2,3)
    p2=Punt(3,7)
    color="#34FFDF"
    c=Cercle(p1,4,color)
    print(c)
    print("El perímetre es",c.perimetre())
    print("El area es",c.area())