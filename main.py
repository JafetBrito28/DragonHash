# Importamos el módulo para limpiar la pantalla
import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función inicial del juego... 
def iniciar_nueva_partida():
    limpiar_pantalla()
    print("Bienvenido a DRAGON HASH, tu aventura comenzara despues de que respondas una serie de preguntas... ")
    input("Presiona Enter para continuar...")
    limpiar_pantalla()
    print("== INICIAR NUEVA PARTIDA ==")
    nombre = input("Ingresa el nombre de tu personaje: ")
    print("¿Que clase quieres ser?... podrias ser un mago... un guerrero...")
    input("Continuar...")
    clase = input("Selecciona la clase de tu personaje (Mago/Guerrero/Pícaro): ")
    
    # Aquí puedes realizar la lógica correspondiente para establecer la partida
    # y continuar con el juego en función de las respuestas del usuario
    print(f"Bienvenido/a, {nombre} el {clase}!")
    input("Presiona Enter para continuar...")
    capitulo_uno()

def capitulo_uno():
# Primer capítulo del juego
    limpiar_pantalla()
    print("== CAPÍTULO 1: DESIERTO ==")
    print("Te despiertas en medio de un desierto...")
    print("De repente, una esfinge aparece frente a ti.")
    print("La esfinge te hace una pregunta:")
    print("¿Cuál es el animal que camina gateando en la mañana,")
    print("erguido en la tarde y encorvado en la noche?")
    print("a) León")
    print("b) Hombre")
    print("c) Serpiente")
    respuesta = input("Ingresa la opción correcta (a/b/c): ")

    if respuesta.lower() == "b":
        limpiar_pantalla()
        print("¡Respuesta correcta!")
        print("La esfinge se alegra y te permite pasar.")
        input("continuar...")
        # Aquí puedes continuar con la lógica del juego, avanzando al siguiente capítulo
    else:
        limpiar_pantalla()
        print("¡Respuesta incorrecta!")
        print("La esfinge te ataca y pierdes el juego.")
        input("continuar...")

# Función para mostrar el arte ASCII del castillo
def mostrar_arte_ascii():
    print(r"""
𝘿𝙍𝘼𝙂𝙊𝙉 𝙃𝘼𝙎𝙃
    
┈┈┈┈▅┈┈▕▀┈┈┈┈┈┈┈
┈┈┈▕┈┈┈╱╲▕▀┈┈┈┈┈
┈┈┈╱╲┈┈▏▕╱╲┈┈┈┈
┈┈┈▏▕╱╲▏▎▏▕╱╲┈▃
┈╱╲▏▎▅▂▅▂▏▎▏▎▏▏
▂▏▎▏▕╭┳┳╮▏┊▏▕╱╲
▏▏┊▏▎┃┊┊┃▏▎▏▎▏▕
▇▆▅▃▂┻┻┻┻▂▃▅▆▇▉

𝑩𝒀 𝑯𝑨𝑺𝑯𝑴𝑨𝑳𝑾𝑨𝑹𝑬
                                     
    """)

# Mostramos la portada del juego
limpiar_pantalla()
mostrar_arte_ascii()
print("¡Bienvenido a DRAGON HASH!")
print("Presiona Enter para continuar...")
input()
# Mostramos el menú del juego
while True:
    limpiar_pantalla()
    print("== DRAGON HASH V 0.1 ==")
    print(r"""
                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \\//     ))#############\
   -###############\\    (oo)    //###############-
  -#################\\  / VV \  //#################-
 -###################\\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)
    """)
    print("== Menú ==")
    print("1. Iniciar nueva partida")
    print("2. Acerca de")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        iniciar_nueva_partida()
        # Aquí puedes implementar la lógica para la partida por capítulos
    elif opcion == "2":
        # Aquí puedes agregar el código para mostrar la información acerca del juego
        limpiar_pantalla()
        print("== ACERCA DE ==")
        print("DRAGON HASH es un juego de rol interactivo...")
        print("Creado por Hashmalware...")
        input("Presiona Enter para continuar...")
    elif opcion == "3":
        # Salir del juego
        print("¡Gracias por jugar a DRAGON HASH!")
        break
    else:
        print("Opción inválida. Por favor selecciona una opción válida.")
        input("Presiona Enter para continuar...")
