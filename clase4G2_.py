class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []

    def verDatosPaciente(self,c):
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
            
    def verNumeroPacientes(self):
        print("En el sistema hay: "+ str(len(self.__lista_pacientes)) + "pacientes")
                
    def ingresarPaciente(self,p):       
        self.__lista_pacientes.append(p)

def main():
                
    sis = Sistema()

    while True:
        opcion = int(input("Ingrese 0 para salir, 1 para ingresar nuevo paciente, 2 ver paciente: "))
        if opcion == 1:
            print("A continuación se solicitaran los datos...")
            # 1- solicito los datos por teclado
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            # 2- creo el objeto Paciente y le asigno los datos
            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)
            sis.ingresarPaciente(pac)
            
        elif opcion == 2:
            sis.verNumeroPacientes()
        elif opcion == 3:
            c = int(input("Ingrese la cedula a buscar: "))
            p = sis.verDatosPaciente(c)
            print("Nombre: " + p.verNombre())
            print("Cedula: " + str(p.verCedula()))
            print("Genero: " + p.verGenero())
            print("Servicio: " + p.verServicio())
        elif opcion !=0:
            continue
        else:
            break
    


