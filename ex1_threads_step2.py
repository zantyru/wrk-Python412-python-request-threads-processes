import time
import threading


def do(delay):
    print(f'Ожидание: {delay} с')
    time.sleep(delay)
    print(f'Работа окончена. Время: {delay} с')


delays = [3, 1, 5, 2, 4]
threads = []

start = time.perf_counter()

for delay in delays:
    th = threading.Thread(target=do, args=(delay,))
    threads.append(th)
    th.start()

for thread in threads:
    thread.join()
    print('*')

finish = time.perf_counter()

print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
