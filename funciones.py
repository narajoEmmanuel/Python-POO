#Elaborado por: Emmanuel Naranjo Blanco y Fabio Navarro Naranjo
#Fecha de Creación: 15/5/2019  8:00am 
#Fecha de última Modificación: 18/5/2019  5:00pm
#Versión: 3.7.2
#Funciones

from clases import*
from archivos import*

def agregarLibroAux(biblioteca,libro,isbn):
    """
    Funcionamiento: verificar si el dato ingresado ya había sido almacenado anteriormente.
    Entradas: isbn, lista biblioteca y objeto libro.
    Salidas: libro agregado al archivo.
    """
    x=0
    while x<len(biblioteca):
        if isbn==biblioteca[x].getISBN():
            print("El ISBN ingresado ya se encuentra registrado.")
            return
        x+=1
    return agregarLibro(biblioteca,libro,isbn)
    

def agregarLibro(biblioteca,libro,isbn):#1
    """
    Funcionamiento: agregar datos de un objeto libro a una un archivo.
    Entradas: isbn, lista biblioteca y objeto libro.
    Salidas: libro agregado al archivo.
    """
    libro.setISBN(isbn)
    nombre=input("Nombre: ")
    libro.setNombre(nombre)
    anno=input("Año de Publicación: ")
    if anno.isdigit():
        libro.setAnno(anno)
    else:
        print("El año de publicación debe ser un número")
        return agregarLibro(biblioteca,libro,isbn)
    biblioteca.append(libro)
    grabar("biblioTECa",biblioteca)
    print("\nDatos guardados exitosamente!")
    return
#-------------------------------------------------------------
def modificarLibro(biblioteca,libro,codigo):#2
    """
    Funcionamiento: modificar un libro previamente ingresado.
    Entradas: lista biblioteca, objeto libro, isbn del libro a modificar.
    Salidas: nuevo objeto modificado.
    """
    x=0
    while x<len(biblioteca):
        if codigo==biblioteca[x].getISBN():
            print("Se van a modificar los siguientes datos:\n")
            mostrarLibro(biblioteca,codigo)
            print("\n")
            del(biblioteca[x])
            agregarLibro(biblioteca,libro,codigo)
            print("\n~El libro ha sido modificado correctamente.~")
            return
        x+=1
    print("El ISBN ingresado no está registrado.")
    return
    
#-------------------------------------------------------------   
def mostrarLibro(biblioteca,codigo):#3.1
    """
    Funcionamiento: muestra el objeto que corresponde al isbn ingresado.
    Entradas: lista biblioteca, isbn del libro a mostrar.
    Salidas: los datos correspondientes al libro.
    """
    x=0
    while x<len(biblioteca):
        if codigo==biblioteca[x].getISBN():
            print("ISBN: "+str(biblioteca[x].getISBN()))
            print("Nombre: "+str(biblioteca[x].getNombre()))
            print("Fecha de publicación: "+str(biblioteca[x].getAnno()))
            return
        x+=1
    print("El ISBN ingresado no está registrado.")
    return
        
#-------------------------------------------------------------
def mostrarTodosLibros(biblioteca):#3.2
    """
    Funcionamiento: muestra todos los datos de los objetos guardados.
    Entradas: lista biblioteca.
    Salidas: los datos de todos los objetos guardados.
    """
    if biblioteca==[]:
        print("No hay libros registrados.")
    x=0
    while x<len(biblioteca):
        print("_"*25)
        print("ISBN: "+str(biblioteca[x].getISBN()))
        print("Nombre: "+str(biblioteca[x].getNombre()))
        print("Fecha de publicación: "+str(biblioteca[x].getAnno()))
        x+=1
#-------------------------------------------------------------    
def eliminarLibro(biblioteca,codigo):#4
    """
    Funcionamiento: elimina un objeto guardado anteriormente.
    Entradas: lista bibliteca, isbn del libro a eliminar.
    Salidas: N/A
    """
    x=0
    while x<len(biblioteca):
        if codigo==biblioteca[x].getISBN():
            print("Se van a eliminar los siguientes datos:\n")
            mostrarLibro(biblioteca,codigo)
            print("\n")
            del(biblioteca[x])
            grabar("biblioTECa",biblioteca)
            print("El libro ha sido eliminado correctamente.")
            return
        x+=1
    print("El ISBN ingresado no está registrado.")
    return 



