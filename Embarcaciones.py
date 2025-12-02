"""
Sistema de gestión de embarcaciones para puerto deportivo
Tarea 4 - POO Python
"""

from abc import ABC, abstractmethod


# ==================== INTERFACES ====================

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


class IRegateable(ABC):
    """Interfaz para embarcaciones que pueden participar en regatas"""
    
    @abstractmethod
    def iniciar_regata(self, otro_barco):
        """Inicia una regata con otro barco"""
        pass


# ==================== CLASE BASE EMBARCACION ====================

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


# ==================== CLASE LANCHA ====================

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


# ==================== CLASE VELERO ====================

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


# ==================== EXCEPCIÓN PERSONALIZADA ====================

class IllegalArgumentException(Exception):
    """Excepción para argumentos ilegales"""
    pass


# ==================== PROGRAMA PRINCIPAL ====================

def main():
    """Programa principal para probar las clases"""
    
    print("=" * 80)
    print("PRUEBA DEL SISTEMA DE GESTIÓN DE EMBARCACIONES")
    print("=" * 80)
    
    # ========== PRUEBA 1: Constructores y atributos ==========
    print("\n--- PRUEBA 1: Constructores y atributos ---")
    
    try:
        # Crear veleros
        velero1 = Velero("Atlantis", 2, 5)
        print(f"✓ Velero creado: {velero1.get_nombre_barco()}")
        
        velero2 = Velero()  # Constructor sin parámetros
        print(f"✓ Velero creado: {velero2.get_nombre_barco()}")
        
        # Crear lanchas
        lancha1 = Lancha("Rapidisima", 2, 1, 30)
        print(f"✓ Lancha creada: {lancha1.get_nombre_barco()}")
        
        lancha2 = Lancha()  # Constructor sin parámetros
        print(f"✓ Lancha creada: {lancha2.get_nombre_barco()}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # ========== PRUEBA 2: Métodos getters y de clase ==========
    print("\n--- PRUEBA 2: Métodos getters y de clase ---")
    
    print(f"Número total de embarcaciones: {Embarcacion.get_num_barcos()}")
    print(f"Número de veleros: {Velero.get_num_veleros()}")
    print(f"Número de lanchas: {Lancha.get_num_lanchas()}")
    print(f"Velero1 - Mástiles: {velero1.get_num_mastiles()}, Tripulantes max: {velero1.get_num_max_tripulantes()}")
    print(f"Lancha1 - Motores: {lancha1.get_num_motores()}, Combustible: {lancha1.get_cantidad_combustible()}")
    
    # ========== PRUEBA 3: Iniciar y parar navegación ==========
    print("\n--- PRUEBA 3: Iniciar y parar navegación ---")
    
    try:
        # Iniciar navegación velero1
        velero1.iniciar_navegacion(10, "empopada", "Pepe Martinez", 1)
        print(f"✓ {velero1.get_nombre_barco()} ha iniciado navegación")
        print(f"  Navegando: {velero1.is_navegando()}, Velocidad: {velero1.get_velocidad()} nudos")
        
        # Iniciar navegación lancha1
        lancha1.iniciar_navegacion(25, "oeste", "Juan Lopez", 2)
        print(f"✓ {lancha1.get_nombre_barco()} ha iniciado navegación")
        print(f"  Navegando: {lancha1.is_navegando()}, Velocidad: {lancha1.get_velocidad()} nudos")
        
        print(f"\nEmbarcaciones navegando: {Embarcacion.get_num_barcos_navegando()}")
        
        # Parar navegación
        velero1.parar_navegacion(1.0)
        print(f"✓ {velero1.get_nombre_barco()} ha parado la navegación")
        
        lancha1.parar_navegacion(0.42)
        print(f"✓ {lancha1.get_nombre_barco()} ha parado la navegación")
        print(f"  Combustible restante: {lancha1.get_cantidad_combustible()}")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # ========== PRUEBA 4: Cambio de rumbo ==========
    print("\n--- PRUEBA 4: Cambio de rumbo ---")
    
    try:
        velero1.iniciar_navegacion(15, "ceñida", "Maria Garcia", 3)
        print(f"✓ {velero1.get_nombre_barco()} navegando en {velero1.get_rumbo()}")
        
        velero1.set_rumbo("empopada")
        print(f"✓ Rumbo cambiado a {velero1.get_rumbo()}")
        
        velero1.parar_navegacion(0.5)
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # ========== PRUEBA 5: Regatas ==========
    print("\n--- PRUEBA 5: Regatas ---")
    
    try:
        # Crear dos veleros para regata
        velero3 = Velero("Tormenta", 2, 4)
        velero4 = Velero("Rayo", 2, 4)
        
        # Iniciar navegación
        velero3.iniciar_navegacion(20, "empopada", "Carlos Ruiz", 2)
        velero4.iniciar_navegacion(18, "empopada", "Ana Lopez", 3)
        
        # Iniciar regata
        resultado = velero3.iniciar_regata(velero4)
        print(f"✓ Regata iniciada: {resultado}")
        
        velero3.parar_navegacion(0.8)
        velero4.parar_navegacion(0.8)
        
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # ========== PRUEBA 6: Señalización ==========
    print("\n--- PRUEBA 6: Señalización (polimorfismo) ---")
    
    embarcaciones = [velero1, lancha1, velero3]
    for embarcacion in embarcaciones:
        embarcacion.señalizar()
    
    # ========== PRUEBA 7: Método __str__ ==========
    print("\n--- PRUEBA 7: Representación de objetos (__str__) ---")
    
    velero1.iniciar_navegacion(10, "empopada", "Pepe Martinez", 1)
    lancha1.iniciar_navegacion(25, "oeste", "Juan Lopez", 2)
    
    print(f"\nVelero: {velero1}")
    print(f"\nLancha: {lancha1}")
    
    velero1.parar_navegacion(1.0)
    lancha1.parar_navegacion(0.42)
    
    # ========== PRUEBA 8: Excepciones ==========
    print("\n--- PRUEBA 8: Manejo de excepciones ---")
    
    try:
        # Intentar crear velero con mástiles inválidos
        velero_error = Velero("Error", 10, 3)
    except Exception as e:
        print(f"✓ Excepción capturada correctamente: {e}")
    
    try:
        # Intentar cambiar rumbo sin navegar
        velero2.set_rumbo("ceñida")
    except Exception as e:
        print(f"✓ Excepción capturada correctamente: {e}")
    
    try:
        # Intentar regata con barcos que no navegan igual
        velero5 = Velero("Viento", 3, 2)
        velero5.iniciar_navegacion(15, "ceñida", "Pedro", 1)
        velero6 = Velero("Mar", 2, 2)
        velero6.iniciar_navegacion(15, "ceñida", "Luis", 1)
        velero5.iniciar_regata(velero6)
    except Exception as e:
        print(f"✓ Excepción capturada correctamente: {e}")
    
    # ========== ESTADÍSTICAS FINALES ==========
    print("\n--- ESTADÍSTICAS FINALES ---")
    print(f"Total de embarcaciones creadas: {Embarcacion.get_num_barcos()}")
    print(f"Total de veleros: {Velero.get_num_veleros()}")
    print(f"Total de lanchas: {Lancha.get_num_lanchas()}")
    print(f"Tiempo total de navegación acumulado: {Embarcacion.get_tiempo_total_navegacion_acumulado():.2f} horas")
    
    print("\n" + "=" * 80)
    print("FIN DE LAS PRUEBAS")
    print("=" * 80)


if __name__ == "__main__":
    main()