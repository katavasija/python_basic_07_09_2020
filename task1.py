"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
"""


class RawStringDateFormatError(Exception):
	def __init__(self, text):
		self.text = text

class LogicDateValueError(Exception):
	def __init__(self, text):
		self.text = text


class NaiveDate:
	"""
	Gregorian calendar date (01.01.0001 - 31.12.3000)
	"""
	FORMAT_TEMPLATE = 'yyyy-mm-dd'

	@classmethod
	def extract_date_parts(cls, date_str):
		"""
		ensure date_str is 'yyyy-mm-dd' format
		extract yyyy , mm, dd to integer values
		without validation
		"""
		try:
			wrong_format = False
			# cycle instead of gotos
			while True:
				date_parts = date_str.split('-')
				# 'yyyy-mm-dd' or 'yyy-mm-dd' fits format
				if len(date_str) < len(NaiveDate.FORMAT_TEMPLATE) - 1 or len(date_parts) != 3:
					wrong_format = True
					break
				for dp in date_parts:
					if not dp.isdigit():
						wrong_format = True
						break
				year = int(date_parts[0])
				month = int(date_parts[1])
				day = int(date_parts[2])
				break
			if wrong_format:
				raise RawStringDateFormatError(f"	неверный формат даты '{date_str}'")
			return year,month,day
		except Exception as ex:
				print(f"	не удалось определить год, месяц или день в значении '{date_str}'")
				print(f"	ожидается значение в формате '{NaiveDate.FORMAT_TEMPLATE}'")
				print(ex)
				# exit(1)
				return 0,0,0

	@staticmethod
	def validate(yyyy, mm, dd):
		"""
		validate yyyy, mm, dd 
		as date
		"""
		def isLeapYear(year):
			if year % 4 != 0:
				return False
			else:
				if year % 100 != 0:
					return True
				else:
					if year % 400 != 0:
						return False
					else:
						return True

		valid = True
		try:
			while True:
				if yyyy > 3000 or yyyy < 1:
					valid = False
					raise LogicDateValueError('	значение года задано неверно, должно быть в диапазоне [1; 3000]')
					break
				if mm > 12 or mm < 1:
					valid = False
					raise LogicDateValueError('	значение месяца задано неверно, должно быть в диапазоне [1; 12]')
					break
				if dd > 31 or dd < 1:
					valid = False
					raise LogicDateValueError('	значение дня задано неверно, должно быть в диапазоне [1; 12]')
					break
				if dd > 30:
					if mm not in [1, 3, 5, 7, 8, 10, 12]:
						valid = False
						raise LogicDateValueError('	значение дня задано неверно, должно быть не больше 30 для месяца {mm}')
				if mm == 2:
					if not isLeapYear(yyyy) and dd > 28:
						valid = False
						raise LogicDateValueError(f'	значение дня задано неверно, должно быть не больше 28 для месяца {mm}')
				break
			return valid
		except Exception as ex:
				print(f'дата, заданная значениями года {yyyy}, месяца {mm}, дня {dd} неверна')
				print(ex)
				return False


	def __init__(self, date_str):
		y,m,d = NaiveDate.extract_date_parts(date_str)
		# print(y,m,d)
		if y and m and d:
			if (NaiveDate.validate(yyyy=y, mm=m, dd=d)):
				print(f'дата {date_str} задана верно')


	def __str__(self):
		return f'{(self.a, self.b)}' 


if __name__ == "__main__":
	d = NaiveDate('2024 13-31')
	d = NaiveDate('333-33-33')
	d = NaiveDate('2020-02-29')
	d = NaiveDate('2021-02-29')

