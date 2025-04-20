from random import randint
from time import sleep
from operator import itemgetter
jogo = {"jogador1":randint(1,6),"jogador2": randint(1,6),"jogador3":randint(1,6),"jogador4":randint(1,6),"jogador5":randint(1,6),"jogador6":randint(1,6)}
ranking = {}
print("valores sorteados ")
for k,v in jogo.items():
    print(f"{k} tirou {v} no dado")
    sleep(0.5)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print("="*30)
for i,ran in enumerate(ranking):
    print(f"O {i+1}° lugar foi o {ran[0]} com o número {ran[1]}")
    sleep(0.5)