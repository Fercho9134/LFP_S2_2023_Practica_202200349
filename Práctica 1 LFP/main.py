import tkinter as tk
import os
from tkinter import filedialog
from producto import Producto

class Metodos:

    def __init__(self):
        self.lista_productos = []

    def menu(self):
        print("╔═════════════════════════╗")
        print("║       Menú inicial      ║")
        print("╠═════════════════════════╣")
        print("║ 1. Cargar inventario    ║")
        print("║ 2. Cargar movimientos   ║")
        print("║ 3. Crear informe        ║")
        print("║ 4. Salir                ║")
        print("╚═════════════════════════╝")

        print("> Ingrese una opción: ", end="")
        opcion = input()
        self.seleccionar_opcion(opcion)

    def seleccionar_opcion(self, opcion):

        if opcion.isnumeric():
            opcion = int(opcion)
            if opcion == 1:
                self.cargar_inventario()
                
            elif opcion == 2:
                self.cargar_movimientos()
            elif opcion == 3:
                self.crear_informe()
            elif opcion == 4:
                print("\n> Gracias por usar el programa, Saliendo...")
                exit()
            else:
                print("\n> Opción inválida... Ingrese una opción correcta\n")
                self.menu()
        else:
            print("\n> Opción inválida... Ingrese una opción correcta\n\n")
            self.menu()
    
    def cargar_inventario(self):
        root = tk.Tk()
        direccion_archivo = filedialog.askopenfilename(filetypes=[("Archivos de Inventario", "*.inv")])
        root.destroy()
        #Ya se tiene la direccion del archivo .inv
        if direccion_archivo == "" or direccion_archivo == None:
            print("\n> No se seleccionó ningún archivo...")
            print("> Volviendo al menú inicial...\n")
            self.menu()
            return
        
        else:
            nombre, extension = os.path.splitext(direccion_archivo)

            if extension.lower() == ".inv":
                print("\n> Accediendo al archivo...")
                #Si todo esta correcto con el archivo, se procede a leerlo

                with open(direccion_archivo, "r") as archivo:

                    for linea in archivo:

                        cadena = linea.strip().replace(';', ' ')
                        informacion_producto = cadena.split(' ')
                        
                        instruccion = informacion_producto[0]
                        nombre_producto = informacion_producto[1]
                        cantidad_producto = informacion_producto[2]
                        precio_unitario = informacion_producto[3]
                        ubicacion = informacion_producto[4]
                        existe = False

                        if instruccion == "crear_producto":

                            if len(self.lista_productos) == 0:
                                producto_nuevo = Producto(nombre_producto, cantidad_producto, precio_unitario, ubicacion)
                                self.lista_productos.append(producto_nuevo)

                            else:
                                for producto in self.lista_productos:
                                    if producto.get_nombre() == nombre_producto and producto.get_ubicacion() == ubicacion:
                                        print("\nEl producto", nombre_producto, "ya existe en la ubicación", ubicacion, "por lo que no se sobreescibirá y se omitirá...")
                                        existe = True
                                        break
                                
                                if existe == False:
                                    producto_nuevo = Producto(nombre_producto, cantidad_producto, precio_unitario, ubicacion)
                                    self.lista_productos.append(producto_nuevo)
           
                        else: 
                            print("\nLa instrucción", instruccion, "no es válida, por lo que se omitirá...")


                    print("\n> Se ha cargado el inventario correctamente...\n")

            else:
                print("\n> El archivo seleccionado no es válido...")
                print("> Volviendo al menú inicial...\n")
                self.menu()
                return

        self.menu()
        return

        


    def cargar_movimientos(self):

        if (len(self.lista_productos) == 0):
            print("\n> No se ha cargado ningún inventario, por lo que no se puede cargar ningún movimiento...")
            print("> Volviendo al menú inicial...\n")
            self.menu()
            return
        
        root = tk.Tk()
        direccion_archivo = filedialog.askopenfilename(filetypes=[("Archivos de movimientos", "*.mov")])
        root.destroy()
        #Ya se tiene la direccion del archivo .mov
        if direccion_archivo == "" or direccion_archivo == None:
            print("\n> No se seleccionó ningún archivo...")
            print("> Volviendo al menú inicial...\n")
            self.menu()
            return
        
        else:
            nombre, extension = os.path.splitext(direccion_archivo)

            if extension.lower() == ".mov":
                print("\nAccediendo al archivo...")
                #Si todo esta correcto con el archivo, se procede a leerlo

                with open(direccion_archivo, "r") as archivo:

                    for linea in archivo:

                        cadena = linea.strip().replace(';', ' ')
                        informacion_movimiento = cadena.split(' ')
                        
                        instruccion = informacion_movimiento[0]
                        nombre_producto_movimiento = informacion_movimiento[1]
                        cantidad_producto_movimiento = informacion_movimiento[2]
                        ubicacion_movimiento = informacion_movimiento[3]
                        existe = False

                        if instruccion == "agregar_stock":

                            for producto in self.lista_productos:

                                if producto.get_nombre() == nombre_producto_movimiento and producto.get_ubicacion() == ubicacion_movimiento:
                                    cantidad_actual = int(producto.get_cantidad())
                                    cantidad_nueva = cantidad_actual + int(cantidad_producto_movimiento)
                                    producto.set_cantidad(cantidad_nueva)
                                    existe = True
                                    break

                            if existe == False:
                                print("\n> El producto", nombre_producto_movimiento, "no existe en la ubicación", ubicacion_movimiento, "por lo que no se puede agregar stock... Se omitirá el movimiento...")


                        elif instruccion == "vender_producto":

                            for producto in self.lista_productos:

                                if producto.get_nombre() == nombre_producto_movimiento and producto.get_ubicacion() == ubicacion_movimiento:
                                    
                                    cantidad_actual = int(producto.get_cantidad())

                                    if cantidad_actual < int(cantidad_producto_movimiento):
                                        print("\n> No se puede vender el producto", nombre_producto_movimiento, "ya que no hay suficiente stock en la ubicación", ubicacion_movimiento, "... Se omitirá el movimiento...")
                                        existe = True
                                        break
                                    
                                    else:
                                        cantidad_nueva = cantidad_actual - int(cantidad_producto_movimiento)
                                        producto.set_cantidad(cantidad_nueva)
                                        existe = True
                                        break

                            if existe == False:
                                print("\n> El producto", nombre_producto_movimiento, "no existe en la ubicación", ubicacion_movimiento, "por lo que no se puede vender... Se omitirá el movimiento...")


                        else: 
                            print("\nLa instrucción", instruccion, "no es válida, por lo que se omitirá...")


                    print("\nSe han cargado los movimientos correctamente...\n")

            else:
                print("\nEl archivo seleccionado no es válido...")
                print("Volviendo al menú inicial...\n")
                self.menu()
                return

        self.menu()
        return

    def crear_informe(self):
        titulo = "INFORME DE INVENTARIO\nProducto\tCantidad\tPrecio unitario\tValor Total\tUbicacion\n"
        with open("informe.txt", "w") as archivo:
            archivo.write(titulo)
            for producto in self.lista_productos:
                nombre = producto.get_nombre()
                cantidad = producto.get_cantidad()
                precio_unitario = producto.get_precio_unitario()
                valor_total = round((int(cantidad) * float(precio_unitario)), 2)
                ubicacion = producto.get_ubicacion()
                
                cadena = "{: <15}\t{: <10}\t{: <15}\t{: <12}\t{: <10}\n".format(
                    nombre, cantidad, ("Q"+str(precio_unitario)), ("Q"+str(valor_total)), ubicacion
                )
                
                archivo.write(cadena)

        print("\n> El informe se guardó en la carpeta raíz del proyecto con el nombre de informe.txt\n")
        self.menu()
        return


if __name__ == '__main__':
    metodos = Metodos()
    print("###########################")
    print("#  Sistema de inventario  #")
    print("###########################")
    metodos.menu()