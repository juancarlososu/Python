import random

def generar_contrasena():
    mayusculas = ["A","B","C","D","E","F","G"]
    minusculas = ["a","b","c","d","e","f","g"]
    simbolos = ["!","%","$","+","@"]
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    
    caracteres = mayusculas + minusculas + simbolos + numeros
    
    contrasena = []
    
    for i in range(15): #se define el numero de caracteres de las contraseñas
        caracter_random =  random.choice(caracteres) #.choice elige una poscisión de todos los caracteres
        contrasena.append(caracter_random) #almacena el caracter en la contrasena
    
    contrasena = ''.join(contrasena) #se genera un string a aprtir de una lista
    
    return contrasena #retorna valor para almacenarlo en def run -> contrasena
    
    
def run():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)


if __name__ == '__main__':
    run()