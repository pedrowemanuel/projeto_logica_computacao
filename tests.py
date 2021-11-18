import csv
import glob
alfabeto = ['a','b',"c",'d','e','f',"g",'h','i','j',"k",'l','m','n',"o",'p','q','r','s','t','u','v','w','x','y','z',".","_"]
arquivos = glob.glob("./pacientes/*.csv")
for arquivo in arquivos:
    file = arquivo.split("_")
    pacientes = int("".join(x for x in file[3] if x not in alfabeto))
    atributos = int("".join(x for x in file[2] if x not in alfabeto))
    with open(arquivo,"r") as leitura:
        reader = csv.reader(leitura)
        for arq in reader:
            print(arq)
