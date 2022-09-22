def play():
    print("*****************************")
    print("*Bem vindo ao jogo da Forca!*")
    print("*****************************")

    palavra_secreta = "carro"

    enforcou = False
    acertou = False

    acertos = ["_", "_", "_", "_", "_"]
    print(acertos)

    while not enforcou and not acertou:
        chute = input("Digite uma letra:  {}  ".format(acertos))
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                acertos[index] = letra
                print("Letra {} correta na posição {}".format(letra, index + 1))
            index = index + 1
        print(acertos)


    print("Fim do jogo!")



if __name__ == "__main__":
    play()
