def run():
    diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3
    }
    
    #se imprime todo el diccionario
    # print(diccionario) 
    
    
    #se imprimen valores del diccionario
    # print(diccionario['llave1'])
    # print(diccionario['llave2'])
    # print(diccionario['llave3'])
    
    poblacion_paises = {
        'Argentina' : 49,
        'Mexico'    : 52,
        'Colombia'  : 68,
    }

    print(poblacion_paises)
    
    #se imprimen las llaves
    for pais in poblacion_paises.keys():
        print(pais)
        
    #se imprimen los valores
    for num_p in poblacion_paises.values():
        print(num_p)
    
    #se imprimen llaves y valores
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes.')
        
if __name__ == '__main__':
    run()
