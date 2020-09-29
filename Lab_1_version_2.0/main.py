import sys
from math import floor
from PyQt5 import QtWidgets
from layout import Ui_MainWindow


class window(QtWidgets.QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.encoder = None
        self.digitalCryptographySystem = None
        self.ui.pushButton.clicked.connect(lambda: self.polybius_code())
        self.ui.pushButton_2.clicked.connect(lambda: self.polybius_decode())
        self.ui.pushButton_3.clicked.connect(lambda: self.digitalCryptographySystem_code())
        self.ui.pushButton_4.clicked.connect(lambda: self.digitalCryptographySystem_decode())

    def polybius_code(self):
        self.encoder = Encoder(self.ui.lineEdit.text())
        self.ui.lineEdit_3.setText(self.encoder.code())

    def polybius_decode(self):
        self.encoder.decode()
        self.ui.lineEdit_2.setText(self.encoder.decode_text)

    def digitalCryptographySystem_code(self):
        self.digitalCryptographySystem = DigitalCryptographySystem(self.ui.lineEdit_4.text())
        self.digitalCryptographySystem.code()
        self.ui.lineEdit_5.setText(self.digitalCryptographySystem.encode_text)

    def digitalCryptographySystem_decode(self):
        self.digitalCryptographySystem.decode()
        self.ui.lineEdit_6.setText(self.digitalCryptographySystem.decode_text)


class Encoder:

    def __init__(self, text):
        self.text = text
        self.encode_text = ""
        self.decode_text = ""
        self.polybius_dictionary = {
            'a': '11', 'b': '12', 'c': '13', 'd': '14', 'e': '15',
            'f': '21', 'g': '22', 'h': '23', 'i': '24', 'j': '25',
            'k': '31', 'l': '32', 'm': '33', 'n': '34', 'o': '35',
            'p': '41', 'q': '42', 'r': '43', 's': '44', 't': '45',
            'u': '51', 'v': '52', 'w': '53', 'x': '54', 'y': '55',
            'z': '61'
        }

    def set_text(self, text):
        self.text = ""
        self.text = text

    def code(self):
        self.encode_text = ""
        list_text = list(self.text.lower())
        for char in list_text:
            if char in self.polybius_dictionary:
                self.encode_text += self.polybius_dictionary.get(char)
            else:
                self.encode_text += (char + char)

        return self.encode_text

    def decode(self):
        new_text = ""
        list_text = []
        step = 2
        for i in range(0, len(self.encode_text), 2):
            list_text.append(self.encode_text[i:step])
            step += 2

        keys_polybius_dictionary = list(self.polybius_dictionary.keys())
        values_polybius_dictionary = list(self.polybius_dictionary.values())

        for char in list_text:
            if char in values_polybius_dictionary:
                i = values_polybius_dictionary.index(char)
                new_text += keys_polybius_dictionary[i]
            else:
                new_text += char[0:1]
        self.decode_text = new_text


class DigitalCryptographySystem:

    def __init__(self, text):
        self.text = text
        self.encode_text = ""
        self.decode_text = ""
        self.dictionary = {
            'a': '2', 'b': '3', 'c': '4', 'd': '5', 'e': '6',
            'f': '7', 'g': '8', 'h': '9', 'i': '10', 'j': '11',
            'k': '12', 'l': '13', 'm': '14', 'n': '15', 'o': '16',
            'p': '17', 'q': '18', 'r': '19', 's': '20', 't': '21',
            'u': '22', 'v': '23', 'w': '24', 'x': '25', 'y': '26',
            'z': '27', '/': '1', '*': '0'
        }

    def set_text(self, text):
        self.text = ""
        self.text = text

    def code(self):
        text_list = list(self.text.lower())

        keys_dictionary = list(self.dictionary.keys())  #letter
        values_dictionary = list(self.dictionary.values())  #numbers

        for char in text_list:
            if char in keys_dictionary:
                value = int(self.dictionary[char])
                if value % 2 == 0:
                    first_code_value = str(int(value / 2))
                    second_code_value = str(int(value / 2))
                else:
                    first_code_value = str(floor(value / 2))
                    second_code_value = str(floor((value / 2)) + 1)

                index_first_code_value = values_dictionary.index(first_code_value)
                index_second_code_value = values_dictionary.index(second_code_value)
                self.encode_text += keys_dictionary[index_first_code_value] + keys_dictionary[
                    index_second_code_value]
        return self.encode_text

    def decode(self):
        new_text = []

        step = 2
        for i in range(0, len(self.encode_text), 2):
            new_text.append(self.encode_text[i:step])
            step += 2

        keys_dictionary = list(self.dictionary.keys())  # letter
        values_dictionary = list(self.dictionary.values())  # numbers

        for char in new_text:
            first_char = list(char)[0]
            second_char = list(char)[1]

            number_value_first_char = int(self.dictionary[first_char])
            number_value_second_char = int(self.dictionary[second_char])

            res_number_value = str(number_value_first_char + number_value_second_char)
            index_char = values_dictionary.index(res_number_value)
            self.decode_text += keys_dictionary[index_char]


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = window()
    application.show()

    sys.exit(app.exec())