# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))

# if a>b:
#     print("O primeiro valor é maior")
# if b>a:
#     print("O segundo valor é maior")

# velocidade = int(input("Insira a velocidade do seu carro: ")
# )
# if velocidade>80:
#     multa = velocidade - 80
#     print(f"Você foi multado em R${multa*5}")
# else:
#     print("dahora")



# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))

# array = [a, b, c]

# print(f"O maior número é: {max(array, key=int)}")
# print(f"O menor número é: {min(array, key=int)}")



# salario = int(input("Insira seu salário: "))

# if salario > 1250:
#     aumento = salario * 0.1
#     print(f"Seu salário é de: R${salario + aumento:.2f} com um aumento de R${aumento:.2f}")
# else:
#     aumento = salario * 0.15
#     print(f"Seu salário é de: R${salario + aumento:.2f} com um aumento de R${aumento:.2f}")


distancia = int(input("Insira a distância: "))

if distancia <= 200:
    passagem = distancia * 0.5
    print(f"Sua viagem custará: R${passagem}")
else:
    passagem = distancia * 0.45
    print(f"Sua viagem custará: R${passagem}")