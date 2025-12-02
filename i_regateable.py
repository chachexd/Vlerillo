"""
Interfaz IRegateable
Define los métodos para embarcaciones que pueden participar en regatas
"""

from abc import ABC, abstractmethod


class IRegateable(ABC):
    """Interfaz para embarcaciones que pueden participar en regatas"""
    
    @abstractmethod
    def iniciar_regata(self, otro_barco):
        """Inicia una regata con otro barco"""
        pass