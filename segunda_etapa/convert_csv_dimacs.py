import sys
from auxiliary_functions import *
from restrictions import *

def main(args):

    dados = []

    if(len(args) != 3):
        print("Parâmetros incorretos: digite -> python convert_csv_dimacs.py nome_do_arquivo.csv n_regras")
        sys.exit()

    if(int(args[2]) <= 0):
        print("Número de regras incorreto, precisa ser maior ou igual a 1")
        sys.exit()

    arquivo = args[1] #nome do arquivo
    m = int(args[2]) #numero de regras

    nome_arquivo = arquivo
    arquivo = arquivo.split('_') #separando o arquivo em strings

    try:
        with open(f"./pacientes/{nome_arquivo}", "r") as file:
            for linha in file:
                dados.append(linha.split(','))
        file.close()
    except FileNotFoundError:
        print("Arquivo não encontrado. Digite novamente o nome do arquivo.")

    if(not dados):
        print("Arquivo vazio. Procure outro arquivo para pesquisar.")
        sys.exit()

    # seperando os dados
    [atributos, pacientes_com_patologia, pacientes_sem_patologia] = separar_dados(dados)

    formula_final = And(
        And(
            And(
                is_cnf(apenas_tres_casos_para_cada_regra_atributo(m, atributos)),
                is_cnf(restricao2(atributos, m))
            ),
            And(
                is_cnf(pacientes_sem_patologia_algum_atributo_nao_aplicado_regra(pacientes_sem_patologia, m, atributos)),
                is_cnf(restricao4(pacientes_com_patologia, atributos, m))
            ),
        ),
        is_cnf(pacientes_com_patologia_cobertos_alguma_regra(pacientes_com_patologia, m))
    )

    cnf_para_dimacs(formula_final, nome_arquivo, m)
    

    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))