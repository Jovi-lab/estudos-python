"""
#Jogo de Adivinhação#

O intuíto do jogo é que você tente acertar um número aleatório de 1 a 100
Em um total de 7 tentativas.
Você pode jogar quantas vezes quiser, quando não quiser mais, você terá um retorno
Geral de como foi seu desempenho em todas as partidas jogadas.
"""
import random
total_geral = 0
partidas_jogadas = 0
partidas_ganhas = 0
partidas_perdidas = 0


def verificar_chute(chute, numero_secreto):
    if chute == numero_secreto:
        return "acertou"
    elif chute < numero_secreto:
        return "maior"
    else:
        return "menor"

def jogar():
    global partidas_ganhas, partidas_perdidas
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 7
    print("=== Jogo de Adivinhação ===")
    print(f"Advinhe o número entre 1 e 100. Você tem {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        chute = int(input(f"Tentativa {tentativas + 1}: "))
        tentativas += 1
        resultado = verificar_chute(chute, numero_secreto)
        
        if resultado == "acertou":
            print(f"Parabéns! Acertou em {tentativas} tentativa(s) !")
            partidas_ganhas += 1
            return tentativas 
        elif resultado == "maior":
            print("O número é maior.")
        else:
            print("O número é menor")
            partidas_perdidas += 1
    print(f"Suas tentativas acabaram. O númmero era {numero_secreto}.")
    partidas_perdidas += 1
    return tentativas


while True:
    partidas_jogadas += 1
    tentativas_usadas = jogar()
    total_geral += tentativas_usadas
    
    resposta = input("Quer jogar de novo? (s/n): ")
    if resposta.lower() != "s":
        print("PLACAR GERAL")
        print(f"Partidas jogadas: {partidas_jogadas}\n")
        print(f"Total de tentativas: {total_geral}")
        print(f"Partidas ganhas: {partidas_ganhas}")
        print(f"Partidas perdidas: {partidas_perdidas}")
        print("Obrigado por jogar! Até mais")
        break