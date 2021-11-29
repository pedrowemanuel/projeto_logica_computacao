import sys
from auxiliary_functions import separar_dados

from restrictions import *

def main(args):

    dados = []

    if(len(args) != 3):
        print("Parâmetros incorretos: digite -> python main.py nome_do_arquivo.csv n_regras")
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
    #print(apenas_tres_casos_para_cada_regra_atributo(m, atributos))
    #print(restricao2(atributos, m))
    #print(pacientes_sem_patologia_algum_atributo_nao_aplicado_regra(pacientes_sem_patologia, m, atributos))
    #print(restricao4(pacientes_com_patologia, atributos, m))
    #print(pacientes_com_patologia_cobertos_alguma_regra(pacientes_com_patologia, m))
    formula_final = And(
        And(
            And(
                apenas_tres_casos_para_cada_regra_atributo(m, atributos),
                restricao2(atributos, m)
            ),
            And(
                pacientes_sem_patologia_algum_atributo_nao_aplicado_regra(pacientes_sem_patologia, m, atributos),
                restricao4(pacientes_com_patologia, atributos, m)
            ),
        ),
        pacientes_com_patologia_cobertos_alguma_regra(pacientes_com_patologia, m)
    )
    #print(length(formula_final))
    print(formula_final)
    solucao = satisfiability_brute_force(formula_final)
    #print(solucao)
    '''regra_solucao = []
    if solucao:
        for i in solucao:
            if 'C' in i:
                continue
            if solucao[i]:
                partes_resposta = i.split("_")
                if partes_resposta[3] == "n":
                    partes_atributo = partes_resposta[1].split(" ")
                    regra_solucao.append(partes_atributo[0]+" > "+partes_atributo[2])
                elif partes_resposta[3] == "p":
                    regra_solucao.append(partes_resposta[1])
        print(regra_solucao)
    else:
        print('Não existe um conjunto de ' + str(m) + ' regras que classifique corretamente todos os pacientes.')
'''
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))


'''{(xP I≤42.09,1,p, F),(xP I≤42.09,1,n, T),(xP I≤42.09,1,s, F),(xP I≤42.09,2,p, F),(xP I≤42.09,2,n, F),(xP I≤42.09,2,s, T)
(xP I≤70.62,1,p, T),(xP I≤70.62,1,n, F),(xP I≤70.62,1,s, F),(xP I≤70.62,2,p, F),(xP I≤70.62,2,n, F),(xP I≤70.62,2,s, T)
(xGS≤37.89,1,p, F),(xGS≤37.89,1,n, F),(xGS≤37.89,1,s, T),(xGS≤37.89,2,p, F),(xGS≤37.89,2,n, T),(xGS≤37.89,2,s, F)'''