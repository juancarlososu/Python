def conversor(pesos,valor_dolar):
    pesos = input("¿Cuantos pesos " + pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Binevenido al conversor de monedas 😁

1. Pesos colombianos
2. Pesos argentinos
3. Pesos mexicano

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos',3875)
elif opcion == '2':
    conversor('argentinos', 65)
elif opcion == '3':
   conversor('mexicamos', 20)
else:
    print("Ingresa una opcion correcta")

