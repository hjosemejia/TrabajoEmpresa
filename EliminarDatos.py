import os
global dempleados
global templeados
global lempleados
global delemple
dempleados = {}
templeados = ()
lempleados = []
delemple = {}

def ingresarDatos():
    pass

            
def imprimirDatos():
    print("LISTA DE EMPLEADOS")
    print("-----------------------------")
    for x in range(len(lempleados)):
        templeados = lempleados[x]
        print(f"EMPLEADO {x+1}")
        dempleados['IDENTIDAD']  = templeados[0]
        dempleados['NOMBRE'] = templeados[1]
        dempleados['CARGO'] = templeados[2]
        dempleados['SALARIO'] = templeados[3]
        for key, valor in dempleados.items():
            print(f"{key}: {valor}")
        print("--------------------------")
    

def eliminarDatos():
    print("****************************************")
    print("|** __ ELIMINAR POR IDENTIFICACION __ **|")
    print("")
    varia = int(len(lempleados))
    x = 0
    delemple['IDENTIDAD']  = input("IDENTIFICACIÓN: ")
    print(f"EMPLEADO A ELIMINAR POR IDENTIFICACION: {delemple['IDENTIDAD']}")
    while x < varia:
        templeados = lempleados[x]
        dempleados['IDENTIDAD'] = templeados[0]
        dempleados['NOMBRE'] = templeados[1]
        dempleados['CARGO'] = templeados[2]
        dempleados['SALARIO'] = templeados[3]
        if delemple['IDENTIDAD'] in dempleados['IDENTIDAD']:
            for key, valor in dempleados.items():
                print(f"{key}: {valor}")
            del lempleados[x]
            x = varia + 1
        else:
            x += 1

def consultarDatos():
    pass


def menu():
    os.system("pause")
    os.system("cls")
    while (True):
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
            ingresarDatos()
        elif    opc == 2:
            print("IMPRIMIR DATOS")
            imprimirDatos()
        elif    opc == 3:
            print("ELIMINAR DATOS")
            eliminarDatos()
        elif    opc == 4:
            print("CONSULTAR DATOS")
            consultarDatos()
        elif    opc == 5:
            print("GRACIAS POR VISITAR NUESTRO SOFTWARE")
            break
        os.system("pause")
        os.system("cls")


def main():
    menu()

if __name__=="__main__":
    main()