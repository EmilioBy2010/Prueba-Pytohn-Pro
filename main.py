my_dict = {
            "ITERACION": "Realizar una acción varias veces",
            "BUG": "Problema en el código que hace que no se ejecute correctamente",
            "CONSOLA": "Ventana, normalmente negra, donde se puede trabajar desde la línea de comandos",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in my_dict.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(my_dict[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print ("no existe esta palabra")
