"""
Начните работу над проектом «Склад оргтехники». 
Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""
from abc import ABC, abstractmethod


class Equipment(ABC):

	def __init__(self, inental_num, model_name):
		self.inental_num = inental_num
		self.model_name = model_name
		self.add_to_warehouse()


	@property
	def inental_num(self):
		return self.__inental_num

	@inental_num.setter
	def inental_num(self, val):
		assert val.isalnum(), 'инвентарный номер - обязательное строковое поле'
		assert not WareHouse.exists_intental_num(val), f'значение поля "{val}" (инвентарный номер) должно быть уникально'
		self.__inental_num = val

	@property
	def model_name(self):
		return self.__model_name

	@model_name.setter
	def model_name(self, val):
		assert val.isalnum(), 'название модели - обязательное строковое поле'
		self.__model_name = val

	@abstractmethod
	def add_to_warehouse(self):
		pass


class Printer(Equipment):
	
	def __init__(self, inental_num, model_name):
		super().__init__(inental_num, model_name)

	def add_to_warehouse(self):
		WareHouse.add(self, WareHouse.PRINTER_KEY)



class WareHouse:
	PRINTER_KEY = 'printer'
	SCANNER_KEY = 'scanner'
	XEROX_KEY = 'xerox'
	NA_KEY = 'na'
	__box = {PRINTER_KEY: [], SCANNER_KEY: [], XEROX_KEY:[]}
	__inental_num_index = []

	@classmethod
	def add(cls, equipment, equipment_key):
		if not cls.exists_intental_num(equipment.inental_num):
			equipment_list = cls.__box[equipment_key]
			equipment_list.append(equipment)
			cls.__inental_num_index.append(equipment.inental_num)
		else:
			print(f'"Оргтехника" {equipment.model_name} не может быть добавлена на склад. Значение инвентарного номера {equipment.inental_num} не уникально.')

	@classmethod
	def exists_intental_num(cls, inental_num):
		return inental_num in cls.__inental_num_index

	@classmethod
	def add_intental_num(cls, inental_num):
		assert inental_num.isalnum(), 'инвентарный номер не может быть пустым'
		assert not cls.exists_intental_num(inental_num), f'значение "{inental_num}" в качестве инвентарного номера не уникально'
		cls.__inental_num_index.append(inental_num)


if __name__ == "__main__":
	printer1 = Printer(inental_num="SDKFJ3", model_name="Canon25")
	printer2 = Printer(inental_num="SDKFJ4", model_name="HP36")
	# printer3 = Printer(inental_num="SDKFJ3", model_name="LG37")

