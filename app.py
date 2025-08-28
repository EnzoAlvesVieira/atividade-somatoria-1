import streamlit as st
#-----------------------------------------------SIDEBAR
st.sidebar.image(f'logo.png')
st.sidebar.title('Live Better - Live Moments')
nome = st.sidebar.text_input('Qual o seu nome? ')
idade = st.sidebar.text_input('Qual a sua idade? ')
peso = st.sidebar.text_input('Qual o seu peso? ')
altura = st.sidebar.text_input('Qual a sua altura? ')
#-----------------------------------------------PRINCIPAL
st.title('Informações Corporais')
st.markdown('''| Faixa de IMC        | Classificação                  |
|---------------------|-------------------------------|
| < 18.5              | Abaixo do peso                 |
| 18.5 – 24.9         | Peso normal                    |
| 25.0 – 29.9         | Sobrepeso                      |
| 30.0 – 34.9         | Obesidade Grau I               |
| 35.0 – 39.9         | Obesidade Grau II              |
| ≥ 40.0              | Obesidade Grau III (mórbida)   |''')
if st.sidebar.button('Calcular '):
    peso = float(peso)
    altura = float(altura)
    imc = peso / (altura **2)
    st.metric('IMC', imc)
    if imc <18.5:
        st.write(f'{nome} Você está abaixo do peso! Começe a se alimentar melhor. ')
    elif imc <= 20.0:
        st.write(f'{nome} Você está com um peso normal! Continue se alimentando de maneira eficaz. ')
    elif imc <=35.0:
         st.write(f'{nome} Você está Sobre-peso! Comece a se moderar em relação aos alimentos.')
    elif imc <=60.0:
        st.write(f'{nome} Você está com Obesidade Grau 1! Tome bastante cuidado com os alimentos gordurosos.' )
    elif imc <=90.0:
        st.write(f'{nome} Você está com Obesidade Grau 2! Você está em situação critica, preste atenção para previnir o seu futuro.')
    elif imc <=130.0:
        st.write(f'{nome} Você está com Obesidade Grau 2! Você está em situação critica, preste atenção para prevenir o seu futuro.')
    
    else:
        st.write(f'{nome} Você está com Obesidade Grau 3(Mórbida) Você está com grandes chances de Infarto ou até mesmo de uma morte instantanea, comece a se cuidar.')