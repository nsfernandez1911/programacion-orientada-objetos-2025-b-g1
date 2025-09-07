class User:
    
    def __init__(self, nombre, document_id):
        self.nombre = nombre
        self._document_id = document_id 
    
    @property
    def document_id(self):
        return self._document_id