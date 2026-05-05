# To-do list

class Task:
    def __init__(self, title, comment):
        self.title = title
        self.comment = comment
        self.done = False

    def change_title(self, new_title):
        if self.title != new_title:
            self.title = new_title

    def set_comment(self, comment): # даже если одинаковое описание, можно так делать
        self.comment = comment

    def print_task(self):
        print(self.title, end='')
        if self.comment:
            print(':', self.comment)

    def complete(self):
        self.done = True

    def get_title(self):
        print(self.title)

    def get_comment(self):
        print(self.comment)

    def get_description(self):
        print(f'{self.title}: {self.comment if self.comment else '(Нет описания)'}')

class To_Do_List:
    def __init__(self):
        self.current_tasks = {}
        self.completed_tasks = {}

    def add_task(self, title, comments = ''):
        if title in self.current_tasks:
            print("Такая задача уже существует!")
        else:
            new_task = Task(title, comment)
            self.current_tasks[title] = new_task
            print("Новая задача создана!")

    def complete_task(self, title):
        if title in self.current_tasks:
            completed_task = self.current_tasks.pop(title)
            self.completed_tasks[title] = completed_task
            print("Задача выполнена!")

        else:
            print("Такой задачи не существует или она уже выполнена.")

    def print_current_tasks(self):
        if self.current_tasks:
            print(f'Текущие задачи (всего {len(self.current_tasks)}):')
            for key in self.current_tasks:
                task = self.current_tasks[key]
                task.get_description()
        else:
            print("Список задач пустой!")

    def print_completed_tasks(self):
        if self.completed_tasks:
            print(f'Выполненные задачи (всего {len(self.completed_tasks)})')
            for key in self.completed_tasks:
                task = self.completed_tasks[key]
                task.get_description()
        else:
            print("Список выполненных задач пустой. Вам это ни о чем не говорит? 🙂")


l = To_Do_List()


## добавить парсинг одинаковых команд и так далее
## можно сделать интерактивный вывод в консоли с помощью inquirer

command = ''
while command != "Выход":
    command = input().split(maxsplit=1)
    cmd = command.pop(0)
    if command:
        rest = command[0].split(": ")
        title, comment = rest[0], '' if len(rest) == 1 else rest[1]

    match cmd:
        case "Добавить":
            l.add_task(title, comment)
        case "Выполнить":
            l.complete_task(title)
        case "Вывести_Текущие":
            l.print_current_tasks()
        case "Вывести_Выполоненные":
            l.print_completed_tasks()


