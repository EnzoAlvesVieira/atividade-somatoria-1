print('| --------------------IMC----------------------------- |')
print('| ---------------------------------------------------- |')
print('| Faixa de IMC        | Classificação                  |')
print('|---------------------|-------------------------------|')
print('| < 20.0              | Abaixo do peso                 |')
print('| 35.0 – 59.99        | Peso normal                    |')
print('| 60.0 – 89.99        | Sobrepeso                      |')
print('| 90.0 – 129.99       | Obesidade Grau I               |')
print('| 130.0 – 170.0       | Obesidade Grau II              |')
print('| ≥ 200.0             | Obesidade Grau III (mórbida)   |')
print('| ---------------------------------------------------- |')
print('| --------------------IMC----------------------------- |')
print('| ---------------------------------------------------- |')
nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade?'))
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
print('| ---------------------------------------------------- |')
imc = peso / (altura **2)
if imc <18.5:
    print(f'{nome} Você está abaixo do peso! Começe a se alimentar melhor. ')
elif imc <= 20.0:
    print(f'{nome} Você está com um peso normal! Continue se alimentando de maneira eficaz. ')
elif imc <=35.0:
    print(f'{nome} Você está Sobre-peso! Comece a se moderar em relação aos alimentos. ')
elif imc <=60.0:
    print(f'{nome} Você está com Obesidade Grau 1! Tome bastante cuidado com os alimentos gordurosos. ')
elif imc <=90.0:
    print(f'{nome} Você está com Obesidade Grau 2! Você está em situação critica, preste atenção para previnir o seu futuro. ')
elif imc <=130.0:
    print(f'{nome} Você está com Obesidade Grau 2! Você está em situação critica, preste atenção para prevenir o seu futuro. ')
else:

    print(f'{nome} Você está com Obesidade Grau 3(Mórbida) Você está com grandes chances de Infarto ou até mesmo de uma morte instantanea, comece a se cuidar. ')
