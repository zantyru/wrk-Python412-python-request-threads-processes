import time
import threading


FILE_NAME = 'prak3_input.txt'


def is_odd(number):
    return number % 2 == 1


def is_even(number):
    return number % 2 == 0


def save_numbers(input_file_name, fn_rule, output_file_name):
    with open(input_file_name, 'r', encoding='utf-8') as in_f,\
            open(output_file_name, 'w', encoding='utf-8') as out_f:
        for line in in_f:
            number = int(line)
            if fn_rule(number):
                out_f.write(str(number))
                out_f.write('\n')


th1 = threading.Thread(
    target=save_numbers,
    args=(FILE_NAME, is_even, 'prak3_output_even.txt')
)
th2 = threading.Thread(
    target=save_numbers,
    args=(FILE_NAME, is_odd, 'prak3_output_odd.txt')
)

start = time.perf_counter()
th1.start()
th2.start()
th1.join()
th2.join()
finish = time.perf_counter()
print(f'Финиш! Потрачено времени: {round(finish - start, 2)} с')
