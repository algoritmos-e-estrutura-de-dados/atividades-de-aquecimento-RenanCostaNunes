
print ("Digite o código do produto: ")
cod_prod1= float(input())

print ("Insira a quantidade: ")
qtd_prod1= int(input())

print ("Insira o valor unitário: ")
und_prod1= float(input())

print ("Insira o segundo produto: ")


print ("Digite o código do produto: ")
cod_prod2= float(input())

print ("Insira a quantidade: ")
qtd_prod2= int(input())

print ("Insira o valor unitário: ")
und_prod2= float(input())

prod1= qtd_prod1 * und_prod1
prod2= qtd_prod2 * und_prod2


print ("VALOR A PAGAR: R$ ", round (prod1+prod2,2))