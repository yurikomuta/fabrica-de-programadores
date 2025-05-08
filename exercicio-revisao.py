#1-usuario irá inserir dois valores
#variavel é um espaço reservado na memória que recebe dados
#tipos variaveis ( texto, booleano, número(inteiro e float(flutuante-peso, altura, medida)))


#calcula subtração
#subtracao = numero1 - numero2
#print("A subtração dos números é :",subtracao)

#calculo multiplicacao
#multiplicacao = numero1 * numero2
#print("A multiplicação dos números é:",multiplicacao)

#calculo potencia 
#potencia = numero1 ** numero2
#print("A potência do numero 1 elevado ao número 2 é: ",potencia)

#########

nota1 = int(input('Insira primeira nota:'))
#print(numero1)

nota2 = float(input('Insira segunda nota :'))
#print(numero2)

#calculo de media
media = nota1 + nota2 / 2
#print("O valor de soma entre os números declarado é: ",soma)

#exemplo booleano
# media = int(input("Digite a sua idade:"))
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
