class View:

    def view_data(data, title):
        print(f'{title}: {data}')

    def get_value(self):
        return int(input('Введите число: '))

    def get_operator(self):
        return str(input('Введите оператор: '))