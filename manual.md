# Introducción a la programación y computación 2
## Práctica 1
### 4to Semestre
```js
Universidad San Carlos de Guatemala
Programador: Irving Fernando Alvarado Asensio
Carne: 202200349
Correo: 3291590461103@ingenieria.usac.edu.gt
```
---
## Descripción
Este proyecto implicó la creación de una aplicación de consola en Python para gestionar un inventario. A través de la implementación de funciones como carga de productos, movimientos de stock y generación de informes, el desarrollo del proyecto permitió ganar experiencia en el manejo de archivos y manipulación de datos. El enfoque en la interacción con archivos y la implementación de reglas de gestión de inventario brindó una oportunidad valiosa para comprender la aplicación práctica de la programación y la resolución de problemas.

## Objetivos
* Objetivo General
    *  Adquirir y aplicar habilidades fundamentales de programación y resolución de problemas a través del desarrollo de una aplicación de consola en Python
* Objetivos Específicos
    * Aprender a interactuar con archivos en Python, desde la lectura hasta la escritura, y entender cómo se pueden utilizar para almacenar y procesar datos de manera eficiente.
    * Adquirir habilidades en el procesamiento de cadenas de texto, dividiéndolas y extrayendo información relevante utilizando métodos y funciones específicas.
    * Comprender cómo utilizar estructuras de datos como listas para organizar y gestionar información, y cómo acceder y manipular elementos en ellas.
    * Practicar la aplicación de reglas lógicas en situaciones prácticas, como la actualización de cantidades en el inventario y la validación de disponibilidad al vender productos.

---
## Descripción del proyecto
El proyecto consiste en una aplicación de consola desarrollada en Python que ofrece la capacidad de gestionar un inventario de productos. La aplicación presenta un menú con cuatro opciones principales, que permiten cargar información desde archivos, realizar movimientos de stock, generar informes y cerrar el programa. A través de la carga de archivos con extensiones ".inv" y ".mov", se pueden crear productos nuevos en lotes y registrar movimientos de agregar stock y vender productos. La aplicación también verifica reglas como la actualización de cantidades y la validación de disponibilidad al vender productos. Adicionalmente, se ofrece la funcionalidad de generar un informe en formato de archivo de texto que muestra los detalles de los productos existentes en el inventario en ese momento. La cuarta opción del menú permite salir y cerrar el programa.

#### Menú

El menú se muestra utilizando el siguiente código
![Imagen1](https://i.ibb.co/93mkk9c/Foto-codigo-men.png")
Dentro de la función "menu" se llama a la función "seleccionar_opcion(argumento)" que recibe como argumento el número ingresado por el usuario. El código de esa función se muestra a continuación
![Imagen2](https://i.ibb.co/qgbZK4k/Seleccionar.png)
Con ayuda de algunos if aninados se guía al usuario a la opción a la que desea ingresar.

#### Carga de inventario

La aplicación permite la carga de productos en el inventario a través de la lectura de un archivo con extensión ".inv". Cada línea del archivo contiene información para crear productos nuevos en lote, incluyendo el nombre del producto, la cantidad disponible, el precio unitario y la ubicación en el inventario. De esto se encarga la función cargar_inventario(self)

La instruccion se debe encontrar en la forma:

```sh
crear_producto <nombre>;<cantidad>;<precio_unitario>;<ubicacion>
```

El código utilizado dentro de esta función es el siguiente:

![Imagen 3](https://i.ibb.co/4gcdHmJ/cargar-inventario.png)

Al inicio de la función, con ayuda de la librería Tkinter se abre una ventana del explorador de archivos de windows, esta le permite al usuario seleccionar un archivo con la extensión ".inv" en el momento que el usuario presiona aceptar, se almacena la dirección del archivo que el usuario desea importar. Si el usuario no seleccionó ningun archivo el programa lo devolverá al menú. Luego de seleccionar el archivo correctamente, se verifica una segunda vez que el archivo seleccionado tenga la extensión correcta, de ser así se procede a leer el archivo linea a linea. De cada linea se extrae la información de cada instrucción para realizar lo que estas indican, esto ultimo se realiza con el siguiente fragmento de código

![Imagen 4](https://i.ibb.co/xj7yc7q/Abriendo-archivo.png")

Una vez obtenido el contenido de la linea de instrucción se procede a crear el nuevo producto, con la instruccion que se muestra a continuacion

![Imagen 5](https://i.ibb.co/nBkY8kM/a-adir-producto.png)

Para ello se utiliza una clase llamada "Producto" cuyo contenido es el siguiente

```sh
class Producto:

    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.ubicacion = ubicacion
```

Todo el código mostrado anteriormente se ejecuta una vez por cada linea que contenga el archivo ".inv" y por cada iteración se verifica que el producto nuevo que se está creando no exista ya en la lista de productos, con el siguiente código

```sh
for producto in self.lista_productos:
    if producto.get_nombre() == nombre_producto and producto.get_ubicacion() == ubicacion:
        print("\nEl producto", nombre_producto, "ya existe en la ubicación", ubicacion, "por lo que no se sobreescibirá y se omitirá...")
        existe = True
        break
```

Al finalizar de crear todos los productos se muestra el menú nuevamente

#### Carga de movimientos

La aplicación permite la carga de instrucciones para actualizar el stock de los productos creados con anterioridad a través de la lectura de un archivo con extensión ".mov". Cada línea del archivo contiene información para añadir o descontar productos del inventario o dicho de otra forma, vender o comprar productos. De esto se encarga la función cargar_movimentos(self)

La instruccion para agregar stock se debe encontrar en la forma:

```sh
agregar_stock <nombre>;<cantidad>;<ubicacion>
```

Y la función para descontar stock debe encontrarse de la forma:

```sh
vender_producto <nombre>;<cantidad>;<ubicacion>

```

El código utilizado dentro de esta función es el siguiente:

![Imagen 3](https://i.ibb.co/61zHmsY/A-adir-movimiento.png")

Al inicio de la función, con ayuda de la librería Tkinter se abre una ventana del explorador de archivos de windows, esta le permite al usuario seleccionar un archivo con la extensión ".mov" en el momento que el usuario presiona aceptar, se almacena la dirección del archivo que el usuario desea importar. Si el usuario no seleccionó ningun archivo el programa lo devolverá al menú. Luego de seleccionar el archivo correctamente, se verifica una segunda vez que el archivo seleccionado tenga la extensión correcta, de ser así se procede a leer el archivo linea a linea. De cada linea se extrae la información de cada instrucción para realizar lo que estas indican, esto ultimo se realiza con el siguiente fragmento de código

![Imagen 4](https://i.ibb.co/QdVLnTR/info-movimi.png)

Una vez obtenido el contenido de la linea de instrucción se procede a seguir la instrucción, esto con ayuda del siguiente código

```sh
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
```

Todo el código mostrado anteriormente se ejecuta una vez por cada linea que contenga el archivo ".mov" por cada iteración va siguiendo la instrucción de la linea al momento de leerla. Al momento de agregar productos se verifica que el producto exista en la ubicación especificada en la instrucción, para ello se utiliza la variable booleana "existe" que se marca como true uicamente si encuentra el nombre del producto en la ubicación indicada.

Al momento de veder productos se verifica que el producto exista en la ubicación indicada y tambien que la cantidad a descontar no sea mayor que la cantidad que se encuentre en ese momento en existencia, esto para evitar cantidades negativas. 

Al finalizar de leer el archivo la aplicación muestra el menú nuevamente.

#### Generación de reporte

La función crear_informe(self) tiene como objetivo generar un informe detallado de los productos existentes en el inventario y guardar esta información en un archivo de texto llamado "informe.txt". Esta función recopila los datos relevantes de cada producto, como su nombre, cantidad, precio unitario, valor total y ubicación, y los formatea en una tabla legible.

La función comienza con la creación de un encabezado que establece el formato del informe, incluyendo los títulos de las columnas. A continuación, recorre la lista de productos en el inventario y extrae los atributos necesarios de cada producto utilizando métodos como
```sh
get_nombre(), get_cantidad(), get_precio_unitario() y get_ubicacion().
```

Se realiza el cálculo del valor total multiplicando la cantidad por el precio unitario, redondeándolo a dos decimales. Luego, se formatean los datos de cada producto en una cadena tabular que cumple con el formato del encabezado.

La cadena formateada se escribe en el archivo de informe junto con el encabezado, creando así una tabla que muestra claramente los detalles de cada producto.

Una vez que se completa la generación del informe y se guarda en el archivo "informe.txt", se muestra un mensaje en la consola indicando la ubicación del archivo y se regresa al menú principal de la aplicación.

El codigo utilizado para esta función se muestra a continuación:

![ImagenRep](https://i.ibb.co/82cxQbb/crear-reporte.png)

#### Salir
Por útlimo, la opción salir del menú. Detiene el programa por completo y limpia la memoria, para esta función únicamente se utiliza la línea 

```sh
exit()
```

![Messi](https://i.ibb.co/z6Nb8rg/messi.jpg")