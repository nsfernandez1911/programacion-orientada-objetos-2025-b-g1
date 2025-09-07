from datetime import datetime, timedelta

class Loan:
    
    def __init__(self, user, item):
        self.user = user
        self.item = item
        self.loan_date = datetime.now()
      
        self.due_date = self.loan_date + timedelta(days=item.loan_days())
        self.return_date = None
    
    @property
    def is_active(self):
        
        return self.return_date is None
    
    @property
    def is_overdue(self):
        
        if not self.is_active:
            return False
        return datetime.now() > self.due_date
    
    @property
    def days_overdue(self):
        
        if not self.is_overdue:
            return 0
        return (datetime.now() - self.due_date).days
    
    def calculate_penalty(self):
       
        if self.return_date:
            
            if self.return_date > self.due_date:
                days_late = (self.return_date - self.due_date).days
                return max(0, days_late) * self.item.penalty_per_day()
        else:
            
            return max(0, self.days_overdue) * self.item.penalty_per_day()
        return 0
    
    def return_item(self):
       
        self.return_date = datetime.now()