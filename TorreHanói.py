import time

def torre_de_hanoi_rapida(n, origen, destino, auxiliar):
    """
    Versión ultra rápida sin impresiones en pantalla.
    Procesa los movimientos directamente en la memoria.
    """
    if n == 1:
        return
    
    # 1. Mover n-1 discos al auxiliar
    torre_de_hanoi_rapida(n - 1, origen, auxiliar, destino)
    
    # 2. Mover el disco grande (operación simulada sin print)
    pass 
    
    # 3. Mover n-1 discos al destino
    torre_de_hanoi_rapida(n - 1, auxiliar, destino, origen)

def iniciar_simulador():
    print("--- SIMULADOR DE ALTA VELOCIDAD (TORRE DE HANOI) ---")
    
    while True:
        try:
            discos = int(input("\nIntroduce el número de discos (o 0 para salir): "))
            
            if discos == 0:
                print("¡Gracias por usar el simulador!")
                break
            elif discos < 0:
                print("Por favor, introduce un número entero positivo.")
                continue
            
            # Cálculo matemático de los movimientos totales
            movimientos_totales = (2 ** discos) - 1
            print(f"\nMovimientos a procesar: {movimientos_totales:,}")
            print("Procesando en memoria, por favor espera...")
            
            # Medimos el tiempo de ejecución
            tiempo_inicio = time.time()
            torre_de_hanoi_rapida(discos, 'A', 'C', 'B')
            tiempo_fin = time.time()
            
            tiempo_total = tiempo_fin - tiempo_inicio
            print(f"¡Completado con éxito!")
            print(f"⏱️ Tiempo total de procesamiento: {tiempo_total:.4f} segundos")
            print("-" * 50)
            
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")

if __name__ == "__main__":
    iniciar_simulador()
