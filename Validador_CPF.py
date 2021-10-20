def get_cpf():
    cpf = input('Digite o seu CPF, apenas os números >>> ')
    print()
    return cpf

def prepare_cpf(cpf):
    for i in cpf:
        if not i.isnumeric():
            print(f'"{i}" Não é número')
            validador_de_cpf()
    cpf_sliced = cpf[0:-2]
    return cpf_sliced

def creat_digits(total):
    conta = 11 - (total % 11)
    resultado = 0 if conta > 9 else conta
    return resultado

def get_digits(pre_worked_cpf):
    multiply = len(pre_worked_cpf) + 1
    total = 0

    for num in pre_worked_cpf:
        total += int(num) * multiply
        multiply -= 1
    return creat_digits(total)

def validador_de_cpf():
    # Pega valor de um input do usuario
    cpf = get_cpf()
    
    # Retira os dois ultimos números do CPF e verifica se há
    # caracteres invalidos
    worked_cpf = prepare_cpf(cpf)

    while len(worked_cpf) != len(cpf):
        # Calcula o penultimo e ultimo digito do cpf nessa ordem e os adiciona
        # ao cpf já trabalhado
        digito = get_digits(worked_cpf)
        worked_cpf += str(digito)

    print(f"O CPF {cpf} é valido!" if cpf == worked_cpf else f"O CPF {cpf} invalido")

###################################################

validador_de_cpf()
