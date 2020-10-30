"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

if __name__ == '__main__':
    while True:
        seconds_str = input("Введите количество секунд (>0)\n")
        if seconds_str.isdigit():
            if int(seconds_str) > 0:
                break
    seconds = int(seconds_str)

    hours = seconds // 3600
    seconds = seconds - hours * 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60

    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
