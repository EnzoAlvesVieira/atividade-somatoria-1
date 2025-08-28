print('| --------------------IMC----------------------------- |')
print('| ---------------------------------------------------- |')
print('| Faixa de IMC        | Classificação                  |')
print('|---------------------|-------------------------------|')
print('| < 18.5              | Abaixo do peso                 |')
print('| 18.5 – 24.9         | Peso normal                    |')
print('| 25.0 – 29.9         | Sobrepeso                      |')
print('| 30.0 – 34.9         | Obesidade Grau I               |')
print('| 35.0 – 39.9         | Obesidade Grau II              |')
print('| ≥ 40.0              | Obesidade Grau III (mórbida)   |')
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