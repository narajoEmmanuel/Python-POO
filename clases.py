#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 15/5/2019  8:00am 
#Fecha de última Modificación: 18/5/2019  5:00pm
#Versión: 3.7.2
#Clases

#importación de librerias
from funciones import*
#Definición de Clases

class Libro:

    
    def __init__(self):
        """
        Funcionamiento:Método constructor de la clase Libro
        Entradas: No tiene
        Salidas: No tiene
        """
        self.isbn=""
        self.nombre=""
        self.annoPub=0
 #--------------------------------------------------------------
    def setISBN(self,pisbn):
        """
        Funcionamiento: Asigna el isbn al atributo 'isbn'
        Entradas: isbn del libro
        Salidas: No tiene
        """
        self.isbn=pisbn

    def getISBN(self):
        """
        Funcionamiento: permite obtener el valor almacenado en ese atributo
        Entradas: No tiene
        Salidas: isbn del libro
        """
        return self.isbn
#--------------------------------------------------------------
    def setNombre(self,pnombre):
        """
        Funcionamiento: Asigna el nombre al atributo 'nombre'
        Entradas: nombre del libro
        Salidas: No tiene
        """
        self.nombre=pnombre

    def getNombre(self):
        """
        Funcionamiento: permite obtener el valor almacenado en ese atributo
        Entradas: No tiene
        Salidas: nombre del libro
        """
        return self.nombre
#--------------------------------------------------------------  
    def setAnno(self,pannoPub):
        """
        Funcionamiento: Asigna el año de publicación al atributo 'annoPub'
        Entradas:  año de publicación del libro
        Salidas: No tiene
        """
        self.annoPub=pannoPub

    def getAnno(self):
        """
        Funcionamiento: permite obtener el valor almacenado en ese atributo
        Entradas: No tiene
        Salidas: año de publicación del libro
        """
        return self.annoPub
 #--------------------------------------------------------------
    def mostrar(self):
        """
        Funcionamiento: Muestra el contenido de los atributos del objeto
        Entradas:No tiene
        Salidas: muestra los datos almacenados
        """  
        return self.isbn,self.nombre,self.annoPub
   
