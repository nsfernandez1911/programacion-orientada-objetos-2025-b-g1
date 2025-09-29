from __future__ import annotations
from models.persona import Persona


class Estudiante(Persona):
    """
    Clase que representa a un estudiante, hereda de Persona.
    Atributos adicionales: carrera, semestre y promedio.
    """

    def __init__(self, nombre: str, edad: int, identificacion: str, correo_electronico: str, 
                 carrera: str, semestre: int, promedio: float) -> None:
        super().__init__(nombre, edad, identificacion, correo_electronico)
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio

    def estudiar(self) -> str:
        """
        Indica que el estudiante está estudiando su carrera.
        """
        return f"{self.nombre} está estudiando {self.carrera} en el semestre {self.semestre}."

    def calcular_beca(self) -> str:
        """
        Retorna si tiene derecho a beca (cuando el promedio es igual o superior a 4.0).
        """
        if self.promedio >= 4.0:
            return f"{self.nombre} tiene derecho a beca con un promedio de {self.promedio}"
        else:
            return f"{self.nombre} no tiene derecho a beca con un promedio de {self.promedio}"

    def mostrar_informacion(self) -> str:
        """
        Sobrescribe el método de Persona para incluir carrera, semestre y promedio.
        """
        info_base = super().mostrar_informacion()
        return f"{info_base}\nCarrera: {self.carrera}\nSemestre: {self.semestre}\nPromedio: {self.promedio}"

    def presentarse(self) -> str:
        """
        Sobrescribe el método de Persona para incluir la carrera.
        """
        return f"Soy {self.nombre}, estudiante de {self.carrera} en semestre {self.semestre}, y tengo {self.edad} años."

    def __repr__(self) -> str:
        return (
            f"Estudiante(nombre='{self.nombre}', edad={self.edad}, identificacion='{self.identificacion}', "
            f"correo='{self.correo_electronico}', carrera='{self.carrera}', semestre={self.semestre}, promedio={self.promedio})"
        )
