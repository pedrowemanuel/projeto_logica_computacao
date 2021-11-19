def log(message):
    with open('log_erro.txt', 'a') as arquivo:
        arquivo.write(str(message) + '\n')