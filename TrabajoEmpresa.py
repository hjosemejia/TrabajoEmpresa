


def menu():
    while(True):
        print("****************************************")
        print("|************ __ M E N U __ ***********|")
        print("| 1. INGRESAR LOS DATOS DEL EMPLEADO   |")
        print("| 2. IMPRIMIR LOS DATOS DEL EMPLEADO   |")
        print("| 3. ELIMINAR LOS DATOS DEL EMPLEADO   |")
        print("| 4. CONSULTAR LOS DATOS DEL EMPLEADO  |")
        print("| 5. SALIR DEL PROGRAMA                |")
        print("|______________________________________|")
        print("")
        opc = int(input("DIGITE LA OPCION QUE DESEA: "))
        if  opc == 1:
            print("INGRESAR DATOS")
        elif    opc == 2:
            print("IMPRIMIR DATOS")
        elif    opc == 3:
            print("ELIMINAR DATOS")
        elif    opc == 4:
            print("CONSULTAR DATOS")
        elif    opc == 5:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break

def main():
    menu()

if __name__=="__main__":
    main()