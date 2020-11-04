"""
 Реализовать проект «Операции с комплексными числами». 
 Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
 Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
"""

class NaiveComplex:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return f'{(self.a, self.b)}' 

	def __add__(self, other):
		"""
		Override addition
		"""
		return type(self)(self.a + other.a, self.b + other.b)

	def __mul__(self, other):
		"""
		Override multiplication
		"""
		a_mul = self.a * other.a - self.b * other.b
		b_mul = self.a * other.b + self.b * other.a
		return type(self)(a_mul, b_mul)



if __name__ == "__main__":
	i1 = NaiveComplex(2, 3)
	print(f'i1:{i1}')
	i2 = NaiveComplex(-1, 1)
	print(f'i2:{i2}')
	print(f'i1+i2={i1 + i2}')
	print(f'i1*i2={i1 * i2}')
	