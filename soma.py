#Contexto: Vamos criar um programa que solicitará ao usuário a inserção de dois números.
# Esses números serão armazenados em diferentes
#variáveis pré-definidas pelo programador.
#Após a inserção será calculado a operação e exibido ao
#usuário o resultado

#variaveis para número 
# int essa recebe valores inteiros (1,2,3,4,5...)
# float essa receberá valores flutuantes (peso, altura, moeda, pi ...)

numero1 = int(input("Digite o primeiro número :"))
#print(numero1)

numero2 = float(input("Digite o segundo número :"))
#print(numero2)

soma = numero1 + numero2

print("O resultado da soma dos dois números é : ",soma)