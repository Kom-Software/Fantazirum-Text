import re
class MainInterpreter:
    def __init__(self):
        self.console = {}
        self.functions = {}

    def interpret(self, program):
        lines = program.split("\n")
        for line in lines:
            if re.fullmatch(r'ent .+? = .+?', line):
                parts = line.split(" ")
                try:
                    self.console[parts[1]] = int(parts[3])
                except:
                    print(
                    'Ошибка 101: Неверное значение числовой переменной. Значение должно быть целым и от -2 147 483 648 до 2 147 483 647.')

            elif re.fullmatch(r'frac .+? = .+?', line):
                parts = line.split(" ")
                try:
                    self.console[parts[1]] = float(parts[3])
                except:
                    print(
                    'Ошибка 102: Неправильное значение числовой переменной. Значение должно быть дробным и от -3.4028235E+38 до 3.4028235E+38.')

            elif re.fullmatch(r'bool .+? = .+?', line):
                parts = line.split(" ")
                try:
                    if parts[3] == "true":
                        self.console[parts[1]] = True
                    elif parts[3] == "false":
                        self.console[parts[1]] = False
                    else:
                        print(
                        'Ошибка 104: Неверное значение булевой переменной. Оно должно равняться "true" или "false".')
                except:
                    print(
                    "Ошибка 201: Неправильное построение. Имели вы в виду: тип название = значение?")

            elif re.fullmatch(r'lin .+? = ".+?"', line):
                parts = line.split(" ")
                lin_parts = line.split('"')
                try:
                    self.console[parts[1]] = lin_parts[1]
                except:
                    print(
                    "Ошибка 103: Неверное значение строчной переменной. Значение должно состоять из букв и цифр.")

            elif re.fullmatch(r'console.say ".+?"', line):
                console_lin_parts = line.split('"')
                print(console_lin_parts[1])

            elif line.startswith("console.say"):
                parts = line.split(" ")
                if parts[1] in self.console:
                    print(self.console[parts[1]])
                else:
                    print("Ошибка 100: Переменная без значения: " + parts[1])

interpreter = MainInterpreter()

program = ""

while True:
    try:
        sprogram = str(input())
        program = program + '\n' + sprogram
        if sprogram == "start":
            interpreter.interpret(program)

    except:
        exit()
