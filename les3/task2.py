"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(**kwargs):
    """
    :param kwargs:
    name, surname, year_birth, city, email, tel
    :return: string of user data
    """
    name = kwargs.get('name', '<name>')
    surname = kwargs.get('surname', '<surname>')
    year_birth = kwargs.get('year_birth', '<year_birth>')
    city = kwargs.get('city', '<city>')
    email = kwargs.get('email', '<email>')
    tel = kwargs.get('tel', '<tel>')

    print(f"{surname} {name} was born in {year_birth}, currently located in {city}. Contacts:{tel}, {email}")

if __name__ == "__main__":
    user_data(name="Kostya", surname="Romanenko", year_birth="1981", city="KRSK", email="mail@mail.ru")
