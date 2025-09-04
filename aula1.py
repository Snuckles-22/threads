#importação de bibliotecas
import threading
import time

#estrutura de thread
def estrutura(nome,inicio,fim):
    for i in range(inicio,fim +1):
        print(f"{nome} -> {i}")

#criação das threads

thread1 = threading.Thread(target=estrutura, args=("Thread-1",1,10))
thread2 = threading.Thread(target=estrutura, args=("Thread-2",50,60))


#tempo de espera
print("Iniciando as threads...")
time.sleep(2)

#rodar as threads
thread1.start()
thread2.start()

#estado de espera
thread1.join()
thread2.join()

print("Threads finalizadas!")

