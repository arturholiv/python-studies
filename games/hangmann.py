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
            # tentativas_restantes = erros - erros
            desenha_forca(erros)
            # print("Você tem {} tentativas restantes".format(tentativas_restantes))

        enforcou = erros == 7
        acertou = "_" not in lista_acertos
        print(lista_acertos)

    if acertou:
        imprime_mensagem_ganhou();
    elif enforcou:
        imprime_mensagem_enforcou(palavra_secreta)
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

    rand_num = random.randrange(0, len(palavras))

    palavra_secreta = palavras[rand_num].upper()
    return  palavra_secreta

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_enforcou(palavra_secreta):
    print("Você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_ganhou():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if __name__ == "__main__":
    play()
