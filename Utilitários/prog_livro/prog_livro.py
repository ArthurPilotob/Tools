#Decisão do cálculo por páginas diárias ou por um certo período de tempo
choice = str(input('Deseja fazer o calcúlo por dias (d) que se tem para ler o livro ou por páginas diárias(pd)? '))
pag_total = int(input('Quantas páginas o livro tem (ou quantas ainda faltam)? '))

#Caso escolha páginas diárias a conta é para descobrir o tempo
if choice == 'pd':
  pag_dia = int(input('Quantas páginas deseja ler por dia? '))
  tempo = round(pag_total/pag_dia)
  print(f'Lendo {pag_dia} por dia, você demoraria {tempo} dias para acabar o livro. ')

#Caso escolha dia a conta é para descobrir quantas páginas deve ler diariamente
elif choice == 'd':
  tempo = int(input('Em quantos dias deseja terminar o livro? '))
  pag_dia = round(pag_total / tempo)
  print(f'Para acabar o livro em {tempo} dias, você precisaria ler {pag_dia,} por dia. ')


# Input de progresso diário
pag_hj = int(input('Quantas páginas leu hoje? '))
pag_faltantes = pag_total - pag_hj
tempo -= 1  # Reduzindo o tempo restante

# Evitando erro de divisão por zero
if tempo > 0:
    previsao_nov = round(pag_faltantes / tempo)
    print(f'Faltam {pag_faltantes} páginas para terminar, anote para usar amanhã no código de novo!.')
    print(f'Para cumprir sua meta, agora precisará ler aproximadamente {previsao_nov} páginas por {tempo} dias, continue assim!.')
else:
    print(f'Você concluiu o livro ou está no último dia! Restam {pag_faltantes} páginas.')
