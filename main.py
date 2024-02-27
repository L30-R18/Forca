import random
import forca
from colorama import Fore, Style

from colorama import Fore

def main():
    while True:
        sair = int(input("Digite 1 para continuar e digite 0 para sair: "))

        if sair == 0:
            break
        
        palavra = forca.lerPalavraArquivo()

        tentativas = random.randint(3, 3 * forca.contarCaracteres(palavra))

        print("-------------------------------")
        forca.pintar_palavra("A palavra possui ", Fore.BLUE)
        print(len(palavra), end='')
        forca.pintar_palavra(" letras.", Fore.BLUE)
        print("\n\n")

        for i in range(tentativas):

            forca.pintar_palavra("Restam ", Fore.BLUE)
            print(tentativas - i, end='')
            forca.pintar_palavra(" tentativas.", Fore.BLUE)
            print()

            palpite = input("Digite palpite: ")

            if len(palpite) != len(palavra):
                forca.pintar_palavra("Erro, palavra fornecida não possui número de caracteres correto! ! !\n", Fore.RED)
                continue

            if forca.verificaPalpite(palpite, palavra):
                forca.pintar_palavra("\n\n__________________________________________________-\n\n", Fore.BLUE)
                forca.pintar_palavra("| Parabéns, você descobriu a palavra certa! ! !    |\n", Fore.BLUE)
                forca.pintar_palavra("|__________________________________________________|\n\n", Fore.BLUE)
                break
            print()
        else:
            print("A palavra correta era:")
            forca.pintar_palavra(palavra, Fore.GREEN)
            print()
            print("-------------------------------")

if __name__ == "__main__":
    main()
