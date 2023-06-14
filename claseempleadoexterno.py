from claseempleado import Empleado
class EmpleadoExterno(Empleado):
    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_finalizacion, monto_viatico, costo_obra, monto_seguro_vida):
        super().__init__(dni, nombre, direccion, telefono)
        self.tarea = tarea
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.monto_viatico = monto_viatico
        self.costo_obra = costo_obra
        self.monto_seguro_vida = monto_seguro_vida

    def calcular_sueldo(self):
        return self.costo_obra - self.monto_viatico - self.monto_seguro_vida
