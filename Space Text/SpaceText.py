class MainInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, program):
        lines = program.split("\n")

        for line in lines:

            if line.startswith("console.say"):
                parts = line.split(" ")
                if parts[1] in self.variables:
                    print(self.variables[parts[1]])
                else:
                    print("Ошибка: Переменная без значения: " + parts[1])

            elif line.startswith("ent"):
                parts = line.split(" ")
                if len(parts) == 4:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        self.variables[parts[1]] = int(parts[3])
                    else:
                        print("Ошибка: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка: Неправильное построение. Имели вы в виду: тип название значение?")

            elif line.startswith("frac"):
                parts = line.split(" ")
                if len(parts) == 3:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        self.variables[parts[1]] = float(parts[3])
                    else:
                        print("Ошибка: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка: Неправильное построение. Имели вы в виду: тип название значение?")

            elif line.startswith("lin"):
                parts = line.split(" ")
                if len(parts) == 3:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        self.variables[parts[1]] = str(parts[3])
                    else:
                        print("Ошибка: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка: Неправильное построение. Имели вы в виду: тип название значение?")

            elif line.startswith("bool"):
                parts = line.split(" ")
                if len(parts) == 3:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        self.variables[parts[1]] = bool(parts[3])
                    else:
                        print("Ошибка: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка: Неправильное построение. Имели вы в виду: тип название значение?")

            else:
                print("Ошибка: Недопустимая команда или начало/конец кода")

# Пример использования
interpreter = MainInterpreter()

program = \
"""
ent я_мажу_жопу_вазелином = 15
console.say я_мажу_жопу_вазелином
"""
interpreter.interpret(program)

