#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 15/5/2019  8:00am 
#Fecha de última Modificación: 18/5/2019  5:00pm
#Versión: 3.7.2
#Archivos

#importación de librerías
import pickle

#Definicion de funciones:

def grabar(biblioTECa,lista):
    """
    Entradas: nombre del archivo a grabar y la lista biblioteca
    Funcion: Graba un archivo
    Salidas: No tiene
    """
    try:
        f=open(biblioTECa,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo: ",inventarioMc)
    return

#--------------------------------------------------------------------------

def lee(biblioTECa,biblioteca):
    """
    Entradas: nombre del archivo a leer y la lista biblioteca.
    Funcion: Lee un archivo previamente nombrado
    Salidas: No tiene
    """
    try:
        f=open("biblioTECa","rb")
        biblioteca=pickle.load(f)
        f.close()
    except FileNotFoundError:
        grabar(biblioTECa,biblioteca)
    except:
        print("Error al leer el archivo: ", biblioTECa)
    return biblioteca

