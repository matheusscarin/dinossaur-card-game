import random
import time
from jogo import embaralhar, distribuir, jogar_rodada
from cartas import baralho

vez = random.choice(["JOGADOR", "MAQUINA"])
print(f"\nSorteio: {vez} começa!")
time.sleep(3)
baralho_embaralhado = embaralhar(baralho)
mao_j1, mao_j2 = distribuir(baralho_embaralhado)

while len(mao_j1) > 0 and len(mao_j2) > 0:
    print(f"\n Nova Rodada | Jogador: {len(mao_j1)} carta(s) | Máquina: {len(mao_j2)} carta(s)")
    vez = jogar_rodada(mao_j1, mao_j2, vez)
    time.sleep(10)

if len(mao_j2) == 0:
    print("\nO JOGADOR VENCEU A PARTIDA!")
elif len(mao_j1) == 0:
    print("\nA MÁQUINA VENCEU A PARTIDA!")