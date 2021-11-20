import csv
import sys
def main(args):
    dados = []
    alfabeto = ['a','b',"c",'d','e','f',"g",'h','i','j',"k",'l','m','n',"o",'p','q','r','s','t','u','v','w','x','y','z',".","_"]
    if(len(args) != 3):
        print("Parametros incorretos: digite -> python main.py nome_do_arquivo.csv n_regras")
        sys.exit()
    if(int(args[2]) <= 0):
        print("Número de regras incorreto, precisa ser maior ou igual a 1")
        sys.exit()
    arquivo = args[1] #nome do arquivo
    m = args[2] #numero de regras
    nome_arquivo = arquivo
    arquivo = arquivo.split('_') #separando o arquivo em strings
    atributos = int("".join(x for x in arquivo[2] if x not in alfabeto))
    pacientes = int("".join(x for x in arquivo[3] if x not in alfabeto))
    try:
        with open(f"./pacientes/{nome_arquivo}", "r") as file:
            for linha in file:
                dados.append(linha)
        file.close()
    except FileNotFoundError:
        print("Arquivo nao encontrado. Digite novamente o nome do arquivo")    
    if(not dados):
        print("Arquivo vazio. Procure outro arquivo para pesquisar")
        sys.exit()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
