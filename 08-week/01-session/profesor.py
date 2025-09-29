from __future__ import annotations
from models.persona import Persona


class Profesor(Persona):
    """
    Clase que representa a un profesor, hereda de Persona.
    Atributos adicionales: asignatura, salario y años de experiencia.
    """

    def __init__(self, nombre: str, edad: int, identificacion: str, correo_electronico: str,
                 asignatura: str, salario: float, años_experiencia: int) -> None:
        super().__init__(nombre, edad, identificacion, correo_electronico)
        self.asignatura = asignatura
        self.salario = salario
        self.años_experiencia = años_experiencia

    def dictar_clase(self) -> str:
        """
        Indica que el profesor está dictando una asignatura.
        """
        return f"El profesor {self.nombre} está dictando la clase de {self.asignatura}."

    def calcular_prima(self) -> str:
        """
        Calcula un bono equivalente al 10% del salario por cada cinco años de experiencia.
        """
        años_bonificables = self.años_experiencia // 5
        prima = (self.salario * 0.10) * años_bonificables
        return f"El profesor {self.nombre} tiene {self.años_experiencia} años de experiencia. Prima calculada: ${prima:,.2f} (${self.salario * 0.10:,.2f} por cada 5 años)"

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el método de Persona para incluir asignatura, salario y experiencia.
        """
        info_base = super().mostrar_informacion()
        return f"{info_base}\nAsignatura: {self.asignatura}\nSalario: ${self.salario:,.2f}\nAños de experiencia: {self.años_experiencia}"

    def enseñar(self) -> str:
        """
        Simula que el profesor está enseñando su materia.
        """
        return f"El profesor {self.nombre} enseña {self.asignatura}."

    def presentarse(self) -> str:
        """
        Sobrescribe el método de Persona para incluir la asignatura.
        """
        return f"Soy el profesor {self.nombre}, tengo {self.edad} años y enseño {self.asignatura}."

    def __repr__(self) -> str:
        return (
            f"Profesor(nombre='{self.nombre}', edad={self.edad}, identificacion='{self.identificacion}', "
            f"correo='{self.correo_electronico}', asignatura='{self.asignatura}', salario={self.salario}, años_experiencia={self.años_experiencia})"
        )
