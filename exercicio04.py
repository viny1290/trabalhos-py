#Exercicio 5

vl = float(input("Valor da prestação: "))
mt = int(input("Porcentagem da multa: "))
qt = int(input("Dias de atraso: "))

prestacao = vl + (vl *(mt/100)*qt)

print("Prestação: ",prestacao)