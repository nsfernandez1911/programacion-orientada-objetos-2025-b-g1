from datetime import datetime, timedelta
from services.inventory import InventoryService
from services.loans import LoansService
from services.reports import ReportsService
from domain.items import Book, Magazine

class BibliotecaDigitalApp:
    
    def __init__(self):
        self.inventory = InventoryService()
        self.loans = LoansService()
        self.reports = ReportsService(self.loans)
        self._load_sample_data()
    
    def _load_sample_data(self):
        
        self.inventory.create_book("El Quijote", 2)
        self.inventory.create_book("Cien Años de Soledad", 1)
        self.inventory.create_magazine("National Geographic", 3)
        self.inventory.create_magazine("Semana", 1)
        
    

        self.inventory.create_user("Juan Pérez", "12345678")
        self.inventory.create_user("María García", "87654321")
    
    def run(self):
        while True:  
            print("\n" + "="*50)
            print("    BIBLIOTECA DIGITAL - POO EN PYTHON")
            print("="*50)
            print("1. Listar materiales")
            print("2. Listar usuarios") 
            print("3. Crear usuario")
            print("4. Realizar préstamo")
            print("5. Realizar devolución")
            print("6. Reporte préstamos activos")
            print("7. Reporte préstamos vencidos")
            print("8. [DEMO] Simular préstamo vencido")
            print("9. Salir")
            print("-"*50)
            
            try:
                opcion = input("Seleccione opción: ").strip()
                
                if opcion == "1":
                    self._show_materials()
                elif opcion == "2":
                    self._show_users()
                elif opcion == "3":
                    self._create_user()
                elif opcion == "4":
                    self._create_loan()
                elif opcion == "5":
                    self._return_loan()
                elif opcion == "6":
                    self._show_active_loans()
                elif opcion == "7":
                    self._show_overdue_loans()
                elif opcion == "8":
                    self._simulate_overdue_loan()
                elif opcion == "9":
                    print("¡Gracias por usar la Biblioteca Digital!")
                    break
                else:
                    print("Opción inválida")
                    
            except Exception as e:
                print(f"Error: {e}")
    
    def _show_materials(self):
        print("\n=== MATERIALES DISPONIBLES ===")
        items = self.inventory.list_items()
        
        for item in items:
            tipo = "book" if isinstance(item, Book) else "magazine"
            print(f"• [{tipo}] {item.titulo} - Stock: {item.stock}")
    
    def _show_users(self):
        print("\n=== USUARIOS REGISTRADOS ===")
        users = self.inventory.list_users()
        
        for user in users:
            print(f"• {user.nombre} (Doc: {user.document_id})")
    
    def _create_user(self):
        print("\n=== CREAR USUARIO ===")
        nombre = input("Nombre: ").strip()
        document_id = input("Documento: ").strip()
        
        user = self.inventory.create_user(nombre, document_id)
        print(f"✓ Usuario creado: {user.nombre} (Doc: {user.document_id})")
    
    def _create_loan(self):
        print("\n=== REALIZAR PRÉSTAMO ===")
        
        
        users = self.inventory.list_users()
        items = [item for item in self.inventory.list_items() if item.stock > 0]
        
        if not users or not items:
            print("No hay usuarios registrados o materiales disponibles")
            return
        
        print("\nUsuarios:")
        for i, user in enumerate(users, 1):
            print(f"{i}. {user.nombre} (Doc: {user.document_id})")
        
        print("\nMateriales disponibles:")
        for i, item in enumerate(items, 1):
            tipo = "book" if isinstance(item, Book) else "magazine"
            print(f"{i}. [{tipo}] {item.titulo} (Stock: {item.stock})")
        
        try:
            
            user_idx = int(input("\nSeleccionar usuario (número): ")) - 1
            item_idx = int(input("Seleccionar material (número): ")) - 1
            
            if 0 <= user_idx < len(users) and 0 <= item_idx < len(items):
                user = users[user_idx]
                item = items[item_idx]
                
                loan = self.loans.create_loan(user, item)
                print(f"\n✓ Préstamo creado exitosamente!")
                print(f"  Usuario: {loan.user.nombre}")
                print(f"  Material: {loan.item.titulo}")
                print(f"  Fecha límite: {loan.due_date.strftime('%Y-%m-%d')}")
                print(f"  Días préstamo: {loan.item.loan_days()}")
            else:
                print("Selección inválida")
        except ValueError:
            print("Por favor ingrese números válidos")
    
    def _return_loan(self):
        print("\n=== REALIZAR DEVOLUCIÓN ===")
        
        active_loans = self.loans.get_active_loans()
        if not active_loans:
            print("No hay préstamos activos")
            return
        
        print("\nPréstamos activos:")
        for i, loan in enumerate(active_loans, 1):
            status = "VENCIDO" if loan.is_overdue else "AL DÍA"
            print(f"{i}. {loan.user.nombre} - {loan.item.titulo} [{status}]")
            if loan.is_overdue:
                print(f"   Días atraso: {loan.days_overdue}, Penalización: ${loan.calculate_penalty()}")
        
        try:
            loan_idx = int(input("\nSeleccionar préstamo (número): ")) - 1
            
            if 0 <= loan_idx < len(active_loans):
                loan = active_loans[loan_idx]
                returned_loan = self.loans.return_loan(loan.user, loan.item)
                
                print(f"\n✓ Devolución procesada!")
                print(f"  Usuario: {returned_loan.user.nombre}")
                print(f"  Material: {returned_loan.item.titulo}")
                
                penalty = returned_loan.calculate_penalty()
                if penalty > 0:
                    print(f"  Penalización aplicada: ${penalty}")
                else:
                    print("  Sin penalización (a tiempo)")
            else:
                print("Selección inválida")
        except ValueError:
            print("Por favor ingrese un número válido")
    
    def _show_active_loans(self):
        print("\n" + self.reports.active_loans_report())
    
    def _show_overdue_loans(self):
        print("\n" + self.reports.overdue_loans_report())
    
    def _simulate_overdue_loan(self): 
     
        print("\n=== SIMULACIÓN: PRÉSTAMO VENCIDO ===")
        print("(Esta opción es solo para demostrar penalizaciones)")
        
        active_loans = self.loans.get_active_loans()
        if not active_loans:
            print("No hay préstamos activos para simular vencimiento")
            return
        
        print("\nPréstamos activos:")
        for i, loan in enumerate(active_loans, 1):
            print(f"{i}. {loan.user.nombre} - {loan.item.titulo}")
        
        try:
            loan_idx = int(input("\nSeleccionar préstamo para simular vencimiento: ")) - 1
            dias_atraso = int(input("¿Cuántos días de atraso simular?: "))
            
            if 0 <= loan_idx < len(active_loans):
                loan = active_loans[loan_idx]
                
                
                loan.loan_date = datetime.now() - timedelta(days=loan.item.loan_days() + dias_atraso)
                loan.due_date = loan.loan_date + timedelta(days=loan.item.loan_days())
                
                print(f"\n✅ SIMULACIÓN APLICADA:")
                print(f"  Préstamo: {loan.item.titulo}")
                print(f"  Días de atraso: {loan.days_overdue}")
                print(f"  Penalización: ${loan.calculate_penalty()}")
                print(f"  Nueva fecha límite: {loan.due_date.strftime('%Y-%m-%d')}")
                print("\nAhora puedes ver este préstamo en 'Reportes vencidos' o devolverlo con penalización")
            else:
                print("Selección inválida")
                
        except ValueError:
            print("Por favor ingrese números válidos")


def main():
    app = BibliotecaDigitalApp()
    app.run()


if __name__ == "__main__":
    main()
