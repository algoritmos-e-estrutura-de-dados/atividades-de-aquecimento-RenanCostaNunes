print ("Insira seu nome: ")
name= str(input())

print ("Digite seu salário fixo: ")
sal_fix= float(input())

print ("Digite seu total de vendas: ")
vend= float(input())


vend_bon = sal_fix + (vend*0.15) 

print (name, ".Seu salário é de = ", vend_bon)