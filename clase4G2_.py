# Creamos la clase paciente
class Paciente():
    # Inicializamos los atributos de persona
    def __init__(self):
        self.__nombre= ""
        self.__cedula= 0
        self.__genero= ""
        self.__servicio = ""
    # Setters
    def asignarNombre(self,nombre):
        self.__nombre = nombre
    def asignarCedula(self,cedula):
        self.__cedula = cedula
    def asignarGenero(self,genero):
        self.__genero = genero
    def asignarServicio(self, servicio):
        self.__servicio = servicio
    # Getters 
    def verNombre(self): 
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verServicio(self):
        return self.__servicio
    # Deleters
    def borrarNombre(self):
        del self.__nombre
    def borrarCedula(self):
        del self.__cedula
    def borrarGenero(self):
        del self.__genero
    def borrarServicio(self):
        del self.__servicio

class Sistema():
    # Inicializamos los atributos de sistema
    def __init__(self):
        self.__lista_pacientes = [] # Creamos una lista vacia para ir añadiento los pacientes que van ingresando a mi sistema
    
    # Definimos una funcion para ingresar paciente
    def ingresar_paciente(self,p):
        self.__lista_pacientes.append(p)
    
    # Definimos una funcion para ver la cantidad de pacientes en el sistema
    def verCantidad_pacientes(self):
        print(f"\nEn el sistema se encuentran {len(self.__lista_pacientes)} pacientes.") # Usamos el metodo len para saber el numero de pacientes que he agregado a la lista
   
    # Definimos una funcion para visualizar la informacion del paciente que el usuario quiera buscar al ingresar la cedula por teclado
    def verPaciente(self,cc):
        # La variable pac recorre la lista de pacientes 
        for pac in self.__lista_pacientes:
            if cc == pac.verCedula():
                # Si la cedula solicitada está, muestra la informacion del paciente en pantalla
                verif = True
                print(f"""
                Nombre= {pac.verNombre()},
                Cedula= {pac.verCedula()},
                Género= {pac.verGenero()},
                Servicio= {pac.verServicio()}""")
            else:
                verif = False   
        if verif == False:
            print("\nEl paciente no se encuentra registrado en el sistema")
            
def main():
# Crear una instancia de la clase sistema para tomar sus atributos y funciones y modificarlo 
    System= Sistema()

    while True:
        menu=input("""\nIngrese una opción:
                1. Ingresar un paciente
                2. Numero de pacientes ingresados
                3. Datos del paciente
                4. Salir 
                """)
        if menu == "1":
            print("\nSeñor usuario usted ha seleccionado la opcion ingresar paciente, por favor diligencie la siguiente información.")
            # Le solicito los datos al usuario por teclado
            nombre = input("Ingrese su nombre: ")
            cedula = int(input("Ingrese su cedula: "))
            genero = input("Ingrese su genero: ")
            servicio = input("Ingrese el servicio donde está alojado: ")
            # Creo el objeto paciente y le asigno los datos
            p = Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)
            System.ingresar_paciente(p)
            print("\nEl paciente ha sido ingresado a la base de datos de manera exitosa.")

        elif menu == "2":
            print("\nSeñor usuario usted ha seleccionado la opcion ver cantidad de pacientes registrados en el sistemas")
            System.verCantidad_pacientes()
        elif menu == "3":
            print("\nSeñor usuario usted ha seleccionado la opcion ver paciente, por favor diligencie la siguiente información.")
            cc = int(input("\nIngrese la cedula del paciente a buscar: "))
            info = System.verPaciente(cc)
            
        elif menu == "4":
            print("\nSaliendo, gracias por usas nuestros servicios")
            break
        else:
            print("\nIngreso una opción no valida, intente de nuevo.")
            
# Hacemos llamado a la función main
if __name__ == "__main__":
    main()
    


