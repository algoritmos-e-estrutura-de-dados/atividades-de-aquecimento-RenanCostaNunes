import math


print ("Insira o valor x1: ")
x1= float (input())
print ("Insira o valor x2: ")
x2= float (input())
print ("Insira o valor y1: ")
y1= float (input())
print ("Insira o valor y2: ")
y2= float (input())

dist= math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

print (round(dist,4))