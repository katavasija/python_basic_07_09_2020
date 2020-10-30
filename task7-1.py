"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
"""


class Cell:
    """
    a cell of a matrix
    """

    def __init__(self, value: float):
        self.__value = float(value)

    def __format__(self, format_spec):
        return f'{self.__value:{format_spec}}'

    def __add__(self, other) -> float:
        """
        :param other: Cell
        :return: sum of self and other values
        """
        return self.value + other.value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, outer_value):
        self.__value = float(outer_value)


class CellAggregator:
    """
    a row or a column of a matrix
    contains a list of values
    :param idx: row or column idx (starting at 0)
    """
    def __init__(self, idx: int):
        self.__idx = int(idx)
        self.__cells = []

    @property
    def idx(self):
        return self.__idx

    @property
    def length(self):
        return len(self.__cells)

    def add_cell(self, cell: Cell):
        self.__cells.append(cell)

    def add_cells_by_values(self, *args):
        for cell_value in args:
            self.add_cell(Cell(cell_value))

    def __iter__(self):
        return self.__cells.__iter__()

    def __getitem__(self, cell_idx: int) -> float:
        return self.__cells[cell_idx]

class Matrix:
    """
    matrix with rows as cell aggregators
    add columns aggregators if needed
    """
    def __init__(self, matrix_data, name = ''):
        self.__rows = []
        self.name = name
        row_idx = 0
        for row_values_list in matrix_data:
            row = CellAggregator(row_idx)
            row_idx += 1
            row.add_cells_by_values(*row_values_list)
            self.__rows.append(row)

    def __getitem__(self, row_idx: int) -> tuple:
        """tuple of row elements"""
        return tuple(self.__rows[row_idx])

    @property
    def row_count(self):
        return len(self.__rows)

    def __add__(self, other):
        new_matrix_data = []
        for i in range(self.row_count):
            row_self = list(self[i])
            row_other = list(other[i])
            new_matrix_data.append([a+b for a,b in zip(row_self, row_other)])
        return type(self)(new_matrix_data, 'Результат сложения')

    def __str__(self):
        """
        :return: matrix to str
        """
        def row_sep(row: CellAggregator) -> str:
            """auxiliary row separator"""
            return '-' * 8 * row.length

        def row_to_str(row: CellAggregator) -> str:
            """auxiliary row string"""
            row_values_str = ''
            for v in row:
                row_values_str += f'|{v:6}|'
            return f'{row_sep(row)}\n{row_values_str}\n'

        matrix_str = ''
        for row in self.__rows:
            matrix_str += row_to_str(row)
        matrix_str += row_sep(row)
        return f'Матрица {self.name}\n {matrix_str}\n'

    def get_cell_value(self, row_idx: int, col_idx: int) -> float:
        return self.__rows[row_idx][col_idx].value


if __name__ == "__main__":
    matrix_data = [[1, 2, 5, 6], [9, 10, 11, 12]]
    m1 = Matrix(matrix_data, 'm1')
    print(m1)
    matrix_data = [[4, 4, 5, 6], [-5, -6, -8, 12]]
    m2 = Matrix(matrix_data, 'm2')
    print(m2)
    print(m1 + m2)
