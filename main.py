import re
import json
import argparse
from tqdm import tqdm


class Validator:
    """
        Объект Validator репрезентует класс для валидации данных.
        Attributes
          ----------
          __email - хранит почту  соответствующей записи
          __height - хранит рост соответствующей записи
          __inn - хранит ИНН соответствующей записи
          __passport_series - хранит серию паспорта соответствующей записи
          __age - хранит возраст соответствующей записи
          __address - хранит адрес соответствующей записи
          __occupation - хранит значение профессии соответствующей записи
          __political_views - хранит значение политических взглядов соответствующей записи
          __worldview - хранит значение мировоззрения соответствующей записи
          __occupation_invalid - хранит невалидные значения профессии
          __political_views_invalid - хранит невалидные значения политических взглядов
          __worldview_invalid - хранит невалидные значения мировоззрения
    """
    __email: str
    __height: float
    __inn: str
    __passport_series: str
    __age: int
    __address: str
    __occupation: str
    __political_views: str
    __worldview: str
    __occupation_invalid = ['Монах', 'Паладин', 'Маг', 'Вышивальщица', 'Маникюрша', 'Цветочница']
    __political_views_invalid = ['согласен с действиями Гарроша Адского Крика на посту вождя Орды',
                                 'патриот независимой Темерии', 'поддерживает Братьев Бури',
                                 'поддерживает Имперский легион']
    __worldview_invalid = ['Культ проклятых', 'Культ Механикус', 'Храм Трибунала', 'Светское гачимученничество',
                           'культ богини Мелитэле', 'Девять божеств', 'Культ пророка Лебеды', 'Культ Вечного Огня']

    def __init__(self, email: str, height: float, inn: str, passport_series: str, age: int, occupation: str,
                 political_views: str,
                 worldview: str, address: str):
        """
            __init__ - инициализирует экземпляр класса Validator
            Parameters
            ----------
            email : str
            height: float
            inn: str
            passport_series: str
            age: int
            occupation: str
            political_views: str
            worldview: str
            address: str
            Путь до выбранного файла
        """
        self.__email = email
        self.__height = height
        self.__inn = inn
        self.__passport_series = passport_series
        self.__age = age
        self.__address = address
        self.__occupation = occupation
        self.__political_views = political_views
        self.__worldview = worldview

    def check_email(self) -> bool:
        """
        Выполняет проверку корректности адреса электронной почты.
        Если в строке присутствуют пробелы, запятые, двойные точки,
        а также неверно указан домен адреса, то будет возвращено False.
        :return: bool
        Булевый результат проверки на корректность
        """
        if re.match(r"\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}", self.__email) is not None:
            return True
        return False

    def check_height(self) -> bool:
        """"
        Проверка корректности роста
        Если строка содержит дробное число с разделителем возвращает True, иначе False
        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\d{1,2}\.\d{1,2}$", str(self.__height)) is not None and (float(self.__height) > 1.00) and \
                (float(self.__height) < 2.50):
            return True
        return False

    def check__inn(self) -> bool:
        """
        Проверка корректности ИНН
        Если строка содержит 12 цифр [0-9] возвращает True, иначе False
        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\d{12}$", self.__inn) is not None:
            return True
        return False

    def check_passport_series(self) -> bool:
        """
        Выполняет проверку корректности записи серии паспорта.
        Если записано не 5 знаков, или не записано два числа через пробел, то возвращает False.
        Иначе True.
        :return: bool
        Булевый результат проверки на корректность
        """
        if len(self.__passport_series) == 5 and re.match(r"\d{2}\s\d{2}", self.__passport_series) is not None:
            return True
        return False

    def check_age(self) -> bool:
        """
        Проверка корректности возраста
        Если строка содержит 2 цифры [0-9] и удовлетворяет условию возвращает True, иначе False
        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^\d{2}$", str(self.__age)) is not None and (int(self.__age) > 14) and (int(self.__age) < 99):
            return True
        return False

    def check_address(self) -> bool:
        """
        Проверку корректности адреса.
        Если строка начинается с ул. или не начинается с Алллея возвращает True, иначе False.
        :return: bool
        Булевый результат проверки
        """
        if re.match(r"^(ул\.)?(Аллея)?\s[\w\.\s-]+\d+$", self.__address) is not None:
            return True
        return False

    def check_occupation(self) -> bool:
        """
        Проверка корректности записи профессии
        Если строка начинается с букв [A-Z][А-Я], не содержит цифр
        и не входит в невалидные значения возвращает True, иначе False.
        :return: bool
        Булевый результат проверки
        """
        if self.__occupation not in self.__occupation_invalid and re.match(r"^([A-Z]|[А-Я])[\D]+$", self.__occupation) \
                is not None:
            return True
        return False

    def check_political_views(self) -> bool:
        """
        Проверка корренктности записи политических взглядов
        Если строка содержит только буквы [А-Я][а-я] и не входит в невалидные значения возвращает True, иначе False.
        :return:
        Булевый результат проверки
        """
        if self.__political_views not in self.__political_views_invalid and \
                re.match(r"^[\D]+$", self.__political_views) is not None:
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Проверка корректности записи мировозрения
        Если строка содержит только буквы [А-Я][а-я] и не входит в невалидные значения возвращает True, иначе False.
        :return:
        Булевый результат проверки
        """
        if self.__worldview not in self.__worldview_invalid and \
                re.match(r"^[\D]+$", self.__worldview) is not None:
            return True
        return False

    def check_all(self) -> int:
        """
        Выполнение всех проверок класса
        :return: int
        Целочисленный результат (номер невалидного значения)
        """
        if not self.check_email():
            return 0
        elif not self.check_height():
            return 1
        elif not self.check__inn():
            return 2
        elif not self.check_passport_series():
            return 3
        elif not self.check_age():
            return 4
        elif not self.check_occupation():
            return 5
        elif not self.check_address():
            return 6
        elif not self.check_political_views():
            return 7
        elif not self.check_worldview():
            return 8
        else:
            return 9


class ReadFile:
    """
    Объект ReadFile считывает и хранит данные из выбранного файла.
    Attributes
      ----------
      __data - хранит данные, считанные из файла
    """

    __data: object

    def __init__(self, path: str):
        """
        __init__ - инициализирует экземпляр класса ReadFromFile
        Parameters
        ----------
        path : str
        Путь до выбранного файла
        """
        self.__data = json.load(open(path, encoding='windows-1251'))

    @property
    def data(self) -> object:
        """
        data - метод получения данных файла
        :return: object
        Возвращает тип object
        """
        return self.__data


parser = argparse.ArgumentParser(description='main')
parser.add_argument('-input', dest="file_input", default='87.txt', type=str)
parser.add_argument('-output', dest="file_output", default='87_output.txt', type=str)
args = parser.parse_args()
output = open(args.file_output, 'w')
file = ReadFile(args.file_input)
checkers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
number_of_valid_records = 0
with tqdm(file.data, desc='Прогресс валидации', colour="#FFFFFF") as progressbar:
    for elem in file.data:
        check_element = Validator(elem['email'], elem['height'], elem['inn'], elem['passport_series'],
                                  elem['age'],
                                  elem['occupation'], elem['political_views'], elem['worldview'], elem['address'])
        valid_values = check_element.check_all()
        if valid_values == 9:
            output.write("email: " + elem["email"] + "\n" + "height:" + str(elem["height"]) + "\n" +
                         "inn: " + elem["inn"] + "\n" + "passport_series:" + str(elem["passport_series"]) + "\n" +
                         "age: " + str(elem["age"]) + "\n" + "occupation: " + elem["occupation"]
                         + "\n" + "political_views: " + elem["political_views"] + "\n" + "worldview: " + elem[
                             "worldview"] +
                         "\n" + "address: " + elem["address"] + "\n" + "............................................\n")
            number_of_valid_records += 1
        else:
            checkers[valid_values] += 1
        progressbar.update(1)
number_of_invalid_records = checkers[0] + checkers[1] + checkers[2] + checkers[3] + checkers[4] + checkers[5] + \
                            checkers[6] + checkers[
                                7] + checkers[8]
print("Общее число корректных записей:", number_of_valid_records, )
print("Общее число некорректных записей:", number_of_invalid_records)
print("Ошибки в email:", checkers[0])
print("Ошибки в height:", checkers[1])
print("Ошибки в inn:", checkers[2])
print("Ошибки в passport_series:", checkers[3])
print("Ошибки в age:", checkers[4])
print("Ошибки в occupation:", checkers[5])
print("Ошибки в address:", checkers[6])
print("Ошибки в political_views:", checkers[7])
print("Ошибки в worldview:", checkers[8])
output.close()