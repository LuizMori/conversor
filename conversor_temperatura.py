
#class Temperatura:

    #def __init__(self, celsius, fahrenheit):
        #self.__celsius = celsius
        #self.__fahrenheit = fahrenheit

    #def temperatura_celsius(self, celsius):
        #self.__celsius = input("Digite a temperatura em Celsius: ")
        #self.__fahrenheit = int(celsius) * 9/5 + 32
        #print("A temperatura convertida de {} para {} é de: ".format(self.__celsius, self.__fahrenheit))

    #def formula_celsius(self, celsius):
        #self.__fahrenheit = celsius * 9/5 + 32
        #return
        #print("A temperatura convertida de {} para {} é de: ".format(self.__celsius, self.__fahrenheit))

temperatura_celsius = input("Digite a temperatura em Celsius: ")
celsius = temperatura_celsius
fahrenheit = int(celsius) * 9/5 + 32

print("A temperatura em fahrenheit é {}ºF".format(fahrenheit))

temperatura_fahrenheit = input("Digite a temperatura em Fahrenheit: ")
fahrenheit = temperatura_fahrenheit
celsius = (int(fahrenheit) - 32) * 5 / 9

print("A temperatura em celsius é {}ºC".format(celsius))





