from linia import Linia
from rectangle import Rectangle
from cercle import Cercle
from punt import Punt
import os
import flet as ft
import flet.canvas as cv
Dibuix={
  "ample":800,
  "alt":600,
  "Figures":[]
}
def triarFigura():
    print("\nIndica la figura que vols afegir:")
    print("1 - Linia")
    print("2 - Rectangle")
    print("3 - Cercle")
    figura = input("Opció: ")

    if figura == "1":
        while True:
            dades = input("Introdueix les dades de la linia (x1 y1 x2 y2 #color): ")
            parts= dades.split()
            if len(parts) == 5:
                x1, y1, x2, y2, color = parts
                linia = Linia(Punt(int(x1),int(y1)),Punt(int(x2),int(y2)),color)
                Dibuix["Figures"].append(linia)
                print(f"Afegida: {linia}")
                break
            else:
                print("Dades incorrectes, torna-ho a provar.")
    elif figura == "2":
        while True:
            dades = input("Introdueix les dades del Rectangle (x1 y1 x2 y2 #color): ")
            parts= dades.split()
            if len(parts) == 5:
                x1, y1, x2, y2, color = parts
                rect = Rectangle(Punt(float(x1), float(y1)), Punt(float(x2), float(y2)), color)
                Dibuix["Figures"].append(rect)
                print(f"Afegit: {rect}")
                break
            else:
                print("Dades incorrectes, torna-ho a provar.")
        
    elif figura == "3":
        while True:
            dades = input("Introdueix les dades del Cercle (x1 y1 r #color): ")
            parts = dades.split()
            if len(parts) == 4:
                x, y, r, color = parts
                cercle = Cercle(Punt(float(x), float(y)), float(r), color)
                Dibuix["Figures"].append(cercle)
                print(f"Afegit: {cercle}")
                break
            else:
                print("Dades incorrectes, torna-ho a provar.")
    else:
        print("Opció no vàlida!")
def loadDibuix():
    try:
        nom = input("Introdueix el nom del fitxer per carregar el dibuix: ")
        ruta_base = os.getcwd() # directori de l'arxiu en execució
        ruta_a_recurs = os.path.join(ruta_base,"./Dades/"+ nom) # ruta relativa a l'arxiu en execució
        with open(ruta_a_recurs, "r", encoding="utf-8") as f:
            contingut = f.readlines()
        for part in contingut:
            linia = part.strip().split()
            print(linia)
            if linia[0] == "dimensions":
                Dibuix["ample"] = int(linia[1])
                Dibuix["alt"] = int(linia[2])
            elif linia[0] == "linia":
                x1 = int(linia[1])
                y1 = int(linia[2])
                x2 = int(linia[3])
                y2 = int(linia[4])
                color = linia[5]
                figura = Linia(Punt(x1, y1),Punt(x2, y2), color)
                Dibuix["Figures"].append(figura)
            elif linia[0] == "rectangle":
                x1 = float(linia[1])
                y1 = float(linia[2])
                x2 = float(linia[3])
                y2 = float(linia[4])
                color = linia[5]
                figura = Rectangle(Punt(x1, y1), Punt(x2, y2), color)
                Dibuix["Figures"].append(figura)
            elif linia[0] == "cercle":
                x = float(linia[1])
                y = float(linia[2])
                r = float(linia[3])
                color = linia[4]
                figura = Cercle(Punt(x, y), r, color)
                Dibuix["Figures"].append(figura)
    except Exception as e:
        print(f"{e}: El fitxer {nom} no existeix.\n")


def saveDibuix():
    nom_fitxer = input("Introdueix el nom del fitxer (sense extensió): ").strip()
    nom_fitxer += ".svg"
    nom_fitxer ="./Dades/" + nom_fitxer
    header = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
    header2 = f'<svg height="{Dibuix["alt"]}" width="{Dibuix["ample"]}">'
    footer = '</svg>'
    with open(nom_fitxer, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        f.write(header2 + "\n")
        for figura in Dibuix["Figures"]:
            f.write('  '+figura.toXML() + "\n")
        f.write(footer + "\n")

    print(f"Dibuix exportat a {nom_fitxer}\n")


def dibuixar(page: ft.Page):
    page.window_width = Dibuix["ample"]        
    page.window_height = Dibuix["alt"]       
    page.window_resizable = False  
    page.title = "Les meues figures"
    page.update()
    figs=[]
    for f in Dibuix["Figures"]:
        if type(f) is Linia:
            figs.append(cv.Line(f.pos.x,f.pos.y,f.altre.x,f.altre.y,
                paint=ft.Paint(stroke_width=1, style=ft.PaintingStyle.STROKE,color=f.color)))
        if type(f) is Rectangle:
            width = abs(f.pos.dist_x(f.altre))
            height = abs(f.pos.dist_y(f.altre))
            figs.append(cv.Rect(f.pos.x,f.pos.y,
                            width,
                            height,
                paint=ft.Paint(stroke_width=1, style=ft.PaintingStyle.FILL,color=f.color)))
        if type(f) is Cercle:
            figs.append(cv.Circle(f.pos.x,f.pos.y,f.radi,
                paint=ft.Paint(stroke_width=1, style=ft.PaintingStyle.FILL,color=f.color)))
    cp = cv.Canvas(
            figs,
            width=float("inf"),
            expand=True,
    )
    page.add(cp)
def menu():
    print("Indica el que vols fer:")
    print("  1 - Afegir figura al dibuix")
    print("  2 - Carregar dibuix des de fitxer")
    print("  3 - Exportar dibuix a SVG")
    print("  4 - Dibuixar i eixir")

def main():
    while True:
        menu()
        opcio = input("Opció: ")
        if opcio == "1":
            triarFigura()
        elif opcio == "2":
            loadDibuix()
        elif opcio == "3":
            saveDibuix()
        elif opcio == "4":
            print("Dibuixem i eixim")
            ft.app(target=dibuixar)   # Es crea una finestra flet amb la funció Dibuixar
            break

        else:
            print("Opció no vàlida!\n")
if __name__ == "__main__":
    main()