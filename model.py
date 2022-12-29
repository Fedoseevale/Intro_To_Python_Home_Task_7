first_number = 0
second_number = 0
operation = ''
result = 0
stringCalcExpression = ''
my_ListStringCalcExpression = []

def get_first():
    global first_number
    return first_number

def get_second():
    global second_number
    return second_number

def get_operation():
    global operation
    return operation

def get_result():
    global result
    return result

def set_first(value):
    global first_number
    first_number = value

def set_second(value):
    global second_number
    second_number = value

def set_operation(oper):
    global operation
    operation = oper

def addition():
    global first_number
    global second_number
    global result
    result = first_number + second_number

def difference():
    global first_number
    global second_number
    global result
    result = first_number - second_number

def multiplication():
    global first_number
    global second_number
    global result
    result = first_number * second_number

def division():
    global first_number
    global second_number
    global result
    result = first_number / second_number
    if result == int(result):
        result = int(result)

def get_stringCalcExpression():
    global stringCalcExpression
    return stringCalcExpression

def set_stringCalcExpression(my_stringCalcExpression):
    global stringCalcExpression
    stringCalcExpression = my_stringCalcExpression
    global my_ListStringCalcExpression
    my_ListStringCalcExpression = my_stringCalcExpression.split(' ')
    return my_ListStringCalcExpression

def stringCalculation():
    global my_ListStringCalcExpression
    first_part = int(my_ListStringCalcExpression[0])
    second_part = int(my_ListStringCalcExpression[2])
    symbol = my_ListStringCalcExpression[1]
    my_result = 0
    if symbol == '+':
        my_result = first_part + second_part
    elif symbol == '-':
        my_result = first_part - second_part
    elif symbol == '*':
        my_result = first_part * second_part
    else:
        my_result = first_part / second_part

    return print(f'{first_part} {symbol} {second_part} = {my_result}')
