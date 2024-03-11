celsius = float(input('Digite a temperatura desejada em graus celsius: '))
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print('A temperatura {}C é: {}F e {}K após sua conversão.'.format(celsius, fahrenheit, kelvin))