import math
print ("Insira o ponto A: ")
a=float(input())

print ("Insira o ponto B: ")
b=float(input())

print ("Insira o ponto C: ")
c=float(input())

print ("TRIANGULO: ", (round (a*c,3)/2))
print ("CIRCULO: ",  (round (3.14159*math.pow(c,2),3) ))
print ("TRAPEZIO: ", ((a+b)*c)/2 )
print ("QUADRADO: ", (round (math.pow(b,2),3)))
print ("RETANGULO: ", (round (a*b,3)))  
