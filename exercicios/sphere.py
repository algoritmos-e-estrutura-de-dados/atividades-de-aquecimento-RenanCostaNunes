import math

print ("Insira o raio da esfera")
raio= float(input())

vol= (4/3.0) * 3.14159 * math.pow(raio,3)

print ("VOLUME= ",(round(vol,3)))