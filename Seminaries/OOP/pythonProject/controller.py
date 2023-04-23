from calc_model import CalcModel
from view import View

class Controller:

    def start_calc():
        value_a = View.get_value()
        operator = View.get_operator()
        value_b = View.get_value()
        calc = CalcModel()
        result = None
        if operator == '+':
            result = calc.sum(value_a, value_b)
        elif operator == '-':
            result = calc.sub(value_a, value_b)
        elif operator == '/':
            result = calc.div(value_a, value_b)
        elif operator == '*':
            result = calc.mult(value_a, value_b)
        else:
            print('Неверный оператор')
        View.view_data(result, "Ответ")