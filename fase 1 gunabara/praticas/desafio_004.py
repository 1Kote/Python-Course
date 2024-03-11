var = input('Digite algo: ')

varType = type(var)
varAlpha = var.isalpha()
varDecimal = var.isdecimal()
print('O tipo é: {}!'.format(varType))
print('É alpha? r: {}'.format(varAlpha))
