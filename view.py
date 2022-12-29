def input_number() -> int:
    while True:
        try:
            number = int(input('Введите целое число: '))
            return number
        except:
            print('Ошибка')

def imput_operation():
    while True:
        operation = input('Введите операцию: ')
        if operation in ['+', '-', '*', '/', '=']:
            return operation
        else:
            print('Введите корректную операцию!')

def print_to_console(value_text):
    print(value_text)

def log_off():
    print('До свидания!')

def print_division_by_zero():
    print('На ноль делить нельзя!')

def input_stringCalcExpression() -> str:
    while True:
        try:
            stringCalcExpression = input('Введите выражение для вычисления '
                                         '(из трёх элементов, между элементами выражения поставьте пробел): ')
            check_string = stringCalcExpression.split(' ')
            ex1 = check_string[0].isdigit()
            ex2 = check_string[2].isdigit()
            ex3 = check_string[1].isdigit()
            if (len(check_string) == 3) and (ex1 == True) and (ex2 == True) and (ex3 == False) \
                    and (check_string[1] == '+'):
                return stringCalcExpression
            elif (len(check_string) == 3) and (ex1 == True) and (ex2 == True) and (ex3 == False) \
                    and (check_string[1] == '-'):
                return stringCalcExpression
            elif (len(check_string) == 3) and (ex1 == True) and (ex2 == True) and (ex3 == False) \
                    and (check_string[1] == '*'):
                return stringCalcExpression
            elif (len(check_string) == 3) and (ex1 == True) and (ex2 == True) and (ex3 == False) \
                    and (check_string[1] == '/'):
                return stringCalcExpression
        except:
            print('Неправильный ввод. Введите заново.')