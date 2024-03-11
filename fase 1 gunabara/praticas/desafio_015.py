km = float(input('Digite a quantidade de kilometros rodados no carro: '))
time = int(input('Agora digite quantos dias o carro esteve em sua posse: '))
kmValue = km * 0.15
timeValue = time * 60
totalValue = timeValue + kmValue

print('Após rodar {}km durante {} dias, o valor do aluguel é de R${:.2f}.'.format(km, time, totalValue))
