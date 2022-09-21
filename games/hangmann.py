def play():
    print("*****************************")
    print("*Bem vindo ao jogo da Forca!*")
    print("*****************************")

    palavra_sercreta = "carro"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Digite uma letra:  ").lower()

        index = 1
        for letra in palavra_sercreta:
            if chute == letra:
                print("Letra {} correta na posição {}".format(letra, index))
            index = index + 1
        # print("jogando...")

    print("Fim do jogo!")



if __name__ == "__main__":
    play()
