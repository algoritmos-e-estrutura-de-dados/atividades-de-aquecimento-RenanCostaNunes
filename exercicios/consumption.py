from decimal import Decimal
print ("Insira a distância percorrida: ")
dist= Decimal(input())
print ("Insira quanto litros foram utilizados: ")
km= Decimal(input())


print (round (dist/km,3))