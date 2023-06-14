def test(self):
  
empleados = EmpleadoCollection(100)  # Tamaño de la colección
cargar_empleados_planta(empleados, "planta.csv")
cargar_empleados_contratados(empleados, "contratados.csv")
cargar_empleados_externos(empleados, "externos.csv") 

def registrar_horas_trabajadas(empleados, dni, horas):
    for empleado in empleados.obtener_empleados():
        if empleado.dni == dni:
            if isinstance(empleado, EmpleadoContratado):
                empleado.horas_trabajadas += horas
                break

def total_tarea(empleados, tarea):
    total_monto = 0
    for empleado in empleados.obtener_empleados():
        if isinstance(empleado, EmpleadoExterno) and empleado.tarea == tarea:
            total_monto += empleado.calcular_sueldo()
    return total_monto

def ayuda_economica(empleados):
    empleados_ayuda = []
    for empleado in empleados.obtener_empleados():
        if empleado.calcular_sueldo() < 150000:
            empleados_ayuda.append(empleado)
    return empleados_ayuda

def calcular_sueldos(empleados):
    for empleado in empleados.obtener_empleados():
        sueldo = empleado.calcular_sueldo()
        print("Nombre:", empleado.nombre)
        print("Teléfono:", empleado.telefono)
        print("Sueldo a cobrar:", sueldo)
        print()

# Ejemplos de uso
registrar_horas_trabajadas(empleados, "12345678", 8)
monto_total_tarea = total_tarea(empleados, "carpintería")
empleados_ayuda_economica = ayuda_economica(empleados)

calcular_sueldos(empleados)

if __name__== '__main__':
  test()





 
'''