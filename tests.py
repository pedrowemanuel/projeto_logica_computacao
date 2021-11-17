import csv
import glob
dados = []
arquivos = glob.glob("./pacientes/*.csv")
for arquivo in arquivos:
    with open(arquivo,"r") as leitura:
        reader = csv.reader(leitura)
        for linha in reader:
            dados.append(linha)
print(dados)