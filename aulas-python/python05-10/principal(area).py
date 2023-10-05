import area 
print("Qual area deseja escolher? ")
print('(1) retangulo')
print('(2) triangulo')
print('(3) circulo')
escolha= int(input('Numero da escolha: '))
if escolha ==1:
    lado= float('Digite o lado: ')
    altura=float ('Digite a altura: ')
    resultado= area.area_retangulo(lado, altura )
    print('Area do retangulo: {:.2f}'.format(resultado))
elif escolha==2:
    lado= float('Digite o lado: ')
    altura=float ('Digite a altura: ')
    resultado= area.area_triangulo(lado, altura)
    print('Area do triangulo: {:.2f}'.format(resultado))
elif escolha==3: 
    raio= ('Digite o valor do raio: ')
    resultado= area.area_circulo(raio)
    print('Area do circulo: {:.2f}'.format(resultado))
else:
    print('Opção invalida')
