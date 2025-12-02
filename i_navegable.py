"""
Interfaz INavegable
Define los métodos para embarcaciones que pueden navegar
"""

from abc import ABC, abstractmethod


class INavegable(ABC):
    """Interfaz para embarcaciones que pueden navegar"""
    
    @abstractmethod
    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):
        """Inicia la navegación de la embarcación"""
        pass
    
    @abstractmethod
    def parar_navegacion(self, tiempo_navegando):
        """Detiene la navegación de la embarcación"""
        pass