"""
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
"""

if __name__ == "__main__":

    product_template = {
        'название': ("имя товара", str),
        'цена': ("стоимость товара", int),
        'количество': ("количество товара", int),
        'единица измерения': ("Единицы измерения (шт, кг и т.д.)", str)
    }

    next_inter = True
    auto_inc = 1
    product_list = []

    while next_inter:
        product = {}
        # fill product by template
        for key, value in product_template.items():
            while True:
                # value[0] is prompt
                user_value = input(f'{value[0]}\n')
                try:
                    # value[1] is type cast
                    user_value = value[1](user_value) # int(user_value)
                except ValueError as e:
                    print("{e}\nНеверное значение данных")
                    continue
                product[key] = user_value
                break
        product_list.append((auto_inc, product))
        auto_inc += 1

        # check if need continue
        while True:
            next_add = input("Добавить еще продукт? Да/Нет\n")
            if next_add.lower() in ['да', 'нет']:
                next_inter = next_add.lower() == 'да'
                break
            else:
                print('Неверный ввод, повторите')

    print(product_list)

    product_analytics = {}
    # fill analytics dictionary
    for key in product_template:
        result = []
        for itm in product_list:
            result.append(itm[1][key])

        product_analytics[key] = result

    print(product_analytics)
