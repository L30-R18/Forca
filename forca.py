import random
from colorama import Fore, Style

def lerPalavraArquivo():
        
    random_value = random.randint(1, 4200)

    with open("palavras.txt", 'r') as arquivo:
        conteudo = arquivo.read()
        Lista_palavras = conteudo.split(';')

        return Lista_palavras[random_value]
    
def contarCaracteres(palavra: str):
    return len(palavra)

def pintar_palavra(palavra, cor):
    print(cor + palavra + Style.RESET_ALL, end='')

def pintar_palavra_multicolorida(palavra, cores):
    palavra_pintada = ""
    for caractere, cor in zip(palavra, cores):
        palavra_pintada += cor + caractere
    palavra_pintada += Style.RESET_ALL
    print(palavra_pintada)

def verificaPalpite(palpite, palavra):
    aux = palavra
    i = 0
    vitoria = 0
    cores = [Fore.BLACK]
    cores.remove(Fore.BLACK)
    while i < len(palavra):
        if palpite[i] == aux[i]:
            vitoria += 1
            cores.append(Fore.GREEN)
            i += 1
            continue
        elif palpite[i] in aux:
            cores.append(Fore.YELLOW)
        else:
            cores.append(Fore.RED)
        i += 1
    pintar_palavra_multicolorida(palpite, cores)
    if vitoria == len(palavra):
        return 1
    return 0
        

        