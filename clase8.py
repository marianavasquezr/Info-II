class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__visita = {} 
    # metodos getters
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verVisita(self):
        return self.__visita
    #metodos setters
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def asignarVisita(self,v):
        self.__visita = v
    #metodos eliminar
    def eliminarNombre(self):
        del self.__nombre
    def eliminarCedula(self):
        del self.__cedula
    def eliminarGenero(self):
        del self.__genero
    def eliminarVisita(self):
        del self.__visita
        

class Visita:
    pass
class Indice:
    pass
class Sistema:
    pass
