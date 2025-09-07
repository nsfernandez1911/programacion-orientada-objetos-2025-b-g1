from typing import List, Optional
from domain.loan import Loan
from domain.user import User
from domain.items import Item

class LoansService:
    
    
    def __init__(self):
        self._loans: List[Loan] = []
    
    def create_loan(self, user: User, item: Item) -> Loan:
        
        
        if item.stock <= 0:
            raise ValueError(f"Sin stock disponible para {item.titulo}")
        
        
        for loan in self._loans:
            if (loan.is_active and 
                loan.user.document_id == user.document_id and 
                loan.item.titulo == item.titulo):
                raise ValueError("Usuario ya tiene préstamo activo de este material")
        
        
        loan = Loan(user, item)
        self._loans.append(loan)
        item.stock -= 1
        
        return loan
    
    def return_loan(self, user: User, item: Item) -> Loan:
        
        
        for loan in self._loans:
            if (loan.is_active and 
                loan.user.document_id == user.document_id and 
                loan.item.titulo == item.titulo):
                
                loan.return_item()
                item.stock += 1
                return loan
        
        raise ValueError("No se encontró préstamo activo")
    
    def get_active_loans(self) -> List[Loan]:
    
        return [loan for loan in self._loans if loan.is_active]
    
    def get_overdue_loans(self) -> List[Loan]:
       
        return [loan for loan in self._loans if loan.is_active and loan.is_overdue]