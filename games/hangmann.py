def play():
    print("*****************************")
    print("*Bem vindo ao jogo da Forca!*")
    print("*****************************")

    palavra_secreta = "carro".upper()

    enforcou = False
    acertou = False

    erros = 0

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

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in lista_acertos
        print(lista_acertos)

    if acertou:
        print("Você ganhou")
    elif enforcou:
        print("Você perdeu")
    print("Fim do jogo!")



if __name__ == "__main__":
    play()
