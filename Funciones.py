import math


# ##Función de potencia
# def multi(x):
#     return x*x
# print(multi(4))

##Función área de un circulo
radio=input("\n\nIngrese el radio del círculo (metros): ")
radioint=float(radio)
def areacir(r):
    area = (math.pi)*(r**2)
    return area
def pericir(r):
    perimetro= (math.pi)*(2*r)
    return perimetro
def volucir(r):
    volumen=(4/3)*(math.pi)*(r**3)
    return volumen
print("\nEl perimetro del círculo es:",pericir(radioint),"metros")
print("El área del círculo es:",areacir(radioint),"metros cuadrados")
print("El vólumen del círculo es:",volucir(radioint),"metros cúbicos \n\n")

# ##División entera
# var=(5//2)*2.0
# print(var)

