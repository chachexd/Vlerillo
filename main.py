"""
Programa Principal - Sistema de Gestión de Embarcaciones
Tarea 4 - POO Python
"""

from embarcacion import Embarcacion
from lancha import Lancha
from velero import Velero


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