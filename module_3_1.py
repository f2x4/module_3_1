# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины
# этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает
# True, если строка находится в этом списке, False - если отсутствует.
# Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы
# по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search,
# реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное
# кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).


calls = 0

def string_info(string):
    # Счетчик вызова функции
    count_calls()
    length = len(string)
    low_case = string.lower()
    upper_case = string.upper()
    return length, low_case, upper_case


def is_contains(some_string, some_list):
    # Счетчик вызова функции
    count_calls()
    # Привести значения аргументов функции к одному регистру - нижнему
    some_string = some_string.lower()
    some_list = [i.lower() for i in some_list]
    if some_string in some_list:
        return True
    else:
        return False


def count_calls():
    """ Счетчик вызова функций """
    global calls
    calls += 1
    return

print(string_info("SomeString"))
print(string_info("AbrAcAdAbrA"))
print(is_contains('Upc', ['Abc', 'ups', 'a', 'd']))
print(is_contains('KREX', ['Krex', 'Pex', 'Fex']))
print(calls)