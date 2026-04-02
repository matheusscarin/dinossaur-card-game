import random
import time
from cartas import baralho

def embaralhar(baralho):
    random.shuffle(baralho)
    return baralho

def distribuir(baralho):
    metade = len(baralho) // 2
    baralho_um = baralho[:metade]
    baralho_dois = baralho[metade:]
    return baralho_um, baralho_dois

def mostrar_carta(carta):
    print(f"""
    {carta["nome"]}
    1 - Comprimento: {carta["comprimento_m"]:.2f}
    2 - Velocidade: {carta["velocidade_kmh"]:.2f}
    3 - Peso: {carta["peso_kg"]:.2f}
    4 - Força: {carta["forca"]}
    """)

def escolher_atributo(carta):
    mostrar_carta(carta)
    
    while True:
        try:
            escolha = int(input("\nEscolha um atributo (1 - 4): "))    
            if escolha >= 1 and escolha <= 4:
                break
            else:
                print("\nEscolha Inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("\nEscolha Inválida! Digite um número entre 1 e 4.")

    if escolha == 1:
        return "comprimento_m"
    elif escolha == 2:
        return "velocidade_kmh"
    elif escolha == 3:
        return "peso_kg"
    elif escolha == 4:
        return "forca"

def resolver_super_trunfo(mao_vencedor, mao_perdedor, carta_j1, carta_j2, nome_vencedor):
    mostrar_carta(carta_j1)
    time.sleep(3)
    print("\nCarta do Adversário:")
    mostrar_carta(carta_j2)
    mao_vencedor.append(carta_j1)
    mao_vencedor.append(carta_j2)
    time.sleep(3)
    print(f"{nome_vencedor} venceu a rodada com a carta Super Trunfo!")
    return nome_vencedor

def jogar_rodada(mao_j1, mao_j2, vez_do_jogador):
    carta_j1 = mao_j1[0]
    carta_j2 = mao_j2[0]
    del mao_j1[0]
    del mao_j2[0]

    if carta_j1["super_trunfo"]:
        return resolver_super_trunfo(mao_j1, mao_j2, carta_j1, carta_j2, "JOGADOR")
    elif carta_j2["super_trunfo"]:
        return resolver_super_trunfo(mao_j2, mao_j1, carta_j1, carta_j2, "MAQUINA")
    else:
        if vez_do_jogador == "JOGADOR":
            atributo = escolher_atributo(carta_j1)
        else:
            mostrar_carta(carta_j1)
            atributos = ["comprimento_m", "velocidade_kmh", "peso_kg", "forca"]
            atributo = random.choice(atributos)
            print(f"\nA Máquina escolheu: {atributo}")
            time.sleep(5)
    
        print("\nCarta do Adversário:")
        mostrar_carta(carta_j2)

        valor_j1 = carta_j1[atributo]
        valor_j2 = carta_j2[atributo]

        if valor_j1 > valor_j2:
            mao_j1.append(carta_j1)
            mao_j1.append(carta_j2)
            print("O Jogador venceu a rodada!")
            return "JOGADOR"
        elif valor_j2 > valor_j1:
            mao_j2.append(carta_j2)
            mao_j2.append(carta_j1)
            print("A Máquina venceu a rodada!")
            return "MAQUINA"
        else:
            mao_j1.append(carta_j1)
            mao_j2.append(carta_j2) 
            print("Empate! Cada um fica com sua carta.")
            return vez_do_jogador