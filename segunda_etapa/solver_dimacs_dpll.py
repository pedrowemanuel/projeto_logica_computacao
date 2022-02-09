import sys
from lib.functions import *
from lib.semantics import *

def main(args):
    
    path_arquivo = "./DIMACS/Fórmulas Satisfatíveis/"
    
    if(len(args) != 2):
        print("Parâmetros incorretos: digite -> python solver_dimacs_dpll.py nome_do_arquivo.cnf")
        sys.exit()

    nome_arquivo = args[1] #nome do arquivo
    
    # converter arquivo dimacs para formula em formato de lista
    formula = dimacs_para_cnf(path_arquivo+nome_arquivo)   
        
    # resolver a fórmula usando o algotimo dpll
    resultado = DPLL(formula)

    if resultado != False:
        print(resultado)
    else:
        print('A fórmula é insatisfatível')

    return 0 

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    