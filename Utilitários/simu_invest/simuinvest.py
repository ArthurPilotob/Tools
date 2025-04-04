#Simuinvest (vs)

#Input do valor para o investimento
valor = float(input('Valor que deseja investir agora: '))

#Input de decisão se a pessoa investirá mensalmente
pergunta = input('Deseja aplicar valor mensalmente? (digite sim ou não) ').strip().lower()[0]

 #If para caso a pessoa deseja aplicar um valor mensalmente
if pergunta == 's':
    valor_mensal = float(input('Qual valor deseja? '))
else:
    valor_mensal = 0

#Taxa usada (100% CDI)
taxam = 0.011

#Input do tempo do investimento
tempom = int(input('Digite o tempo em meses que pretende aplicar: '))

#Crio uma outra varavel pois como irei usar (valor) futuramente no codigo preciso armazenar esse valor em algum lugar
valor_investido = valor


#Define o contador de meses
mesparaprint = 1

#Prints para melhor visualização do conteúdo do programa
print(" ")
print('Evolução patrimonial ao longo dos meses: ')

#For se repetindo a quantidade de meses, simulando o juros composto
for mes in range(tempom):
    #Cálculo do juros composto
    valor_juros = valor_investido * taxam
    valor_investido += valor_juros + valor_mensal
    valor_tot_mensal = (valor_mensal*tempom)
    dividendo = (valor+valor_tot_mensal)
    #Prints
    print('-'*30)
    print(f'Carteira mês {mesparaprint} : R${valor_investido:.2f}')
    #Aumentar o contador de meses em 1 a cada repetição do programa
    mesparaprint += 1

#Calcula o valor que o investimento rendeu
invest_rendeu = valor_investido - dividendo

#Prints mostrando o valor que rendeu e o valor total da sua conta
print(" ")
print(f'Seus investimentos renderão o valor de R$ {invest_rendeu:.2f}')
print(f'O valor total da sua conta será de R$ {valor_investido:.2f}')
