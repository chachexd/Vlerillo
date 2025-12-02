class Embarcacion:
    PATRON_POR_DEFECTO = "Sin patron"
    RUMBO_POR_DEFECTO = "Sin rumbo"
    MIN_TRIPULANTES = 0

    __barcos_creados = 0
    __barcos_navegando = 0
    __tiempo_total_navegacion = 0

    def __init__(self, nombre, max_tripulantes):
        if nombre is None:
            raise ValueError("El nombre de la embarcaci\u00f3n es obligatorio.")

        nombre_normalizado = nombre.strip() if isinstance(nombre, str) else ""
        if nombre_normalizado == "":
            raise ValueError("El nombre de la embarcaci\u00f3n no puede estar vac\u00edo.")

        if max_tripulantes < self.MIN_TRIPULANTES:
            raise ValueError(
                f"El n\u00famero de tripulantes debe ser, como m\u00ednimo, {self.MIN_TRIPULANTES}."
            )

        # Atributos constantes (solo la propia clase puede consultarlos)
        self.__nombre = nombre_normalizado
        self.__max_tripulantes = max_tripulantes

        # Estado del barco (accesible por clases hijas)
        self._navegando = False

        # Datos de navegacion (accesibles por clases hijas)
        self._velocidad = 0
        self._nombre_patron = self.PATRON_POR_DEFECTO
        self._rumbo = self.RUMBO_POR_DEFECTO
        self._tripulantes = self.MIN_TRIPULANTES
        self._tiempo_navegacion = 0

        Embarcacion.__barcos_creados += 1

    def _iniciar_navegacion(
        self,
        patron=None,
        rumbo=None,
        tripulantes=MIN_TRIPULANTES,
        velocidad=0,
    ):
        """Marca el inicio de navegacion y actualiza los contadores de clase."""
        if self._navegando:
            return

        if tripulantes > self.__max_tripulantes:
            raise ValueError("Se supera el numero maximo de tripulantes permitido.")

        self._navegando = True
        self._nombre_patron = patron if patron is not None else self.PATRON_POR_DEFECTO
        self._rumbo = rumbo if rumbo is not None else self.RUMBO_POR_DEFECTO
        self._tripulantes = max(tripulantes, self.MIN_TRIPULANTES)
        self._velocidad = velocidad

        Embarcacion.__barcos_navegando += 1

    def _detener_navegacion(self, tiempo_empleado=0):
        """Detiene la navegacion y acumula tiempo de viaje."""
        if self._navegando:
            Embarcacion.__barcos_navegando -= 1

        if tiempo_empleado > 0:
            self._tiempo_navegacion += tiempo_empleado
            Embarcacion.__tiempo_total_navegacion += tiempo_empleado

        self._navegando = False
        self._velocidad = 0
        self._rumbo = self.RUMBO_POR_DEFECTO
        self._tripulantes = self.MIN_TRIPULANTES
        self._nombre_patron = self.PATRON_POR_DEFECTO
