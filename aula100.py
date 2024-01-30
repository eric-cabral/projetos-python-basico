import re

# CÁLCULO DO PRIMEIRO DÍGITO DE UM CPF

#cpf = input(str('Digite um CPF para validação: ').strip())
cpf_usuario = ('478.762.278-13')

# Substitui os caracteres especiais
lista_cpf = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', cpf_usuario)[:9]

# Soma os números do CPF após devida multiplicação
soma_digitos_1 = []
primeiro_total_1 = 0
index_1 = 0
for multiplicador in range(10, 1, -1):
    soma_digitos_1 = (int(lista_cpf[index_1]) * multiplicador)
    primeiro_total_1 += soma_digitos_1
    index_1 += 1

# Multiplica o total por 10 e obtem o resto do resultado por 11
segundo_total_1 = (primeiro_total_1 * 10) % 11

# Verifica se o segundo total é valido
primeiro_digito = 0 if segundo_total_1 > 9 else segundo_total_1


# CÁLCULO DO SEGUNDO DÍGITO DO CPF

# Adiciona o primeiro dígito ao CPF
lista_cpf_digito_2 = lista_cpf + str(primeiro_digito)

# Calcula o segundo dígito do CPF
soma_digitos_2 = []
primeiro_total_2 = 0
index_2 = 0
for multiplicador in range(11, 1, -1):
    soma_digitos_2 = (int(lista_cpf_digito_2[index_2]) * multiplicador)
    primeiro_total_2 += soma_digitos_2
    index_2 += 1

# Multiplica o total por 10 e obtem o resto do resultado por 11
segundo_total_2 = (primeiro_total_2 * 10) % 11

# Verifica se o segundo total é valido
segundo_digito = 0 if segundo_total_2 > 9 else segundo_total_2

cpf_calculado = f'{lista_cpf}{primeiro_digito}{segundo_digito}'

if re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', cpf_usuario) == cpf_calculado:
    print(f'O CPF {cpf_usuario} é válido!')
else:
    print('CPF inválido!')
