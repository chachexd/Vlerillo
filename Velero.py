"""
Clase Velero
Embarcación a vela que puede participar en regatas
"""

from embarcacion import Embarcacion
from i_regateable import IRegateable
from excepciones import IllegalArgumentException


class Velero(Embarcacion, IRegateable):
    """Clase para veleros"""
    
    # Constantes públicas
    MIN_MASTILES = 1
    MAX_MASTILES = 4
    MIN_VELOCIDAD_VELERO = 2
    MAX_VELOCIDAD_VELERO = 30
    
    # Atributos de clase
    _num_veleros = 0
    
    def __init__(self, nombre=None, num_mastiles=None, num_max_tripulantes=None):
        """Constructor de Velero"""
        
        # Constructor sin parámetros
        if nombre is None:
            Velero._num_veleros += 1
            nombre = f"Velero {Velero._num_veleros}"
            num_mastiles = Velero.MIN_MASTILES
            num_max_tripulantes = Embarcacion.MIN_TRIPULANTES
        else:
            # Validación para constructor con parámetros
            if num_mastiles < Velero.MIN_MASTILES or num_mastiles > Velero.MAX_MASTILES:
                raise IllegalArgumentException(
                    f"El número de mástiles debe estar entre {Velero.MIN_MASTILES} y {Velero.MAX_MASTILES}."
                )
            
            Velero._num_veleros += 1
        
        # Llamar al constructor de la clase base
        super().__init__(nombre, num_max_tripulantes)
        
        # Atributo constante propio de Velero
        self._num_mastiles = num_mastiles
    
    # ========== MÉTODOS GETTERS ==========
    
    def get_num_mastiles(self):
        return self._num_mastiles
    
    @classmethod
    def get_num_veleros(cls):
        return cls._num_veleros
    
    # ========== SOBREESCRITURA DE MÉTODOS ==========
    
    def set_rumbo(self, rumbo):
        """Cambia el rumbo del velero mientras navega"""
        
        # Validaciones específicas de Velero
        if rumbo is None:
            raise ValueError("El rumbo no puede ser nulo, debes indicar el rumbo (ceñida o empopada) para poder modificarlo.")
        
        if rumbo not in ["ceñida", "empopada"]:
            raise ValueError("El rumbo no es correcto, debes indicar el rumbo (ceñida o empopada) para poder modificarlo.")
        
        # Llamar al método de la clase base
        super().set_rumbo(rumbo)
    
    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):
        """Inicia la navegación del velero"""
        
        # Validación específica de Velero
        if velocidad < Velero.MIN_VELOCIDAD_VELERO or velocidad > Velero.MAX_VELOCIDAD_VELERO:
            raise ValueError(f"La velocidad de navegación de {velocidad} nudos es incorrecta.")
        
        # Llamar al método de la clase base
        super().iniciar_navegacion(velocidad, rumbo, patron, num_tripulantes)
    
    def iniciar_regata(self, otro_barco):
        """Inicia una regata con otro velero"""
        
        # Validaciones
        if otro_barco is None:
            raise ValueError("El barco con el que se intenta regatear no existe")
        
        if not self._navegando:
            raise Exception(f"No se puede iniciar la regata, el barco {self._nombre} no está navegando.")
        
        if not otro_barco._navegando:
            raise Exception(f"No se puede iniciar la regata, el barco {otro_barco._nombre} no está navegando.")
        
        if self._rumbo != otro_barco._rumbo:
            raise Exception(
                f"No se puede iniciar la regata, los barcos {self._nombre} y {otro_barco._nombre} "
                "deben navegar con el mismo rumbo."
            )
        
        if self._num_mastiles != otro_barco._num_mastiles:
            raise Exception(
                f"No se puede iniciar la regata, los barcos {self._nombre} y {otro_barco._nombre} "
                "no tienen el mismo numero de mástiles."
            )
        
        # Determinar ganador
        if self._velocidad > otro_barco._velocidad:
            return f"El barco {self._nombre} ha llegado antes a la línea de llegada."
        elif self._velocidad < otro_barco._velocidad:
            return f"El barco {otro_barco._nombre} ha llegado antes a la línea de llegada."
        else:
            return f"Los barcos {self._nombre} y {otro_barco._nombre} han llegado a la vez a la línea de llegada."
    
    def señalizar(self):
        """Señalización del velero"""
        print(f"AVISO del velero {self._nombre} con banderas de señalización marítima.")
    
    def __str__(self):
        """Representación en cadena del velero"""
        resultado = super().__str__()
        resultado += f", Número de mástiles: {self._num_mastiles}"
        return resultado