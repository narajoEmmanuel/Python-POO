#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 15/5/2019  8:00am 
#Fecha de última Modificación: 18/5/2019  5:00pm
#Versión: 3.7.2
#Principal

#importación de librerias
from clases import*
from archivos import*
from funciones import*

#Definicion de funciones:
print("BiblioTECa".center(26,"-"))
def menu():
      try:
            while True:
                  libro=Libro()
                  print("\n"+"Menú Principal".center(26,"-"))
                  print("1-Agregar Libro")
                  print("2-Modificar Libro")
                  print("3-Mostrar Libro")
                  print("4-Eliminar Libro")
                  print("5-Terminar")
                  opcion=int(input("\nEscoja una opción: "))
                  print("-"*29)
                  if opcion==1:
                        isbn=input("Ingrese el ISBN: ")
                        agregarLibroAux(biblioteca,libro,isbn)
                  elif opcion==2:
                        codigo=input("Ingrese el ISBN del libro que desea modificar: ")
                        modificarLibro(biblioteca,libro,codigo)
                  elif opcion==3:
                        menuSecundario()
                  elif opcion==4:
                        codigo=input("Ingrese el ISBN del libro que desea eliminar: ")
                        eliminarLibro(biblioteca,codigo)
                  elif opcion==5:
                        grabar("biblioTECa",biblioteca)
                        break
      except ValueError:
            menu()
                                                           
def menuSecundario():
      print("\n"+"Menú Secundario".center(26,"-"))
      print("1.Mostrar todos los libros registrados")
      print("2.Buscar por ISBN")
      try:
            opcionMenuSec=int(input("\nEscoja una opción: "))
            if opcionMenuSec==1:
                  mostrarTodosLibros(biblioteca)
            elif opcionMenuSec==2:
                  codigo=input("Ingrese el ISBN del libro que desea mostrar: ")
                  mostrarLibro(biblioteca,codigo)
            else:
                  menuSecundario()
      except ValueError:
            menuSecundario()
#------------------------------------------------------------------------------------------------------------

#Instanciar variables
libro=Libro()

#Programa Principal
biblioteca=[]
biblioteca=lee("biblioTECa",biblioteca)
menu()
