# To-do list

class To_Do_List:
    def __init__(self):
        self.current_tasks = {} # будет сохраняться все в виде {title : комментарий (может быть пустым)}
        self.completed_tasks = {}
        self.relatives = {} # {title: id}
        self.id_counter = 0

    def add_task(self, title, comments = ''):

        self.current_tasks[title] = comments
        print("Задача успешно добавлена")

    def complete_task(self, title):
        if title in self.current_tasks:
            completed = self.current_tasks.pop(title)
            self.completed_tasks[title] = completed
            print("Задача выполнена!")

        else:
            print("Такой задачи не существует или она уже выполнена.")

    def print_current_tasks(self):
        if self.current_tasks:
            print(f'Текущие задачи (всего {len(self.current_tasks)})')
            for item in self.current_tasks:
                print(f'{item}: {self.current_tasks[item]}')

        else:
            print("Список задач пустой!")

    def print_completed_tasks(self):
        if self.completed_tasks:
            print(f'Выполненные задачи (всего {len(self.completed_tasks)})')
            for item in self.completed_tasks:
                print(f'{item}: {self.completed_tasks[item]}')

        else:
            print("Вы не выполнили ни одной задачи!!")


l = To_Do_List()


## добавить парсинг одинаковых команд и так далее
## можно сделать интерактивный вывод в консоли с помощью inquirer

command = ''
while command != "Выход":
    command = input().split(maxsplit=1)
    cmd = command.pop(0)
    rest = command[0].split("; ")
    title, comment = rest[0], '' if len(rest) == 1 else rest[1]

    match cmd:
        case "Добавить":
            l.add_task(title, comment)
        case "Выполнить":
            l.complete_task(command[1])
        case "Вывести_Текущие":
            l.print_current_tasks()
        case "Вывести_Выполоненные":
            l.print_completed_tasks()

