import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Exibição do título
st.title('Seu controle financeiro')
st.write('Adicione os valores e geraremos sua planilha!')

# Criação das colunas para os inputs de valores recebidos
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col1:
    recsal = st.number_input('Salário:', min_value=0.0, step=10.0, key="salario")
with col2:
    recali = st.number_input('Alimentação:', min_value=0.0, step=10.0, key="alimentacao")
with col3:
    rectra = st.number_input('Transporte:', min_value=0.0, step=10.0, key="transporte_recebido")
with col4:
    recout = st.number_input('Outros:', min_value=0.0, step=10.0, key="outros_recebido")

receb = recsal + recali + rectra + recout

# Inicialização do session state para armazenar os valores gastos
if 'valores_comida' not in st.session_state:
    st.session_state.valores_comida = []
if 'valores_transporte' not in st.session_state:
    st.session_state.valores_transporte = []
if 'valores_outros' not in st.session_state:
    st.session_state.valores_outros = []
if 'mostrar_gastos' not in st.session_state:
    st.session_state.mostrar_gastos = False

# Exibindo valores recebidos
if st.button('Enviar'):
    st.session_state.mostrar_gastos = True
    st.write(f'O valor recebido esse mês foi de R$ {receb:.2f}')

# Exibir seção de gastos apenas após clicar no botão "Enviar"
if st.session_state.mostrar_gastos:
    # Criação das colunas para os inputs de valores gastos
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        com = st.number_input('Comida (adicionar valor):', min_value=0.0, step=10.0, key="comida")
        if st.button('Adicionar valor em comida'):
            if com is not None:
                st.session_state.valores_comida.append(com)

    with col2:
        out = st.number_input('Outros:', min_value=0.0, step=10.0, key="outros_gasto")
        if st.button('Adicionar valor em outros'):
            if out is not None:
                st.session_state.valores_outros.append(out)

    with col3:
        tra = st.number_input('Transporte:', min_value=0.0, step=10.0, key="transporte_gasto")
        if st.button('Adicionar valor à transporte'):
            if tra is not None:
                st.session_state.valores_transporte.append(tra)

    # Mostrar todos os valores na tabela
    if st.session_state.valores_comida or st.session_state.valores_transporte or st.session_state.valores_outros:
        dados = {
            'Comida': st.session_state.valores_comida,
            'Transporte': st.session_state.valores_transporte,
            'Outros': st.session_state.valores_outros
        }
        max_len = max(len(st.session_state.valores_comida), len(st.session_state.valores_transporte), len(st.session_state.valores_outros))
        df = pd.DataFrame({
            'Comida': st.session_state.valores_comida + [0] * (max_len - len(st.session_state.valores_comida)),
            'Transporte': st.session_state.valores_transporte + [0] * (max_len - len(st.session_state.valores_transporte)),
            'Outros': st.session_state.valores_outros + [0] * (max_len - len(st.session_state.valores_outros))
        })
        st.write(df)

    # Somando os valores totais
    total_comida = sum(filter(None, st.session_state.valores_comida))
    total_transporte = sum(filter(None, st.session_state.valores_transporte))
    total_outros = sum(filter(None, st.session_state.valores_outros))
    total_gasto = total_comida + total_transporte + total_outros

    # Exibição do total gasto
    st.write(f'Total gasto este mês: R$ {total_gasto:.2f}')

    # Adicionando botão para limpar os dados
    if st.button("Limpar dados"):
        st.session_state.valores_comida = []
        st.session_state.valores_transporte = []
        st.session_state.valores_outros = []
        st.session_state.mostrar_gastos = False
        st.experimental_rerun()

    # Exibição do gráfico de pizza apenas se houver gastos
    if total_gasto > 0:
        sizes = [total_comida, total_transporte, total_outros]
        labels = ['Comida', 'Transporte', 'Outros']

        st.write('Gráfico que demonstra seus gastos do mês: ')
        fig, ax = plt.subplots()
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')

        wedges, texts, autotexts = ax.pie(
            sizes, 
            labels=labels, 
            autopct='%1.1f%%', 
            startangle=90, 
            colors=['#ff9999','#66b3ff','#99ff99']
        )

        for label in texts:
            label.set_color('white')
        for autotext in autotexts:
            autotext.set_color('white')

        ax.axis('equal')
        st.pyplot(fig)
    else:
        st.write("Nenhum valor foi gasto este mês.")
