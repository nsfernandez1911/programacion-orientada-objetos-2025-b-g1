from services.loans import LoansService

class ReportsService:
    
    def __init__(self, loans_service: LoansService):
        self.loans_service = loans_service
    
    def active_loans_report(self) -> str:
        active_loans = self.loans_service.get_active_loans()
        
        if not active_loans:
            return "No hay préstamos activos"
        
        report = "=== PRÉSTAMOS ACTIVOS ===\n"
        for loan in active_loans:
            status = "VENCIDO" if loan.is_overdue else "AL DÍA"
            report += f"• {loan.user.nombre} - {loan.item.titulo} [{status}]\n"
            report += f"  Fecha límite: {loan.due_date.strftime('%Y-%m-%d')}\n"
            
            if loan.is_overdue:
                report += f"  Días atraso: {loan.days_overdue}\n"
                report += f"  Penalización estimada: ${loan.calculate_penalty()}\n"
            report += "\n"
        
        return report
    
    def overdue_loans_report(self) -> str:
        overdue_loans = self.loans_service.get_overdue_loans()
        
        if not overdue_loans:
            return "No hay préstamos vencidos"
        
        report = "=== PRÉSTAMOS VENCIDOS ===\n"
        total_penalty = 0
        
        for loan in overdue_loans:
            penalty = loan.calculate_penalty()
            total_penalty += penalty
            
            report += f"• {loan.user.nombre} - {loan.item.titulo}\n"
            report += f"  Días atraso: {loan.days_overdue}\n"
            report += f"  Penalización: ${penalty}\n\n"
        
        report += f"TOTAL PENALIZACIONES: ${total_penalty}"
        return report