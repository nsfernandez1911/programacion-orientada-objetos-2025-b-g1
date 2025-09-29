from models.estudiante import Estudiante
from models.profesor import Profesor
from models.persona import Persona

def main() -> None:
    print("=" * 60)
    print("TALLER: HERENCIA EN PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("=" * 60)
    
    # 1. Crear objetos de las clases Persona, Estudiante y Profesor
    print("\n1. CREACIÓN DE OBJETOS")
    print("-" * 30)
    
    # Crear una persona básica
    persona = Persona(
        nombre="María González", 
        edad=25, 
        identificacion="12345678", 
        correo_electronico="maria.gonzalez@email.com"
    )
    
    # Crear un estudiante
    estudiante = Estudiante(
        nombre="Ana García", 
        edad=20, 
        identificacion="87654321", 
        correo_electronico="ana.garcia@estudiante.edu",
        carrera="Ingeniería de Sistemas", 
        semestre=6, 
        promedio=4.2
    )
    
    # Crear un profesor
    profesor = Profesor(
        nombre="Carlos Rodríguez", 
        edad=45, 
        identificacion="11223344", 
        correo_electronico="carlos.rodriguez@profesor.edu",
        asignatura="Programación Orientada a Objetos", 
        salario=5000000, 
        años_experiencia=12
    )
    
    print("✓ Objetos creados exitosamente:")
    print(f"  - Persona: {persona.nombre}")
    print(f"  - Estudiante: {estudiante.nombre}")
    print(f"  - Profesor: {profesor.nombre}")
    
    # 2. Ejecutar métodos definidos en cada clase
    print("\n2. EJECUCIÓN DE MÉTODOS DE CADA CLASE")
    print("-" * 40)
    
    # Métodos de Persona
    print("\n📋 MÉTODOS DE LA CLASE PERSONA:")
    print(f"Saludar: {persona.saludar()}")
    print(f"¿Es mayor de edad? {persona.es_mayor_edad()}")
    print(f"Información:\n{persona.mostrar_informacion()}")
    
    # Métodos de Estudiante
    print("\n🎓 MÉTODOS DE LA CLASE ESTUDIANTE:")
    print(f"Estudiar: {estudiante.estudiar()}")
    print(f"Cálculo de beca: {estudiante.calcular_beca()}")
    print(f"Información:\n{estudiante.mostrar_informacion()}")
    
    # Métodos de Profesor
    print("\n👨‍🏫 MÉTODOS DE LA CLASE PROFESOR:")
    print(f"Dictar clase: {profesor.dictar_clase()}")
    print(f"Cálculo de prima: {profesor.calcular_prima()}")
    print(f"Información:\n{profesor.mostrar_informacion()}")
    
    # 3. Evidenciar correcta aplicación de herencia
    print("\n3. EVIDENCIA DE HERENCIA")
    print("-" * 25)
    
    # Demostración de polimorfismo
    personas = [persona, estudiante, profesor]
    
    print("🔄 Demostración de polimorfismo (método presentarse):")
    for i, persona_obj in enumerate(personas, 1):
        print(f"  {i}. {persona_obj.presentarse()}")
    
    # 4. Evidenciar sobrescritura de métodos
    print("\n4. SOBRESCRITURA DE MÉTODOS")
    print("-" * 30)
    
    print("📝 Comparación del método mostrar_informacion():")
    print("\n🔹 Persona (método base):")
    print(persona.mostrar_informacion())
    
    print("\n🔹 Estudiante (método sobrescrito):")
    print(estudiante.mostrar_informacion())
    
    print("\n🔹 Profesor (método sobrescrito):")
    print(profesor.mostrar_informacion())
    
    # 5. Cálculos de beca y prima
    print("\n5. CÁLCULOS DE BECA Y PRIMA")
    print("-" * 30)
    
    print("💰 Cálculo de beca para estudiantes:")
    print(f"  {estudiante.calcular_beca()}")
    
    print("\n💵 Cálculo de prima para profesores:")
    print(f"  {profesor.calcular_prima()}")
    
    # 6. Actualización del correo electrónico
    print("\n6. ACTUALIZACIÓN DEL CORREO ELECTRÓNICO")
    print("-" * 40)
    
    print("📧 Actualizando correo de la persona:")
    print(f"  {persona.actualizar_correo('maria.gonzalez.nueva@email.com')}")
    print(f"  Nuevo correo: {persona.correo_electronico}")
    
    print("\n📧 Actualizando correo del estudiante:")
    print(f"  {estudiante.actualizar_correo('ana.garcia.nueva@estudiante.edu')}")
    print(f"  Nuevo correo: {estudiante.correo_electronico}")
    
    print("\n📧 Actualizando correo del profesor:")
    print(f"  {profesor.actualizar_correo('carlos.rodriguez.nuevo@profesor.edu')}")
    print(f"  Nuevo correo: {profesor.correo_electronico}")
    
    # 7. Resumen final
    print("\n7. RESUMEN FINAL")
    print("-" * 15)
    print("✅ Herencia implementada correctamente")
    print("✅ Sobrescritura de métodos funcionando")
    print("✅ Cálculos de beca y prima implementados")
    print("✅ Actualización de correo electrónico funcionando")
    print("✅ Polimorfismo demostrado")
    
    print("\n" + "=" * 60)
    print("TALLER COMPLETADO EXITOSAMENTE")
    print("=" * 60)

if __name__ == "__main__":
    main()
