def palindromo(palabra):
    palabra = palabra.replace(' ','') #se quitan los espacios de la palabra
    palabra = palabra.lower() #todo a minusculas
    palabra_invertida = palabra[::-1] #invierte la palabra ejemplo: carlos | solrac - ana | ana
    if palabra == palabra_invertida:
        return True
    else:
        return False    


def run():
    palabra = input("Escriba una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es aplindromo")
    else:
        print("No es palindromo")

if __name__ == '__main__':
    run()