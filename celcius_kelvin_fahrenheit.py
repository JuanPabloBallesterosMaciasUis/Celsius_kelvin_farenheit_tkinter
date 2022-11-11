# Converetir una cantidad dad de °C en su equivalente a °k Y °F

print("--------------------------------------")
print("-----Celsius en kelvin y fahrenheit----")
print("--------------------------------------")

#input
C = input("Dijíte los °C: ") 
C = int(C)

#process
k = C + 273

k1 = int(C)
f = (C*9/5) +32


f1 = int(f)

#output
print("-------------------------------RESULTADOS-------------------------------------------")
print("De los ",C,"grados celsius,"  "serian" ,k, "grados kelvin y" ,f, " grados fahrenheit")
print("------------------------------------------------------------------------------------") 