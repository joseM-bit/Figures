from figura import Figura
from punt import Punt

class Linia(Figura):
    def __init__(self, p1, p2, color):
        super().__init__(p1, color)
        self.__altre = p2
    @property
    def altre(self):
        return self.__altre
    @altre.setter
    def altre(self, altre):
        self.__altre = altre

    def area(self):
        return 0

    def perimetre(self):
        return self.pos.dist(self.__altre)
    
    def __str__(self):
        return f"Linia situada de {self.pos} a {self.__altre} de color {self.color}"
    
    def toXML(self):
        x1, y1 = self.pos
        x2, y2 = self.__altre
        return f'<line stroke="{self.color}" stroke-width="3" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" />'

    
if __name__ == "__main__":
    p1=Punt(2,3)
    p2=Punt(3,7)
    color="#34FFDF"
    l=Linia(p1,p2,color)
    print(l)
    print("La longitud es",l.perimetre())