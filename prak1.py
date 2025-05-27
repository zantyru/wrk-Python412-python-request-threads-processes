from multiprocessing import Process, Queue


MSG_INFO = 0
MSG_SYMBOL = 1


def game(queue_in, queue_out):

    import random as rnd

    word = rnd.choice([
        'охотник' , 'компьютер', 'верёвка',
        'экскаватор', 'бульдог'
    ])

    info = f'Загадано слово. Длина: {len(word)}'
    queue_out.put([MSG_INFO, info])

    letter_mask = [0] * len(word)

    is_word_revealed = False
    while not is_word_revealed:
        message_type, message_data = queue_in.get()

        if message_type == MSG_INFO:
            if message_data.lower() in ('stop', 'стоп', 'exit', 'quit'):
                info = f'Инициирован выход...'
                queue_out.put([MSG_INFO, info])
                break

        elif message_type == MSG_SYMBOL:
            symbol = message_data[0] if len(message_data) > 0 else ''
            for i, letter in enumerate(word):
                if letter == symbol:
                    letter_mask[i] = 1

            if all(letter_mask):
                is_word_revealed = True

            info = ''.join(
                '.' if mask == 0 else letter
                for mask, letter in zip(letter_mask, word)
            )
            queue_out.put([MSG_INFO, info])

    info = 'stop'
    queue_out.put([MSG_INFO, info])


def main():
    queue_in = Queue()
    queue_out = Queue()

    game_process = Process(target=game, args=(queue_out, queue_in))
    game_process.start()

    message_type, message_data = queue_in.get()
    print(message_data)

    is_finished = False
    while not is_finished:

        letter = input('Буква или команда (stop, exit, стоп, quit): ')
        if len(letter) > 1:
            queue_out.put([MSG_INFO, letter])
        else:
            queue_out.put([MSG_SYMBOL, letter])

        message_type, message_data = queue_in.get()
        if message_type == MSG_INFO:
            if message_data == 'stop':
                is_finished = True
                print('Да, завершаем работу.')

            else:
                print(message_data)


if __name__ == '__main__':
    main()
