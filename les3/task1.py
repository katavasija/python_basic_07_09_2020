"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
"""


def a_divide_b(a, b):
    """
    :param a:
    :param b:
    :return: float or None
    """

    def print_mistype_message(param_name, param_value):
        print(f"Внимание! Неверный тип параметра '{param_name}' со значением '{param_value}'.")

    def print_zero_error_message():
        print(f"Внимание! Делитель не может принимать значение '0'.")

    def check_param_type(param_name, param_value):
        if not str(param_value).isdigit():
            print_mistype_message(param_name, param_value)
            return False
        else:
            return True

    is_a_valid = check_param_type('a', a)
    is_b_valid = check_param_type('b', b)
    if is_a_valid and is_b_valid:
        a = float(a)
        b = float(b)
        if b != 0:
            return a / b
        else:
            print_zero_error_message()
            return None
    return None


if __name__ == "__main__":
    a = input("Введите a\n")
    b = input("Введите b\n")
    print(f"Результат деления a на b: {a_divide_b(a, b)}")
