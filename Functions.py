####################################################################
# Alejandro Teajada 17854
# Diego Sevilla 17238
####################################################################
# Curso: Redes
# Programa: Functions.py
# Fecha: 08/2020
####################################################################
"""
    Functions.py: Archivo con funciones utiles para la interaccion con el usuario.
"""



# ----------------
# def function(params):
#    return null


def Wellcome():
    print("______________________________________________________________________________________")
    print("                     ¡   ¡   M   A   N   C   A   L   A   !   !                        ")
    print("______________________________________________________________________________________")
    print("--------------------------------------------------------------------------------------")
    print("                        #######################################                       ")
    print("                              ************************                                ")

def theEnd():
    print(" ")
    print("                                  ¡¡Bye Bye!!       ")
    print("                              ¡¡See you soon!! :D  ")
    print("                                                   ")
    print("                                   (o^^)o          ")
    print("                                    o(^^o)         ")
    print("                                   o(^^)o          ")
    print("                                                   ")
    print("                             ¡ Vuelve pronto !     ")
    print("                                                   ")

def read_integer():
    """ Asks for an integer value and return that value.
        If the input value is not an integer, the function asks for it again """
    while True:
        valor = input("Choose an option: ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("")
            print("¡Haa haaaa! ¡¿Didn't explode right?! ¡Try again! xp")
            print("")

