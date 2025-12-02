class Velero:
    """Descripción de la clase"""
    
    def __init__(self, atributo1, atributo2):
        """Constructor de la clase"""
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self._privado = None
    
    def __str__(self):
        return f"Velero(atributo1={self.atributo1}, atributo2={self.atributo2})"
    
    def __repr__(self):
        return f"Velero(atributo1={self.atributo1!r}, atributo2={self.atributo2!r})"
    
    def metodo(self, parametro):
        """Descripción del método"""
        pass
    
    @property
    def privado(self):
        return self._privado
    
    @privado.setter
    def privado(self, valor):
        self._privado = valor