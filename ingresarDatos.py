import os
global dempleados
global templeados
global lempleados
global delemple
dempleados = {}
templeados = ()
lempleados = []
delemple = {}

def presentacion():
    print("****************************************")
    print("|** TRABAJO DE BASE DE DATOS AVANZADA **")
    print("|                                      |")
    print("|          JORGE ACOSTA PERTUZ         |")
    print("|           HECTOR MEJIA BUENO         |")
    print("|          MOISES RAMIREZ MARIN        |")
    print("|                                      |")
    print("|     ING. JAIDER QUINTERO MENDOZA     |")
    print("|               DOCENTE                |")
    print("|                                      |")
    print("|             UNIGUAJIRA               |")
    print("|       FACULTAD DE INGENIERIA         |")
    print("|        PROGRAMA DE SISTEMAS          |")
    print("|        DISTRITO DE RIOHACHA          |")
    print("|                2020                  |")
    print("|______________________________________|")


def ingresarDatos():
    varia = int(len(lempleados))
    x = 0
    if varia == 0:
        dempleados['IDENTIDAD']  = input("IDENTIFICACIÓN: ")
        dempleados['NOMBRE'] = input("NOMBRES Y APELLIDOS: ")
        dempleados['CARGO'] = input("CARGO: ")
        dempleados['SALARIO'] = input("SALARIO: ")
        templeados = ( dempleados['IDENTIDAD'], dempleados['NOMBRE'],  dempleados['CARGO'], dempleados['SALARIO'])
        empleados = list(templeados)
        lempleados.append(empleados)
    else:
        delemple['IDENTIDAD']  = input("IDENTIFICACIÓN: ")
        while x < varia:
            templeados = lempleados[x]
            dempleados['IDENTIDAD']  = templeados[0]
            if delemple['IDENTIDAD'] in dempleados['IDENTIDAD']:
                print("DOCUMENTO YA EXISTE")
                x = varia + 1
                romper = 1
            else:
                x += 1
                romper = 0
        if  romper == 0:
            dempleados['IDENTIDAD'] = delemple['IDENTIDAD']
            dempleados['NOMBRE'] = input("NOMBRES Y APELLIDOS: ")
            dempleados['CARGO'] = input("CARGO: ")
            dempleados['SALARIO'] = input("SALARIO: ")
            delemple['IDENTIDAD']  = dempleados['IDENTIDAD']
            templeados = ( dempleados['IDENTIDAD'], dempleados['NOMBRE'],  dempleados['CARGO'], dempleados['SALARIO'])
            empleados = list(templeados)
            lempleados.append(empleados)

            
def imprimirDatos():
    pass    

def eliminarDatos():
    pass

def consultarDatos():
    pass


def menu():
    presentacion()
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