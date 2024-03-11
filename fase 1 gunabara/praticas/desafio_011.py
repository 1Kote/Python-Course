largura = int(input('Digite a largura da parade em metros: '))
altura = int(input('Agora digite a altura da parede em metros: '))
area = largura * altura
quantidaDeTinta = area / 2

print('A quantidade de tinta necessaria para printar {} metros quadrados é: {}!'.format(area, quantidaDeTinta))