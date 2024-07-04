import random
from palavraforca import palavras 
def jogo_da_forca():
    
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ["_"] * len(palavra_secreta)
    letras_chutadas = []
    enforcou = False
    acertou = False
    erros = 0

    print("Bem-vindo ao jogo da forca!")
    print("A palavra secreta é: ", " ".join(letras_acertadas))

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.lower()

        if(len(chute) != 1):
            print("Digite apenas uma letra.")
            continue
        elif(chute in letras_chutadas):
            print("Você já tentou essa letra.")
            continue
        elif(not chute.isalpha()):
            print("Digite apenas letras.")
            continue

        letras_chutadas.append(chute)

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(" ".join(letras_acertadas))

    if(acertou):
        print("Parabéns, você ganhou!")
    else:
        print("Que pena, você perdeu!")

jogo_da_forca()
