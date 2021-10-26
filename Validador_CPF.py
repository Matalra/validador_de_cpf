from random import randint

def get_cpf(n = None):
    generating = False
    if not n:
        cpf = input('Digite o seu CPF, apenas os números >>> ')
    else:
        cpf = n
        generating = True
    return cpf, generating


# Retira dois ultimos números do CPF e verifica por caracteres invalidos
def prepare_cpf(cpf):
    if len(cpf) != 11:
            print(f'O CPF foi digitado incorretamente, verifique os números e tente novamente...')
            validador_de_cpf()
    
    for i in cpf:
        if not i.isnumeric():
            print(f'"{i}" Não é número, digite o CPF novamente, por favor...')
            validador_de_cpf()
    
    if not int(cpf):
        print(f'O CPF foi digitado incorretamente, verifique os números e tente novamente...')
        validador_de_cpf()
    
    cpf_sliced = cpf[0:-2]
    return cpf_sliced


# Calcula o penultimo e ultimo digito do cpf nessa ordem e os adiciona
def creat_digits(total):
    conta = 11 - (total % 11)
    resultado = 0 if conta > 9 else conta
    return resultado


# Gera o valor a ser calculado por creat_digits
def get_digits(pre_worked_cpf):
    multiply = len(pre_worked_cpf) + 1
    total = 0

    for num, multiplier in enumerate(range(multiply,1,-1)):
        total += int(pre_worked_cpf[num]) * multiplier

    return creat_digits(total)


def validador_de_cpf(n = None):
    cpf, generating = get_cpf(n)
    worked_cpf = prepare_cpf(cpf)

    while len(worked_cpf) != len(cpf):
        digito = get_digits(worked_cpf)
        worked_cpf += str(digito)

    if cpf == worked_cpf:
        print()
        print(f"O CPF {cpf} é valido!")
        return cpf

    elif generating:
        return False
   
    else:
        print(f"O CPF {cpf} é invalido!")


# Gerador de CPF aleatórios e validos
def gera_cpf():
    while True:
        rand_cpf = str(randint(11111111211,99999999999))
        cpf_valido = validador_de_cpf(rand_cpf)
        if cpf_valido:
            return cpf_valido
