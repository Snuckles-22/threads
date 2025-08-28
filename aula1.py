# importação de biblioteca

import threading
import time # biblioteca de tempo
import math # biblioteca de matemática

# estrututa da thread

def loop(nome, inicio, fim):
    for i in range(inicio, fim +1):
        print(f"{nome} -> {i}")

# pausa entre as durações de contagem
        time.sleep(1)

# criar thread
thread1 = threading.Thread(target=loop, args=("Thread-1", 1, 10))
thread2 = threading.Thread(target=loop, args=("Thread-2", 11, 20))

# rodar
thread1.start()
thread2.start()

# estado de espera
thread1.join()
thread2.join()


