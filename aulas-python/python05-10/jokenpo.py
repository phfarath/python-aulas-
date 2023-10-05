import random

def jogada_comp(lista_jogadas):
    jogada=random.choice(lista_jogadas)
    return jogada

def vencedor(jogada_pc , jogada_usuario):
    if jogada_pc==1 and jogada_usuario==3 or jogada_pc==2 and jogada_usuario==1 or jogada_pc==3 and jogada_usuario==2:
        print('Pc venceu! Vitoria dos robos')
    elif jogada_usuario==1 and jogada_pc==3 or jogada_usuario==2 and jogada_pc==1 or jogada_usuario==3 and jogada_pc==2:
        print('Você venceu dos robos !')
    elif jogada_pc==jogada_usuario:
        print("Empate !")