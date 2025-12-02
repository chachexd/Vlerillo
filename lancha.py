"""
Clase Lancha
Embarcación motorizada con consumo de combustible
"""

from embarcacion import Embarcacion


class Lancha(Embarcacion):
    """Clase para lanchas motoras"""
    
    # Constantes públicas
    MIN_MOTORES = 1
    MAX_MOTORES = 2
    MIN_COMBUSTIBLE = 8
    MAX_COMBUSTIBLE = 50
    FACTOR_COMBUSTIBLE = 0.026
    MIN_VELOCIDAD_LANCHA = 1
    MAX_VELOCIDAD_LANCHA = 50
    
    # Atributos de clase
    _num_lanchas = 0
    
    def __init__(self, nombre=None, num_max_tripulantes=None, num_motores=None, nivel_combustible=None):
        """Constructor de Lancha"""
        
        # Constructor sin parámetros
        if nombre is None:
            Lancha._num_lanchas += 1
            nombre = f"Lancha {Lancha._num_lanchas}"
            num_max_tripulantes = Embarcacion.MIN_TRIPULANTES
            num_motores = Lancha.MIN_MOTORES
            nivel_combustible = Lancha.MAX_COMBUSTIBLE
        else:
            # Validaciones para constructor con parámetros
            if num_motores < Lancha.MIN_MOTORES or num_motores > Lancha.MAX_MOTORES:
                raise ValueError(f"El número de motores debe estar entre {Lancha.MIN_MOTORES} y {Lancha.MAX_MOTORES}.")
            
            if nivel_combustible < Lancha.MIN_COMBUSTIBLE or nivel_combustible > Lancha.MAX_COMBUSTIBLE:
                raise ValueError(
                    f"El nivel de combustible debe estar entre {Lancha.MIN_COMBUSTIBLE} y {Lancha.MAX_COMBUSTIBLE}."
                )
            
            Lancha._num_lanchas += 1
        
        # Llamar al constructor de la clase base
        super().__init__(nombre, num_max_tripulantes)
        
        # Atributos constantes propios de Lancha
        self._num_motores = num_motores
        self._cantidad_combustible = nivel_combustible
    
    # ========== MÉTODOS GETTERS ==========
    
    def get_num_motores(self):
        return self._num_motores
    
    def get_cantidad_combustible(self):
        return self._cantidad_combustible
    
    @classmethod
    def get_num_lanchas(cls):
        return cls._num_lanchas
    
    # ========== SOBREESCRITURA DE MÉTODOS ==========
    
    def set_rumbo(self, rumbo):
        """Cambia el rumbo de la lancha mientras navega"""
        
        # Validaciones específicas de Lancha
        if rumbo is None:
            raise ValueError("El rumbo no puede ser nulo, debes indicar el rumbo (norte, sur, este u oeste) para poder modificarlo.")
        
        if rumbo not in ["norte", "sur", "este", "oeste"]:
            raise ValueError("El rumbo no es correcto, debes indicar el rumbo (norte, sur, este u oeste) para poder modificarlo.")
        
        # Llamar al método de la clase base
        super().set_rumbo(rumbo)
    
    def iniciar_navegacion(self, velocidad, rumbo, patron, num_tripulantes):
        """Inicia la navegación de la lancha"""
        
        # Validaciones específicas de Lancha
        if self._cantidad_combustible < Lancha.MIN_COMBUSTIBLE or self._cantidad_combustible > Lancha.MAX_COMBUSTIBLE:
            raise Exception(
                f"La lancha {self._nombre} no tiene un nivel de combustible válido para iniciar la navegación. "
                f"El nivel de combustible debe estar entre {Lancha.MIN_COMBUSTIBLE} y {Lancha.MAX_COMBUSTIBLE}."
            )
        
        if velocidad < Lancha.MIN_VELOCIDAD_LANCHA or velocidad > Lancha.MAX_VELOCIDAD_LANCHA:
            raise ValueError(
                f"La velocidad de navegación de {velocidad} nudos asignada a {self._nombre} es incorrecta."
            )
        
        # Llamar al método de la clase base
        super().iniciar_navegacion(velocidad, rumbo, patron, num_tripulantes)
    
    def parar_navegacion(self, tiempo_navegando):
        """Detiene la navegación de la lancha"""
        
        # Calcular combustible consumido
        combustible_consumido = int(self._velocidad * tiempo_navegando * Lancha.FACTOR_COMBUSTIBLE)
        
        # Actualizar combustible (no puede ser menor que 0)
        self._cantidad_combustible = max(0, self._cantidad_combustible - combustible_consumido)
        
        # Llamar al método de la clase base
        super().parar_navegacion(tiempo_navegando)
    
    def señalizar(self):
        """Señalización de la lancha"""
        print(f"AVISO de señalización de la lancha {self._nombre} con bocinas y luces intermitentes.")
    
    def __str__(self):
        """Representación en cadena de la lancha"""
        resultado = super().__str__()
        resultado += f", Número de motores: {self._num_motores}, "
        resultado += f"Nivel de combustible: {self._cantidad_combustible}"
        return resultado