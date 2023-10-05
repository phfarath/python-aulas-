#Pedro Henrique Pontes Farath - rm 98608
import jokenpo

jogar_novamente=1
lista_jogadas=[1,2,3]

while jogar_novamente==1:

    print('-=' *25)
    print(f'{"*Começando jokenpo*":^50}')
    print('-=' *25)
    print('Qual movimento deseja fazer ? ')
    print('(1) pedra')
    print('(2) papel')
    print('(3) tesoura')
    jogada_usuario=int(input('Numero: '))
    jogada_pc=jokenpo.jogada_comp(lista_jogadas)

    if jogada_pc==1:
        print('O robo tirou pedra')
    elif jogada_pc==2:
        print('O robo tirou papel')
    elif jogada_pc==3:
        print('O robo tirou tesoura')


    verificacao= jokenpo.vencedor(jogada_pc, jogada_usuario)

    print('Deseja jogar novamente? (1)sim (2)não ')
    jogar_novamente=int(input())

