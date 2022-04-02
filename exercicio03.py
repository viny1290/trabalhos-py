#Crie um programa que solicite ao usuário a sua idade expressa em anos, meses e dias (variaveis separadas).
#Calcule e mostre a idade expressa apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

a = int(input("Digites idade em anos: "))
m = int(input("Digites meses: "))
d = int(input("Digite dias: "))

ta = a * 365
tm = m * 30
tt = ta + tm + d

print("Sua idade em dias é: ", tt, "Dias")