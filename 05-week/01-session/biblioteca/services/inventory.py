from typing import List, Optional
from domain.items import Item, Book, Magazine
from domain.user import User

class InventoryService:
    
    def __init__(self):
        self._items: List[Item] = []
        self._users: List[User] = []
    
    def create_book(self, titulo: str, stock: int = 1) -> Book:
        book = Book(titulo, stock)
        self._items.append(book)
        return book
    
    def create_magazine(self, titulo: str, stock: int = 1) -> Magazine:
        magazine = Magazine(titulo, stock)
        self._items.append(magazine)
        return magazine
    
    def create_user(self, nombre: str, document_id: str) -> User:
        
        for user in self._users:
            if user.document_id == document_id:
                raise ValueError(f"Usuario con documento {document_id} ya existe")
        
        user = User(nombre, document_id)
        self._users.append(user)
        return user
    
    def list_items(self) -> List[Item]:
        return self._items.copy()
    
    def list_users(self) -> List[User]:
        return self._users.copy()
    
    def find_item_by_title(self, titulo: str) -> Optional[Item]:
        for item in self._items:
            if item.titulo.lower() == titulo.lower():
                return item
        return None
    
    def find_user_by_document(self, document_id: str) -> Optional[User]:
        for user in self._users:
            if user.document_id == document_id:
                return user
        return None