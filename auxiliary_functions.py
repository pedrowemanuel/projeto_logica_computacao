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