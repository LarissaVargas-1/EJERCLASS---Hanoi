import time

class SimuladorHanoi:
    def __init__(self):
        """Método constructor: Inicializa los atributos de la clase."""
        self.tiempo_total = 0.0

    def resolver_recursivo(self, n, origen, destino, auxiliar):
        """Método recursivo que procesa los movimientos en memoria."""
        if n == 1:
            return
        
        # 1. Mover n-1 discos al auxiliar
        self.resolver_recursivo(n - 1, origen, auxiliar, destino)
        
        # 2. Mover el disco grande (operación en memoria)
        pass 
        
        # 3. Mover n-1 discos al destino
        self.resolver_recursivo(n - 1, auxiliar, destino, origen)

    def ejecutar_simulacion(self, discos):
        """Método de control: Gestiona el cronómetro y la llamada al motor recursivo."""
        movimientos_totales = (2 ** discos) - 1
        print(f"\nMovimientos a procesar: {movimientos_totales:,}")
        print("Procesando en memoria, por favor espera...")
        
        # Medición de tiempo
        tiempo_inicio = time.time()
        self.resolver_recursivo(discos, 'A', 'C', 'B')
        tiempo_fin = time.time()
        
        self.tiempo_total = tiempo_fin - tiempo_inicio
        
        print(f"¡Completado con éxito!")
        print(f"⏱️ Tiempo total de procesamiento: {self.tiempo_total:.4f} segundos")
        print("-" * 50)

    def menu_interactivo(self):
        """Método de interfaz: Maneja la interacción con el usuario en terminal."""
        print("--- SIMULADOR POO - TORRE DE HANOI ---")
        
        while True:
            try:
                discos = int(input("\nIntroduce el número de discos (o 0 para salir): "))
                
                if discos == 0:
                    print("¡Gracias por usar el simulador orientado a objetos!")
                    break
                elif discos < 0:
                    print("Por favor, introduce un número entero positivo.")
                    continue
                
                # Llamamos al método que controla la simulación
                self.ejecutar_simulacion(discos)
                
            except ValueError:
                print("Entrada inválida. Debes ingresar un número entero.")

# Instanciación de la clase y ejecución del programa
if __name__ == "__main__":
    # Creamos el objeto 'simulador' a partir de nuestra clase
    simulador = SimuladorHanoi()
    # Ejecutamos el método principal para iniciar el juego
    simulador.menu_interactivo()
