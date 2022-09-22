import random


def play():
    print_apresentacao()

    palavra_secreta = set_palavra_secreta()

    enforcou = False
    acertou = False

    erros = 0
    tentativas_restantes = 0
    lista_acertos = ["_" for letra in palavra_secreta]

    print(lista_acertos)

    while not enforcou and not acertou:
        chute = input("Digite uma letra:  {}  ".format(lista_acertos)).strip().upper()
        chute = chute.strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    lista_acertos[index] = letra
                    print("Letra {} correta na posição {}".format(letra, index + 1))
                index += 1
        else:
            erros += 1
            tentativas_restantes = len(palavra_secreta) - erros
            print("Você tem {} tentativas restantes".format(tentativas_restantes))

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in lista_acertos
        print(lista_acertos)

    if acertou:
        print("Você ganhou")
    elif enforcou:
        print("Você perdeu")
    print("Fim do jogo!")


def print_apresentacao():
    print("*****************************")
    print("*Bem vindo ao jogo da Forca!*")
    print("*****************************")


def set_palavra_secreta():
    palavras = []
    with open("words.txt", "r") as arquivo_palavras:
        for palavra in arquivo_palavras:
            palavra = palavra.strip()
            palavras.append(palavra)

    rand_num = random.randrange(0, len(palavras) + 1)

    palavra_secreta = palavras[rand_num].upper()
    return  palavra_secreta

if __name__ == "__main__":
    play()
