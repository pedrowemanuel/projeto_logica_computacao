import sys
from lib.functions import *
from lib.semantics import *
from auxiliary_functions import interpretacao_cnf_para_dicionario,montarRegras, substituir_valores_por_atomos
import time

def main(args):
    
    path_arquivo = "./DIMACS/Fórmulas Restrições Pacientes/"
    
    if(len(args) != 2):
        print("Parâmetros incorretos: digite -> python solver_dimacs_dpll.py nome_do_arquivo.cnf")
        sys.exit()

    nome_arquivo = args[1] #nome do arquivo
    
    # converter arquivo dimacs para formula em formato de lista
    [formula, atomos] = dimacs_para_cnf(path_arquivo+nome_arquivo)   
    
    # resolver a fórmula usando o algotimo dpll
    inicio_execucao = time.time() 
    resultado = DPLL(formula)
    fim_execucao = time.time()
    
    print("Tempo de execução: " + str(fim_execucao - inicio_execucao) + " s")

    if resultado != False:
        
        if atomos == {}:
            print(resultado)
        else:
            resultado = interpretacao_cnf_para_dicionario(resultado)
            resultado = substituir_valores_por_atomos(resultado, atomos)

            print("Regras:")
            print(montarRegras(resultado))

    else:
        print('A fórmula é insatisfatível')

    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    