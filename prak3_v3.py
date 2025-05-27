import time
import threading


def is_odd(number):
    return number % 2 == 1


def is_even(number):
    return number % 2 == 0


def save_numbers(fn_rule):
    lock = threading.Lock()
    INPUT_FILE_NAME = 'prak3_input.txt'
    OUPUT_FILE_NAME = 'prak3_output.txt'
    with open(INPUT_FILE_NAME, 'r', encoding='utf-8') as in_f,\
            open(OUPUT_FILE_NAME, 'w', encoding='utf-8') as out_f:
        for line in in_f:
            number = int(line)
            if fn_rule(number):
                with lock:
                    out_f.write(f'{fn_rule.__name__} {str(number)}')
                    out_f.write('\n')



th1 = threading.Thread(target=save_numbers, args=(is_even,))
th2 = threading.Thread(target=save_numbers, args=(is_odd,))

start = time.perf_counter()
th1.start()
th2.start()
th1.join()
th2.join()
finish = time.perf_counter()
print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
