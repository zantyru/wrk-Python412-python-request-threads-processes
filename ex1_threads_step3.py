import time
import concurrent.futures


def do(delay):
    time.sleep(delay)
    return f'Работа окончена. Время: {delay} с'


delays = [3, 1, 5, 2, 4]


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    result_1 = executor.submit(do, 1)
    result_2 = executor.submit(do, 0.5)
    print(result_1.result())
    print(result_2.result())

finish = time.perf_counter()


print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
