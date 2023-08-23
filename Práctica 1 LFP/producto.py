class Producto:

    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.ubicacion = ubicacion

    def get_nombre(self):
        return self.nombre
    
    def get_cantidad(self):
        return self.cantidad
    
    def get_precio_unitario(self):
        return self.precio_unitario
    
    def get_ubicacion(self):
        return self.ubicacion
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio_unitario(self, precio_unitario):
        self.precio_unitario = precio_unitario
    
    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion