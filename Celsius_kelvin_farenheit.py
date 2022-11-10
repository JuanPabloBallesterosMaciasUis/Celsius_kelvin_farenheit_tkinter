import math
# Programa No. 1 : area y perimetro circulo

print("-------------------------")
print("----AREA - PERIMETRO-----")

# input
r = input("Dijite el valor de radio: ")
r = int(r)

#process
A = math.pi*r**2
P = 2*math.pi*r

#output
print("------------RESULTADO------------")
print("El area es: "+ str (A))
print("El perimetro es: "+ str(P))
print("---------------------------------")