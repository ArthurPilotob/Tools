import streamlit as st

opcao = st.radio(
    "Deseja basear sua meta no tempo para ler o livro ou em páginas diárias que pretende ler?",
    ["Páginas diárias", "Tempo"]
)
pag_total = st.number_input('Quantas páginas o seu livro possui?')

tempo = None  # Inicializa a variável tempo

if opcao == 'Tempo':
    tempo = int(st.number_input('Quantos dias deseja levar até finalizar sua leitura: '))
    
    if tempo > 0:
        pag_diaria = round(pag_total / tempo)
        st.write(f'Você deve ler aproximadamente {pag_diaria} por dia para terminar seu livro em {tempo} dias')

if opcao == 'Páginas diárias':
    pag_diaria = st.number_input('Quantas páginas irá ler diariamente')

    if pag_diaria > 0:
        tempo = round(pag_total / pag_diaria)
        st.write(f'Você terminará o seu livro em {tempo} dias')

# Só executa o cálculo se tempo tiver sido definido
if tempo:
    pag_hj = st.number_input('Quantas páginas conseguiu ler hoje')
    pag_faltantes = pag_total - pag_hj
    tempo -= 1 
    
    if tempo > 0:
        previsao_nov = round(pag_faltantes / tempo)
        st.write(f'Faltam {pag_faltantes} páginas para terminar, anote para usar amanhã no código de novo!.')
        st.write(f'Para cumprir sua meta, agora precisará ler aproximadamente {previsao_nov} páginas por {tempo} dias, continue assim!.')
    else:
        st.write(f'Você concluiu o livro ou está no último dia! Restam {pag_faltantes} páginas.')
