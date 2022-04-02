#Faça um programa que calcule e mostre o valor do volume do tronco de uma pirâmide, para isso o 
# programa deve solicitar ao usuário os valores da altura (h), o valor da base menor (b) e o da base maior (B)
#E calcule a seguinte expressão: V=h/3*(B**2+b**2+(B**2*b**2)**0.5)

h = float(input("Altura do tronco da pirâmide: "))
b = float(input("Valor da base menor: "))
B = float(input("Valor da base maior: "))

h = B ** 2 * b ** 2
w = B ** 2 + b ** 2
d = w + h ** 0.5
V = h / 3 * d

print("Volume da piramide = ", V)