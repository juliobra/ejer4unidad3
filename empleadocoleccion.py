import numpy as np

class EmpleadoCollection:
    def __init__(self, size):
        self.empleados = np.empty(size, dtype=object)
        self.count = 0

    def agregar_empleado(self, empleado):
        self.empleados[self.count] = empleado
        self.count += 1

    def obtener_empleados(self):
        return self.empleados[:self.count]
        
       def cargar_empleados_planta(empleado_collection, archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(',')
            dni = datos[0]
            nombre = datos[1]
            direccion = datos[2]
            telefono = datos[3]
            sueldo_basico = float(datos[4])
            antiguedad = int(datos[5])
            empleado_planta = EmpleadoPlanta(dni, nombre, direccion, telefono, sueldo_basico, antiguedad)
            empleado_collection.agregar_empleado(empleado_planta)

def cargar_empleados_contratados(empleado_collection, archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(',')
            dni = datos[0]
            nombre = datos[1]
            direccion = datos[2]
            telefono = datos[3]
            fecha_inicio = datos[4]
            fecha_finalizacion = datos[5]
            horas_trabajadas = int(datos[6])
            empleado_contratado = EmpleadoContratado(dni, nombre, direccion, telefono, fecha_inicio, fecha_finalizacion, horas_trabajadas)
            empleado_collection.agregar_empleado(empleado_contratado)

def cargar_empleados_externos(empleado_collection, archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split(',')
            dni = datos[0]
            nombre = datos[1]
            direccion = datos[2]
            telefono = datos[3]
            tarea = datos[4]
            fecha_inicio = datos[5]
            fecha_finalizacion = datos[6]
            monto_viatico = float(datos[7])
            costo_obra = float(datos[8])
            monto_seguro_vida = float(datos[9])
            empleado_externo = EmpleadoExterno(dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_finalizacion, monto_viatico, costo_obra, monto_seguro_vida)
            empleado_collection.agregar_empleado(empleado_externo)
