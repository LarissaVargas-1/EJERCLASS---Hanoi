# EJERCLASS---Hanoi
Este programa maneja 4 métodos:

° init self es el método que se encarga de inicializar las variables

°revolver recursivo es el método que se encarga de la logica del algoritmo de la torre y es el que se llama recusivamente

°ejecutar simulación es el encargado de calcular los movimientos, pone el cronometro y llama al método recursivo

°menú interectivo es la interfaz del usuario es la que te pide ingresar el número de discos y verifica si es correcto

Al momento de medir el tiempo dio:

con 5 discos 0.0 segundos
con 10 discos 0.0002 segundos
con 30 discos 141.5143 segundos
con 64 discos siguió procesándose hasta que busque un aproximado del tiempo que tomaría y seguiría indefinidamente hasta causar un error

Conclusiones

Al momento de buscar el programa de la torre se encontró uno sencillo que solo tenia ingresado tres dígitos, luego se pidió uno donde se pudiera modificar la cantidad de discos y al intentar ingresar las primeras dos cantidades no tardo mucho pero al ingresar la cantidad de 30 discos empezó a tarda mas tiempo por lo que investigue cuanto tardaría aproximadamente encontré que tardaría menos si le quitara los print ya que los movimientos se harían directamente en la memoria sin mostrar todos los mensajes de los movimientos así que pedí las modificaciones con un extra para medir el tiempo de procesamiento. Al llegar a los 64 discos se complico pues el programa no dejo de ejecutarse ahí fue cuando se descubrió que 64 discos continuaría indefinidamente hasta mostrar un mensaje de error por el desbordamiento de memoria.

