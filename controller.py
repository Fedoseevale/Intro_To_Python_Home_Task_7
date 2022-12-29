import view
import model


def input_first():
    number = view.input_number()
    model.set_first(number)

def input_second():
    while True:
        number = view.input_number()
        if model.get_operation() == '/' and number == 0:
            view.print_division_by_zero()
        else:
            model.set_second(number)
            break

def imput_operation():
    oper = view.imput_operation()
    model.set_operation(oper)

def solution():
    oper = model.get_operation()
    if oper == '+':
        model.addition()
    elif oper == '-':
        model.difference()
    elif oper == '*':
        model.multiplication()
    elif oper == '/':
        model.division()

    result_string = f'{model.get_first()} {model.get_operation()} {model.get_second()} = {model.get_result()}'
    view.print_to_console(result_string)
    model.set_first(model.get_result())

def input_raw_stringCalcExpression():
    string = view.input_stringCalcExpression()
    model.set_stringCalcExpression(string)

def start():
    type_calc = int(input('Выберете тип калькулятора (1 - кнопочный, 2 - строчный):'))
    print(type_calc)
    if type_calc == 1:
        input_first()
        while True:
            imput_operation()
            if model.get_operation() == '=':
                view.log_off()
                break
            input_second()
            solution()
    else:
        print('Калькулятор строчный')
        input_raw_stringCalcExpression()

        model.stringCalculation()
        view.log_off()
