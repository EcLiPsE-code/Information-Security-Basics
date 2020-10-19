class Playfir:
    def __init__(self) -> None:
        self._message: str = None
        self._key: str = None
        self._alphabet: str = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        self._key_matrix = None

    def set_key(self, key) -> None:
        self._key = key

    def set_message(self, message) -> None:
        self._message = message

    def get_key(self) -> str:
        return self._key

    def get_message(self) -> str:
        return self._message

    def get_key_matrix(self):
        return self._key_matrix

    # генерация таблицы, содержащая введенный ключ матрциы
    def generate_key_matrix(self):
        self._key_matrix = [[0 for i in range(4)]
                            for j in range(8)]
        list_letters = list(self._alphabet)  # массив букв алфавита
        key_list_letter = list(self._key)  # массив букв введенного ключа
        for i in range(4):
            for j in range(8):
                if



class Task2:
    def __init__(self) -> None:
        self._count_row_first_matrix: int = None
        self._count_col_first_matrix: int = None
        self._count_row_second_matrix: int = None
        self._count_col_second_matrix: int = None
        self._first_matrix = None
        self._second_matrix = None
        self._result_matrix = None

    def set_first_matrix(self, matrix) -> None:
        self._first_matrix = matrix

    def set_second_matrix(self, matrix) -> None:
        self._second_matrix = matrix

    def set_row_count_first_matrix(self, row: int) -> None:
        self._count_row_first_matrix = row

    def set_col_count_first_matrix(self, col: int) -> None:
        self._count_col_first_matrix = col

    def set_row_count_second_matrix(self, row: int) -> None:
        self._count_row_second_matrix = row

    def set_col_count_second_matrix(self, col: int) -> None:
        self._count_col_second_matrix = col

    def get_first_matrix(self):
        for i in range(self._count_row_first_matrix):
            for j in range(self._count_col_first_matrix):
                print("{}".format(self._first_matrix[i][j]), end="\t")
            print()

    def get_second_matrix(self):
        for i in range(self._count_row_first_matrix):
            for j in range(self._count_col_first_matrix):
                print("{}".format(self._second_matrix[i][j]), end="\t")
            print()

    def get_result_matrix(self):
        for i in range(len(self._result_matrix)):
            for j in range(len(self._result_matrix[0])):
                print("{}".format(self._result_matrix[i][j]), end="\t")
            print()

    def get_count_row_first_matrix(self) -> int:
        return self._count_row_first_matrix

    def get_count_col_first_matrix(self) -> int:
        return self._count_col_first_matrix

    def get_count_row_second_matrix(self) -> int:
        return self._count_row_second_matrix

    def get_count_col_second_matrix(self) -> int:
        return self._count_col_second_matrix

    # проверка совместимости матриц
    def compatibility_check(self) -> bool:
        if self._count_col_first_matrix != self._count_row_second_matrix:
            return False
        else:
            return True

    def multiply_matrix(self):
        self._result_matrix = [[0 for i in range(self._count_col_second_matrix)]
                               for j in range(self._count_row_first_matrix)]
        for i in range(self._count_row_first_matrix):
            for k in range(self._count_col_second_matrix):
                for i in range(self._count_row_first_matrix):
                    temp = 0
                    for j in range(self._count_row_second_matrix):
                        temp += self._first_matrix[i][j] * self._second_matrix[j][k]
                        self._result_matrix[i][k] = temp


def menu():
    print("----------------------MENU--------------------")
    print("1) Шифр Плейфера (для русского алфавита       ")
    print("2) Метод умножения матриц                     ")
    print("3) Решетка Кардано                            ")
    print("4) Выход                                      ")
    print("----------------------------------------------")


if __name__ == '__main__':
    flag = True
    while flag:
        menu()
        print("Введите пункт меню: ")
        k = int(input())
        if k == 1:
            playfir = Playfir()
            print("Введите ключ:")
            playfir.set_key(input())
            print("Введите сообщение, которое необходимо зашифровать:")
            playfir.set_message(input())
        elif k == 2:
            task2 = Task2()
            print("Введите кол-во строк первой матрицы:")
            task2.set_row_count_first_matrix(int(input()))
            print("Введите кол-во столбцов первой матрицы:")
            task2.set_col_count_first_matrix(int(input()))
            print("Введите первую матрицу:")
            task2.set_first_matrix([(list(map(int, input().split())))
                                    for i in range(task2.get_count_row_first_matrix())])

            print("Введите кол-во строк второй матрицы:")
            task2.set_row_count_second_matrix(int(input()))
            print("Введите кол-во столбцов второй матрицы:")
            task2.set_col_count_second_matrix(int(input()))
            print("Введите вторую матрицу:")
            task2.set_second_matrix([(list(map(int, input().split())))
                                     for i in range(task2.get_count_row_second_matrix())])
            if task2.compatibility_check():
                print("Выполняем умножение матриц")
                print("Первая матрица: ")
                task2.get_first_matrix()
                print("Вторая матрица:")
                task2.get_second_matrix()
                print("Результат умножения матриц:")
                task2.multiply_matrix()
                task2.get_result_matrix()
            else:
                print("Умножение не возможно")
        elif k == 3:
            pass
        elif k == 4:
            flag = False
            break
        else:
            print("Такого пункта меню нет!")
