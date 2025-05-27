import time
import threading


def do(delay):
    print(f'Ожидание: {delay} с')
    time.sleep(delay)
    print(f'Работа окончена. Время: {delay} с')


th1 = threading.Thread(target=do, args=(1,))
th2 = threading.Thread(target=do, args=(0.5,))

start = time.perf_counter()

# do(1)
# do(0.5)

th1.start()
th2.start()

th1.join()
th2.join()

finish = time.perf_counter()

print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
