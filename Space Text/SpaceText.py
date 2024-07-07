class MainInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, program):
        lines = program.split("\n")
        print(lines)
        for line in lines:

            if line.startswith("console.say"):
                parts = line.split(" ")
                if parts[1] in self.variables:
                    print(self.variables[parts[1]])
                elif parts[1].startswith('"') and parts[1].endswith('"'):
                    print(parts[1])
                else:
                    print("Ошибка 100: Переменная без значения: " + parts[1])

            elif line.startswith("console.get"):
                parts = line.split(" ")
                if len(parts) == 2:
                    print(f"{self.variables.get(parts[1])}")
                else:
                    print("Ошибка 200: Неправильное построение. Имели вы в виду: console.get название_переменной?")

            elif line.startswith("ent"):
                parts = line.split(" ")
                if len(parts) == 4:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        self.variables[parts[1]] = int(parts[3])
                    else:
                        print("Ошибка 300: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка 201: Неправильное построение. Имели вы в виду: тип название = значение?")

            elif line.startswith("frac"):
                parts = line.split(" ")
                if len(parts) == 4:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        self.variables[parts[1]] = float(parts[3])
                    else:
                        print("Ошибка 300: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка 201: Неправильное построение. Имели вы в виду: тип название = значение?")

            elif line.startswith("lin"):
                parts = line.split(" ")
                if len(parts) == 4:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        self.variables[parts[1]] = str(parts[3])
                    else:
                        print("Ошибка 300: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка 201: Неправильное построение. Имели вы в виду: тип название = значение?")

            elif line.startswith("bool"):
                parts = line.split(" ")
                if len(parts) == 4:                                                             # проверка на то, что, правильно ли пользователь указал построение? (тип название значение)
                    if parts[2] == "=":
                        if parts[3] == "true":
                            self.variables[parts[1]] = True
                        elif parts[3] == "false":
                            self.variables[parts[1]] = False
                        else:
                            print("Ошибка 101: Неверное значение булевой переменной. Оно должно равняться 'true' или 'false'.")
                    else:
                        print("Ошибка 300: Неверный знак присвоения или сравнения.")
                else:
                    print("Ошибка 201: Неправильное построение. Имели вы в виду: тип название = значение?")

            elif line.startswith("feauture"):
                parts = line.split(" ")
                if len(parts) == 2:
                    if parts[1].endswith(":"):
                        print(parts[1])

            elif line.startswith("start"):
                pass

            elif line.startswith(""):
                pass

            else:
                print("Ошибка 400: Неизвестная команда.")

interpreter = MainInterpreter()

program = ""

while True:
    sprogram = str(input())
    program = program + "\n" + sprogram
    if sprogram == "start":
        interpreter.interpret(program)
