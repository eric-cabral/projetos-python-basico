import re

# CÁLCULO DO PRIMEIRO DÍGITO DE UM CPF

cpf = input(str('Digite um CPF para validação: ').strip())

# Substitui os caracteres especiais
lista_cpf = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', cpf)

# Soma os números do CPF após devida multiplicação
soma_digitos = []
primeiro_total = 0
index = 0
for multiplicador in range(10, 1, -1):
    soma_digitos = (int(lista_cpf[index]) * multiplicador)
    primeiro_total += soma_digitos
    index += 1

# Multiplica o total por 10 e obtem o resto do resultado por 11
segundo_total = (primeiro_total * 10) % 11

# Verifica se o segundo total é valido
primeiro_digito = 0 if segundo_total > 9 else segundo_total

print(f'O primeiro dígito deste CPF é {primeiro_digito}')
