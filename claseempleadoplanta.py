from claseempleado import Empleado


class EmpleadoPlanta(Empleado):
    def __init__(self, dni, nombre, direccion, telefono, sueldo_basico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.sueldo_basico = sueldo_basico
        self.antiguedad = antiguedad

    def calcular_sueldo(self):
        return self.sueldo_basico + (self.sueldo_basico * 0.01 * self.antiguedad)
