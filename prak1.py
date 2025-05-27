import time
import threading
import random as rnd


start = time.perf_counter()
L = [
    rnd.randint(-20_000_000, 20_000_000)
    for _ in range(20_000_000)
]
finish = time.perf_counter()
print(f'Время создания списка: {round(finish - start, 2)} с')


th1 = threading.Thread(target=lambda x: print(min(x)), args=(L,))
th2 = threading.Thread(target=lambda x: print(max(x)), args=(L,))

start = time.perf_counter()
th1.start()
th2.start()
th1.join()
th2.join()
finish = time.perf_counter()
print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
