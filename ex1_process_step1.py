import time
import multiprocessing


def do(delay):
    print(f'Ожидание: {delay} с')
    time.sleep(delay)
    print(f'Работа окончена. Время: {delay} с')


if __name__ == '__main__':
    delays = [60, 1, 50, 20, 4]
    processes = []

    start = time.perf_counter()

    for delay in delays:
        th = multiprocessing.Process(target=do, args=(delay,))
        th.start()
        processes.append(th)

    for process in processes:
        process.join()
        print('*')

    finish = time.perf_counter()

    print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
