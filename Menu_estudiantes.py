from crudmysql import MySQL
from env import variables

objetoMysql= MySQL(variables)

def menu_principal():
    while True:
        print("/******************* Menu Principal ************************/")
        print(" 1. Validar Estudiante ")
        print(" 2. Cargar Materia ")
        print(" 3. Actualizar calificacion ")
        print(" 4. Salir ")

        opcion = input("Ingresa Opcion: ")
        if opcion == '1': #Validar estudiante
            numerocontrol= input("Ingresa Numero Control: ")
            clave= input("Ingresa la clave: ")
            validar_Estudiante(numerocontrol,clave)
            
        elif opcion == '2': #Cargar Materia
            numControl = input("Ingresa Numero Control: ")
            clave = input("Ingresa Clave: ")
            cargar_Materia(numControl,clave)
        elif opcion == '3': #Actualizar Calificacion
            numControl= input("Ingresa Numero Control: ")
            mate = input("Ingresa Nombre Materia: ")
            Actualizar_calificacion(numControl,mate)
        elif opcion == '4': #Salir
            print("Adios !!!")
            break
        else:
            print("Ingresa una opcion valida (1-4)")

def validar_Estudiante(numcontrol,clave):
    objetoMysql.myConexionSQL()
    miConsulta=f"Select * from usuarios where control='{numcontrol}' and  clave ='{clave}'"
    valores = objetoMysql.consulta(miConsulta)
    if valores:
        MostrarMaterias(numcontrol)
    else:
        print("Estudiante no encontrado")

def MostrarMaterias(numcontrol):
    acu=0
    sql_materias="SELECT E.nombre, K.materia, K.calificacion " \
                 "FROM estudiantes E, kardex K " \
                 f"WHERE E.control = K.control and E.control = '{numcontrol}';"
    resp = objetoMysql.consulta(sql_materias)
    if resp:
        print("Estudiante ",resp[0][0])
        for mat in resp:
            if mat is not None:
                print("Materia: ",mat[1], "Calificacion: ",mat[2])
                acu+=mat[2]
                prom= acu/len(resp)
        print("Promedio General: ",prom)
        print()
        objetoMysql.desconectar_mysql()
        


def cargar_Materia(numcontrol,clave):
    objetoMysql.myConexionSQL()
    miConsulta=f"Select * from usuarios where control='{numcontrol}' and  clave ='{clave}';"
    valores = objetoMysql.consulta(miConsulta)
    if valores:
        nombre_materia= input("Nombre Materia: ")
        consulta = f"Insert into kardex (control,materia,calificacion) values ('{numcontrol}','{nombre_materia}',0);"
        dat = objetoMysql.consulta(consulta)
        print("Carga Materia completa")
        print()
    else:
        print("El estudiante no existe")
        print()
    objetoMysql.desconectar_mysql()

def Actualizar_calificacion(numerocontrol,materia):
    objetoMysql.myConexionSQL()
    consulta = f"Select * from Kardex where control = '{numerocontrol}' and materia = '{materia}'; "
    ejecutarConsulta = objetoMysql.consulta(consulta)
    if ejecutarConsulta:
        cali =float(input("Ingresa Calificacion:"))
        sql_actuali_prom =f"UPDATE kardex set calificacion={cali} where control='{numerocontrol}' and materia= '{materia}';"
        objetoMysql.consulta(sql_actuali_prom)
        print("Actualizacion exitosa")
        print()
    else:
        print("Materia No encontrada")
        print()
    objetoMysql.desconectar_mysql()



menu_principal()