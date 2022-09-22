def play():
    print("*****************************")
    print("*Bem vindo ao jogo da Forca!*")
    print("*****************************")

    palavra_secreta = "carro".upper()

    enforcou = False
    acertou = False

    erros = 0

    acertos = ["_", "_", "_", "_", "_"]
    print(acertos)

    while not enforcou and not acertou:
        chute = input("Digite uma letra:  {}  ".format(acertos)).strip().upper()
        chute = chute.strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    acertos[index] = letra
                    print("Letra {} correta na posição {}".format(letra, index + 1))
                index += 1
        else:
            erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in acertos
        print(acertos)

    if acertou:
        print("Você ganhou")
    elif enforcou:
        print("Você perdeu")
    print("Fim do jogo!")



if __name__ == "__main__":
    play()
