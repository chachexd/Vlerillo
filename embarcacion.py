"""
Clase Embarcacion (abstracta)
Clase base para todas las embarcaciones del puerto deportivo
"""

from abc import ABC, abstractmethod
from i_navegable import INavegable


class Embarcacion(INavegable, ABC):
    """Clase abstracta base para todas las embarcaciones"""
    
    # Constantes públicas
    PATRON_POR_DEFECTO = "Sin patrón"
    RUMBO_POR_DEFECTO = "Sin rumbo"
    MIN_TRIPULANTES = 0
    
    # Atributos de clase (privados)
    _num_barcos = 0
    _num_barcos_navegando = 0
    _tiempo_total_navegacion_acumulado = 0.0
    
    def __init__(self, nombre, num_max_tripulantes):
        """Constructor de Embarcacion"""
        
        # Validaciones
        if nombre is None:
            raise ValueError("El nombre de la embarcación es obligatorio.")
        
        if nombre.strip() == "":
            raise ValueError("El nombre de la embarcación no puede estar vacío.")
        
        if num_max_tripulantes < Embarcacion.MIN_TRIPULANTES:
            raise ValueError(f"El número de tripulantes debe ser, como mínimo, {Embarcacion.MIN_TRIPULANTES}.")
        
        # Atributos constantes del objeto (privados)
        self._nombre = nombre
        self._num_max_tripulantes = num_max_tripulantes
        
        # Atributos de estado (protegidos para que las subclases puedan acceder)
        self._navegando = False
        self._velocidad = 0
        self._patron = Embarcacion.PATRON_POR_DEFECTO
        self._rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self._tripulacion = 0
        self._tiempo_total_navegacion = 0.0
        
        # Actualizar atributos de clase
        Embarcacion._num_barcos += 1
    
    # ========== MÉTODOS GETTERS ==========
    
    def get_nombre_barco(self):
        return self._nombre
    
    def get_num_max_tripulantes(self):
        return self._num_max_tripulantes
    
    def is_navegando(self):
        return self._navegando
    
    def get_velocidad(self):
        return self._velocidad
    
    def get_rumbo(self):
        return self._rumbo
    
    def get_patron(self):
        return self._patron
    
    def get_tripulacion(self):
        return self._tripulacion
    
    def get_tiempo_total_navegacion(self):
        return self._tiempo_total_navegacion
    
    # ========== MÉTODOS DE CLASE ==========
    
    @classmethod
    def get_num_barcos(cls):
        return cls._num_barcos
    
    @classmethod
    def get_num_barcos_navegando(cls):
        return cls._num_barcos_navegando
    
    @classmethod
    def get_tiempo_total_navegacion_acumulado(cls):
        return cls._tiempo_total_navegacion_acumulado
    
    # ========== MÉTODOS DE MODIFICACIÓN ==========
    
    def set_rumbo(self, rumbo):
        """Cambia el rumbo de la embarcación mientras navega"""
        
        if not self._navegando:
            raise Exception(f"La embarcación {self._nombre} no está navegando, no se puede cambiar el rumbo.")
        
        if rumbo == self._rumbo:
            raise Exception(
                f"La embarcación {self._nombre} ya está navegando con ese rumbo ({self._rumbo}), "
                "debes indicar un rumbo distinto para poder modificarlo."
            )
        
        # Si todo está bien, actualizar rumbo
        self._rumbo = rumbo
    
    # ========== MÉTODOS DE NAVEGACIÓN (de la interfaz INavegable) ==========
    
    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):
        """Inicia la navegación de la embarcación"""
        
        # Validaciones
        if self._navegando:
            raise Exception(f"La embarcación {self._nombre} ya está navegando y se encuentra fuera de puerto.")
        
        if rumbo is None or rumbo.strip() == "":
            raise ValueError("Debes indicar el rumbo para iniciar la navegación.")
        
        if patron is None or patron.strip() == "":
            raise ValueError("El patrón de la embarcación no puede estar vacío, se necesita un patrón para iniciar la navegación.")
        
        if num_tripulantes < Embarcacion.MIN_TRIPULANTES or num_tripulantes > self._num_max_tripulantes:
            raise ValueError(
                f"El número de tripulantes debe estar entre {Embarcacion.MIN_TRIPULANTES} y {self._num_max_tripulantes}."
            )
        
        # Actualizar atributos
        self._navegando = True
        self._velocidad = velocidad
        self._rumbo = rumbo
        self._patron = patron
        self._tripulacion = num_tripulantes
        
        # Actualizar contador de clase
        Embarcacion._num_barcos_navegando += 1
    
    def parar_navegacion(self, tiempo_navegando):
        """Detiene la navegación de la embarcación"""
        
        # Validaciones
        if not self._navegando:
            raise Exception(f"La embarcación {self._nombre} no está navegando.")
        
        if tiempo_navegando < 0:
            raise ValueError("Tiempo navegando incorrecto, debe ser mayor que cero.")
        
        # Actualizar tiempos
        self._tiempo_total_navegacion += tiempo_navegando
        Embarcacion._tiempo_total_navegacion_acumulado += tiempo_navegando
        
        # Resetear estado de navegación
        self._navegando = False
        self._velocidad = 0
        self._rumbo = Embarcacion.RUMBO_POR_DEFECTO
        self._patron = Embarcacion.PATRON_POR_DEFECTO
        self._tripulacion = 0
        
        # Actualizar contador de clase
        Embarcacion._num_barcos_navegando -= 1
    
    # ========== MÉTODO ABSTRACTO ==========
    
    @abstractmethod
    def señalizar(self):
        """Método abstracto para la señalización"""
        pass
    
    # ========== MÉTODO __str__ ==========
    
    def __str__(self):
        """Representación en cadena de la embarcación"""
        
        resultado = f"Nombre de la embarcación: {self._nombre}, "
        resultado += f"Tripulación: {self._tripulacion}, "
        
        if self._navegando:
            resultado += "Navegando: Sí, "
            resultado += f"con el patrón {self._patron} en {self._rumbo} a {self._velocidad} nudos, "
        else:
            resultado += "Navegando: No, "
        
        resultado += f"Tiempo total de navegación de la embarcación: {self._tiempo_total_navegacion:.2f} horas"
        
        return resultado