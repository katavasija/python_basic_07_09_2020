"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. 
Необходимо запрашивать у пользователя данные и заполнять список. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. 
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. 
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, 
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) 
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться
"""


class FloatValueErrorException(Exception):
	
	def __init__(self, text):
		self.text = text


class FloatNumbersList:
	
	def __init__(self):
		self.__list = []
	
	def input_and_print_list(self):
		"""
		To append only float numbers, got by input.
		Use type checking and custom exception.
		Expect "stop" substring to break the input cycle.
		Print list.
		"""
		while True:
			x = input('Введите число для добавления в список, "stop" чтобы прекратить ввод\n')
			if "stop" in x.lower():
				break
				
			try:
				if not x.isdigit():
					raise FloatValueErrorException('необходимо ввести число или "stop"')
				else:
					self.__list.append(x)
			except FloatValueErrorException as err:
				print(err)
				continue
		if len(self.__list):
			print(self.__list)
		else:
			print('список пуст')


if __name__ == "__main__":
	fn_list = FloatNumbersList()
	fn_list.input_and_print_list()
	