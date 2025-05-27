import time
import concurrent.futures


def do(delay):
    print(f'Начало задержки: {delay} с')
    time.sleep(delay)
    return f'Работа окончена. Время: {delay} с'


delays = [3, 1, 5, 2, 4]


start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # results = [executor.submit(do, delay) for delay in delays]
    #
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executor.map(do, delays)

    for result in results:
        print(result)

finish = time.perf_counter()


print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
