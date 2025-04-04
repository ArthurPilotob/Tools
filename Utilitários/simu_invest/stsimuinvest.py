
import streamlit as st
import pandas as pd
#Baixar as bibliotecas necessárias

cdi = float(0.011)
#Valor do cdi

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#Importa o styles css para estilizar os meus textos e inputs

col1, col2, col3 = st.columns([1, 4, 1])
#Crio as colunas para melhorar a visualização da logomarca

with col1:
    st.image('C:/Users/Oem/_projeto_teste/img/logo_azul (3).png', caption='.', width=300)
#Adiciono a img pelo caminho (deve estar no mesmo repositório)

st.title('Seja bem-vindo ao simulador de investimento!')
st.write('Teste o quanto seu dinheiro renderá no futuro.')
#Adiciono o título e a descrição do app

col2, col3, col4 = st.columns([1, 1, 1])
#Crio as colunas para organizar os meus inputs

with col2:
    valor = st.number_input("Valor que irá investir.", min_value=0.0, step=10)

with col3:
    tempo = st.number_input("Tempo em meses.", min_value=1, step=1)
#Inputs para perguntar ao user as informações do investimento que ele irá fazer

with col4:
    banco = st.radio("Escolha qual banco deseja (CDB liquidez diária)", options=["Itaú", "Nubank", "PicPay", "Rico", "Inter", "Bradesco",])
#Input com radio para tomada de decisão de qual banco ele irá investir

st.write("Você escolheu: ", banco)
#Decisão do user

if banco == "Itaú":
    cdb = float(1 * cdi)
elif banco == "Nubank":
    cdb = float(1 * cdi)
elif banco == "PicPay":
    cdb = float(1.02 * cdi)
elif banco == "Rico":
    cdb = float(1.50 * cdi)
elif banco == "Inter":
    cdb = float(1 * cdi)
elif banco == "Bradesco":
    cdb = float(1 * cdi)
#Ifs e suas respectivas diferenças (valor do cdi)

pergunta = st.radio('Deseja aplicar um valor mensalmente?', ('Sim', 'Não'))
#Input de escolha para decidir se o user vai ou não aplicar um valor mensalmente

if pergunta == 'Sim':
    valor_mensal = st.number_input("Qual valor?", min_value=0.0, step=10)
else:
    valor_mensal = 0
    #Pergunta ao user qual valor ele deseja aplicar (se a resposta for não o valor é definido como zero, para o codigo não quebrar)

if st.button('Executar simulação'):
  #Botão de submit para os resultados não aparecerem imediatamente, diminuindo a poluição visual do app
    valor_investido = valor
    #Definir o valor a ser investido
    mesparaprint = 1
    #Definir o contador de meses
    resultados = []
    meses = []
    valores = []
    #Definir as listas que armazenaram os valores para futuramente mostrar esses dados ao user

    for mes in range(tempo):
      #For definindo quantas vezes o juros se repetirá
        valor_juros = valor_investido * cdb
        #Definição do valor de juros
        valor_investido += valor_juros + valor_mensal
        #Definição do proximo valor a ser investido (juros compostos)
        resultados.append([mesparaprint, valor_investido])
        #Inserir os valores na lista
        meses.append(mesparaprint)
        #Inserir os meses que passaram na lista
        valores.append(valor_investido)
        #Inserir os valores na lista
        mesparaprint += 1
        #Sempre que um mês passa no for adiciona 1 ao contador

    df_resultados = pd.DataFrame(resultados, columns=['Mês', 'Valor da Carteira'])
    #Definem a tabela com os valores de mês e valor no ínicio da coluna
    df_resultados.set_index('Mês', inplace=True)
    #Define o índice da tabela como 'mês'
    df_resultados['Valor da Carteira'] = df_resultados['Valor da Carteira'].round(2)
    #Arredonda para duas casas decimais o valor da carteira
    st.line_chart(df_resultados['Valor da Carteira'], use_container_width=True)
    #Define o gráfico como os valores da carteira, para mostrar a evolução ao user

    total_investido =valor + valor_mensal * tempo
    #Define o valor total investido pelo user
    invest_rendeu = valor_investido - total_investido
    #Define o valor total que o investimento rendeu

    df_resultados['Valor da Carteira'] = df_resultados['Valor da Carteira'].apply(lambda x: f'R$ {x:.2f}')
    #Mostra ao user a tabela com a formataçao adequada com R$ e duas casas decimais

    st.dataframe(df_resultados, use_container_width=True)
    #Fazer a tabela preencher todo o espaço disponível, tambem habilitando a rolagem com o mouse e a opção tela cheia

    st.markdown(f'<p class="last-text">Seus investimentos renderão o valor de R$ {invest_rendeu:.2f}</p>', unsafe_allow_html=True)
    #Primeiramente atribuo uma classe para conseguir fazer a estilização no css, depois, mostro ao user o valor que o investimento dele rendeu
    st.markdown(f'<p class="last-text">O valor total da sua conta será de R$ {valor_investido:.2f}</p>', unsafe_allow_html=True)
    #Mesma ideia do markdown de cima, mostro ao user o valor total de sua carteira
