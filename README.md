# Library Management System

This Python project, implemented in `biliotecaMenu.py`, is a simple Library Management System that allows users to add, modify, view, and delete book records. The code is modularized into separate files: `clases.py` for class definitions, `archivos.py` for file handling functions, and `funciones.py` for auxiliary functions.

## Usage
1. Run `biliotecaMenu.py`.
2. Follow the menu options to perform various actions on the library system.
3. The system data is stored in the `biblioTECa` file.

## File Structure

### biliotecaMenu.py
- **Functions:**
  - `menu()`: Displays a menu for users to perform various actions on the library system.
  - `menuSecundario()`: Displays a secondary menu for additional functionalities.
  - `main()`: The main execution function that initializes variables, reads the library data from a file, and starts the menu.

### clases.py
- **Classes:**
  - `Libro`: Represents a book with attributes such as ISBN, name, and publication year. Includes methods for setting and getting attributes and displaying book details.

### funciones.py
- **Functions:**
  - `agregarLibroAux(biblioteca, libro, isbn)`: Checks if a given ISBN already exists in the library and adds a new book to the library if not.
  - `agregarLibro(biblioteca, libro, isbn)`: Adds a new book to the library with user-provided details.
  - `modificarLibro(biblioteca, libro, codigo)`: Modifies an existing book in the library with updated details.
  - `mostrarLibro(biblioteca, codigo)`: Displays details of a specific book based on the provided ISBN.
  - `mostrarTodosLibros(biblioteca)`: Displays details of all books in the library.
  - `eliminarLibro(biblioteca, codigo)`: Deletes a book from the library based on the provided ISBN.

### archivos.py
- **Functions:**
  - `lee(file_name, data)`: Reads data from a file and returns the updated data.
  - `grabar(file_name, data)`: Writes data to a file.
