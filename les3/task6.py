"""
Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    """
    self-made title() for a single word

    :param word: ascii latin word
    :return: ascii latin Word (first letter capital)
    """
    if not len(word):
        return word

    first_char_code = ord(word[0])
    # first_char_code between 'a' and 'z'
    if 97 <= first_char_code <= 122:
        # a -> A...z->Z
        return chr(first_char_code - 32) + word[1:]
    else:
        return word


if __name__ == "__main__":
    string = input('Введите латинские слова, разделенные пробелом\n')
    print('Каждое латинское слово с заглавной буквы:\n')
    words = string.split(' ')
    final_string = ''
    for word in words:
        print(int_func(word), end=' ')
