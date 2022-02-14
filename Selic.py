cores = {'verde': '\033[1;32m',
        'vermelho': '\033[1;31m',
        'ciano': '\033[1;36m',
        'roxo': '\033[1;35m',
        'limpar': '\033[m'}

deposito_inicial = float(input('Digite seu depósito inicial: R$ '))
investimento = float(input('Digite aqui seu investimento mensal: R$ '))
print(f'A taxa de juros do {cores["verde"]}PicPay{cores["limpar"]} é de {cores["verde"]}0.98%{cores["limpar"]} ao mês. Dados do dia {cores["ciano"]}(10/02/2022){cores["limpar"]}')
mes = 1
saldo = deposito_inicial + investimento
while mes <= 24:
    if mes == 1:
        juros = (saldo * 0.98 / 100) # Juros
        saldo = saldo + (saldo * 0.98 / 100) # Saldo com Juros
        juros_final = saldo - juros # Juros sozinho
    else:
        juros = (saldo * 0.98 / 100) # Juros
        saldo = saldo + (saldo * 0.98 / 100) + investimento # Saldo com Juros
        juros_final = saldo - juros # Juros sozinho
    print(f'''No {cores['roxo']}{mes}° mês{cores['limpar']}, seu saldo é de: {cores["verde"]}R$ {saldo:.2f}{cores["limpar"]}.
Fazendo um investimento de {cores["vermelho"]}R$ {investimento:.2f}{cores["limpar"]} ao mês, sob {cores['vermelho']}0.98%{cores['limpar']} de juros ao mês!
Portanto, seu capital rendeu R$ {cores['ciano']}{juros:.2f}{cores['limpar']} de juros.\n''')
    mes += 1
print(f'O ganho total obtido é de {cores["verde"]}R$ {saldo:.2f}{cores["limpar"]}.')
