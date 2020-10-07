"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию 
и не завершиться с ошибкой.
"""



class CustomZeroDivisionError(Exception):
	
	def __init__(self, text):
		self.text = text
	

if __name__ == "__main__":
	while True:
		x = input('Вычислим значение дроби 1/x, введите x\n')
		try:
			x = float(x)
			if x == 0:
				raise CustomZeroDivisionError('деление на ноль не определено')
			fraction = 1 / x
		except ValueError:
			print('необходимо ввести число')
			continue
		except CustomZeroDivisionError as e:
			print(e)
			continue
		print(f'Значение:{fraction:.3f}')
		break
	
	