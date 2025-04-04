import pandas as pd
# Importar as bibliotecas

def lin():
    print('-' * 40)
# Criar um def para as linhas que irei utilizar (puramente decorativo)

valor_recebidos = float(input("Insira o salário recebido: "))
# Input para perguntar ao user quanto ele recebeu em cada área
lin()
print('Valor recebido do salário:', valor_recebidos)
lin()
# Mostra ao user o recebido em cada área *tlvz eu tire dps se pa

valor_recebidoc = float(input("Insira o valor recebido para alimentação: "))
lin()
print('Valor recebido alimentação:', valor_recebidoc)
lin()

valor_recebidot = float(input("Insira o valor recebido para transporte: "))
lin()
print('Valor recebido transporte:', valor_recebidot)
lin()

valor_recebidom = float(input("Insira o valor recebido com outros: "))
lin()
print('Valor recebido outros:', valor_recebidom)
lin()

recebido_tot = valor_recebidos + valor_recebidoc + valor_recebidot + valor_recebidom
print('O valor total recebido esse mês foi de:', float(recebido_tot))
lin()
# Mostra ao user o total recebido no mês

listc = []
listt = []
listo = []
# Listas para receber os valores gastos no mês em cada área

def preencher_lista(lista, tamanho_maximo):
    while len(lista) < tamanho_maximo:
        lista.append(0)
# Criar uma função para preencher as listas menores com valor 0 para não quebrar a tabela no pandas

def obter_gastos(categoria, lista):
    while True:
        input_usuario = input(f"Insira o valor gasto com {categoria} ou 'ok' para sair: ")
        if input_usuario.lower() == "ok":
            break
        try:
            num = float(input_usuario)
            lista.append(num)
        except ValueError:
            print("Por favor, insira um valor válido ou 'ok' para sair.")
# Criar uma nova função que coletará todos os valores gastos em cada âmbito desejado

obter_gastos("comida", listc)
obter_gastos("transporte", listt)
obter_gastos("outros", listo)
# Rodar a função para coletar os valores das seguintes categorias.

max_length = max(len(listc), len(listt), len(listo))
# Determinar o tamanho máximo das listas

preencher_lista(listc, max_length)
preencher_lista(listt, max_length)
preencher_lista(listo, max_length)
#Rodar a função de preencher listas para todas as colunas terem exatamente o mesmo tamanho

df = pd.DataFrame({
    "Comida": listc,
    "Transporte": listt,
    "Outros": listo
})

# Criar a tabela com os valores gastos em cada área para aparecer os valores gastos na tabela do excel

df.loc['Recebido'] = [valor_recebidoc, valor_recebidot, valor_recebidom]
# Adicionar a linha de valores recebidos no início

df.loc['Gasto Total'] = [sum(listc), sum(listt), sum(listo)]
# Adicionar linha de gastos totais

df.loc['Total'] = df.loc['Recebido'] - df.loc['Gasto Total']
# Adicionar linha de Total (ganhos - gastos) para ver se possuiu lucro ou despesas no respectivo mês da tabela

mes = input("Digite o nome do mês para salvar o arquivo: ")
# Perguntar ao user o nome do respectivo mês para salvar o arquivo com o nome correto
df.to_excel(f'Controle_{mes}.xlsx', index=True)
# Salvar o arquivo no repositorio do usuario, permitindo a visualização da tabela inclusive nos arquivos do computador do user

print(df)
# Mostrar a tabela
print("Arquivo Excel salvo com sucesso!")
#Avisar ao user que a tabela no excel foi gerada

gasto_tot = sum(listc) + sum(listt) + sum(listo)
lin()
print('O valor total gasto esse mês foi de:', float(gasto_tot))
lin()
# Calcular o total de gastos e mostra-lós ao user

if valor_recebidot < sum(listt):
    print('Prejuízo no transporte, valor de:', valor_recebidot - sum(listt))
else:
    print('Saldo no transporte, valor de:', valor_recebidot - sum(listt))
# Verificando prejuízo ou saldo do transporte

if recebido_tot < gasto_tot:
    print('Prejuízo esse mês, valor de:', recebido_tot - gasto_tot)
else:
    print('Saldo esse mês, valor de:', recebido_tot - gasto_tot)
# Verificando prejuízo ou saldo total
