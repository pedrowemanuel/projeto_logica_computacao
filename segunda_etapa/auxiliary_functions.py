def log(message):
    with open('log_erro.txt', 'a') as arquivo:
        arquivo.write(str(message) + '\n')
    arquivo.close()

def separar_dados(dados):

    atributos = []
    pacientes_com_patologia = []
    pacientes_sem_patologia = []

    for linha in range(len(dados)):

        quantidade_de_colunas = len(dados[linha])
        dados_paciente = []

        for coluna in range(quantidade_de_colunas):
            if linha == 0:
                if coluna < (quantidade_de_colunas - 1):
                    atributos.append(dados[linha][coluna])
            else:
                if coluna == (quantidade_de_colunas - 1):
                    dados_paciente.append(int(dados[linha][coluna].replace("\n","")))
                else:
                    dados_paciente.append(int(dados[linha][coluna]))

        if dados_paciente != []:
            if dados_paciente[quantidade_de_colunas - 1] == 0:
                dados_paciente.pop()
                pacientes_sem_patologia.append(dados_paciente)
            elif dados_paciente[quantidade_de_colunas - 1] == 1:
                dados_paciente.pop()
                pacientes_com_patologia.append(dados_paciente)
    return [atributos, pacientes_com_patologia, pacientes_sem_patologia]

def montarRegras(solucao):

    regras = {}

    for i in solucao:
        partes_resposta = i.split("_")
        if partes_resposta[0] == 'C':
            continue
        if solucao[i]:
            numero_regra = partes_resposta[2]
            if numero_regra not in regras:
                regras[numero_regra] = []
            if partes_resposta[3] == "n":
                partes_atributo = partes_resposta[1].split(" ")
                regras[numero_regra].append(partes_atributo[0]+" > "+partes_atributo[2])
            elif partes_resposta[3] == "p":
                regras[numero_regra].append(partes_resposta[1])

    regras_string = "{"

    for numero in range(1, len(regras) + 1):
        regras_string += str(regras[str(numero)]) + u"\u21d2" + " P"
        if(int(numero) < len(regras)):
            regras_string += ",\n"

    regras_string += "}"

    return regras_string

def interpretacao_cnf_para_dicionario(interpretacao):
    """ converte uma valoração no formato de lista(cnf) para dicionário:
        Ex: [1,2,-3] ===> {1:True,2:True,3:False} """
    
    interpretacao_convertida = {}      
    for literal in interpretacao:
        if int(literal) >= 0:
            interpretacao_convertida[literal] = True
        else:
            interpretacao_convertida[-literal] = False

    return interpretacao_convertida

def substituir_valores_por_atomos(interpretacao, atomos):
    """ substitui as chaves de um dicionario por seus respectivos atomos """
    
    interpretacao_convertida = {}      
    for atomo in interpretacao.keys():
        interpretacao_convertida[atomos[atomo]] = interpretacao[atomo]

    return interpretacao_convertida