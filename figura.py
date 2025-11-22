from punt import Punt
import re
from abc import ABC, abstractmethod
class Figura:
    def __init__(self, posicio, color):
        self.__pos = posicio
        self.__color = color

    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self, valor):
        self.__pos = valor

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, valor):
        self.__color = valor
        
    def area(self):
        pass

    def perimetre(self):
        pass
    
        
    def __str__(self):
        return f"Figura de color {self.color} a la posicio {self.pos}"
    
    @abstractmethod
    def toXML(self):
        pass

def comprovaHEX(hex_string):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_string)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    p1=Punt(2,3)
    p2=Punt(3,4)
    color="#34FFDF"
    print (f'El color {color} valid={comprovaHEX(color)}')
    f=Figura(p1,color)
    print(f)