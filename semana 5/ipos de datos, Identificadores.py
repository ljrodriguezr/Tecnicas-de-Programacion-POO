# Calcular el área del rectángulo
def calcular_area_rectangulo(largo, ancho):
    area = largo * ancho
    return area

# variables
largo_rectangulo = 9.5
ancho_rectangulo = 7.5

# llamado
area_rectangulo= calcular_area_rectangulo(largo_rectangulo, ancho_rectangulo)

#print(area_rectangulo)

if isinstance(largo_rectangulo, float) and isinstance(ancho_rectangulo, float):
    print(area_rectangulo)
else:
    print("los datos no son correctos")

