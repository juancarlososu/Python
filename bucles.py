
# Ciclo Why
# def run():
#     LIMITE = 1000
#     contador = 0
#     potencia_2 = 2**contador
    
#     while potencia_2 < LIMITE:
#         print('2 elevado a ' + str(contador) + ' es igual a: '+ str(potencia_2))
#         contador =  contador + 1 contador += 1
#         potencia_2 = 2**contador
    
#Ciclo for

def run():
    # for i in range(1,10):
    #     print(i)
    
    nombre = input("Ingresa tu nombre: ")
    for letra in nombre:
        print(letra.upper())
    
    
    
if __name__ == '__main__':
    run()
