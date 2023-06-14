from claseempleado import Empleado

class EmpleadoContratado(Empleado):
    valor_hora = 100  # Valor por hora común para todos los empleados contratados

    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_finalizacion, horas_trabajadas):
        super().__init__(dni, nombre, direccion, telefono)
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.horas_trabajadas = horas_trabajadas

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.valor_hora
