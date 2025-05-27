from multiprocessing import Process, Queue


def process_code(queue_input, queue_output):
    while True:
        print(f'[CHILD] Ожидание данных...')
        i = queue_input.get()
        print(f'[CHILD] Получено: {i}')

        if i >= 100:
            print('[CHILD] Завершение...')
            break

        i += 1
        print(f'[CHILD] Отправка: {i}')
        queue_output.put(i)


if __name__ == '__main__':
    queue_1 = Queue()
    queue_2 = Queue()

    process = Process(target=process_code, args=(queue_1, queue_2))
    process.start()

    i = 0
    while True:

        print(f'[MAIN] Отправка: {i}')
        queue_1.put(i)

        i = queue_2.get()
        print(f'[MAIN] Получено: {i}')

        if i == 100:
            print('[MAIN] Завершение...')
            break
