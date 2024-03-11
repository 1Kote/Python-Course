price = int(input('Digite o preço que dever receber o desconto: '))
priceDiscount = price*(5/100)
finalValue = price - priceDiscount

print('O novo preço com disconto de 5% é:{}!'.format(finalValue))