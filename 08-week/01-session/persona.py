from __future__ import annotations

class Persona:
    """
    Clase base que representa a una persona.
    Atributos: nombre, edad, identificación y correo electrónico.
    """

    def __init__(self, nombre: str, edad: int, identificacion: str, correo_electronico: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.identificacion = identificacion
        self.correo_electronico = correo_electronico

    def saludar(self) -> str:
        """
        Muestra un saludo personalizado con el nombre.
        """
        return f"¡Hola! Mi nombre es {self.nombre}."

    def es_mayor_edad(self) -> bool:
        """
        Indica si la persona es mayor de edad.
        """
        return self.edad >= 18

    def mostrar_informacion(self) -> str:
        """
        Imprime los datos generales de la persona.
        """
        return f"Nombre: {self.nombre}\nEdad: {self.edad} años\nIdentificación: {self.identificacion}\nCorreo: {self.correo_electronico}"

    def actualizar_correo(self, nuevo_correo: str) -> str:
        """
        Permite cambiar el correo de la persona.
        """
        correo_anterior = self.correo_electronico
        self.correo_electronico = nuevo_correo
        return f"Correo actualizado de '{correo_anterior}' a '{nuevo_correo}'"

    def presentarse(self) -> str:
        """
        Retorna una presentación básica de la persona.
        """
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def __str__(self) -> str:
        return f"{self.nombre} ({self.edad} años)"

    def __repr__(self) -> str:
        return f"Persona(nombre='{self.nombre}', edad={self.edad}, identificacion='{self.identificacion}', correo='{self.correo_electronico}')"
