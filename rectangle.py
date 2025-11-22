from figura import Figura
from punt import Punt

class Rectangle(Figura):
    def __init__(self, p1, p2, color):
        super().__init__(p1, color)
        self.__p2 = p2
    @property
    def altre(self):
        return self.__p2
    @altre.setter
    def altre(self, altre):
        self.__p2 = altre
    
    def area(self):
        base = self.pos.x - self.__p2.x
        altura = self.pos.y - self.__p2.y
        return base * altura

    def perimetre(self):
        base = self.pos.x - self.__p2.x
        altura = self.pos.y - self.__p2.y
        return abs(2 * (base + altura))
    
    def __str__(self):
        return f"Rectangle situada de {self.pos} a {self.__p2}  de color {self.color}"
    
    def toXML(self):
        x = min(self.pos.x, self.__p2.x)
        y = min(self.pos.y, self.__p2.y)
        width = abs(self.__p2.x - self.pos.x)
        height = abs(self.__p2.y - self.pos.y)
        return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{self.color}"/>'

    
if __name__ == "__main__":
    p1=Punt(2,3)
    p2=Punt(3,7)
    color = "#34FFDF"

    r = Rectangle(p1, p2, color)
    print(r)
    print("El perímetre és", r.perimetre())
    print("L'àrea és", r.area())