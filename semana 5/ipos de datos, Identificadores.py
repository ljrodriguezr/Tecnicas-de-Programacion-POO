# Calcular el área de un cuadrado
def calcular_area_cuadrado(largo, ancho):
    area = largo * ancho
    return area

# variables
largo_cuadrado = 9.5
ancho_cuadrado = 7.5

# llamado
area_cuadrado= calcular_area_cuadrado(largo_cuadrado, ancho_cuadrado)

#print(area_cuadrado)

if isinstance(largo_cuadrado, float) and isinstance(ancho_cuadrado, float):
    print(area_cuadrado)
else:
    print("los datos no son correctos")

