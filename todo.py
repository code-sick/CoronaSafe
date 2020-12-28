import sys
from datetime import datetime


def lineCount(filename):
    lines = 0
    for line in open(filename):
        lines += 1
    return lines


def findTodo(num):
    with open('todo.txt', "r") as f:
        for i in range(lineCount("todo.txt")):
            content = f.readline()
            if i == num - 1:
                todo = content
                return todo


def help():
    print("Usage :-")
    print('$ ./todo add "todo item"  # Add a new todo')
    print("$ ./todo ls               # Show remaining todos")
    print("$ ./todo del NUMBER       # Delete a todo")
    print("$ ./todo done NUMBER      # Complete a todo")
    print("$ ./todo help             # Show usage")
    print("$ ./todo report           # Statistics")


def addToFile(todo, fileName):
    with open(fileName, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(todo.rstrip('\r\n') + '\n' + content)
    print("Added todo: " + '''"''' + todo + '''"''')


def deleteInTodoFile(num):
    todoDelete = findTodo(num)
    with open("todo.txt", "r+") as f:
        content = f.readlines()
        f.seek(0)
        for i in content:
            if i != todoDelete:
                f.write(i)
        f.truncate()


def listTodo():
    with open("todo.txt", "r") as f:
        lines = lineCount("todo.txt")
        for i in range(lines):
            print("[" + str(lines - i) + "] " + f.readline(), end="")


def doneTodo(num):
    todoDone = findTodo(num)
    print(todoDone)
    deleteInTodoFile(num)
    todoDone = "x " + str(datetime.utcnow().date()) + " " + str(todoDone)
    addToFile(todoDone, "done.txt")


def report():
    todo = lineCount("todo.txt")
    done = lineCount("done.txt")
    print(str(datetime.utcnow().date()) +
          " Pending : " + str(todo) + " Completed : " + str(done))


if len(sys.argv) > 1:
    inpVar = sys.argv[1]
else:
    inpVar = "help"


if inpVar == "help":
    help()

if inpVar == "ls":
    listTodo()

if inpVar == "add":
    addToFile(sys.argv[2], "todo.txt")

if inpVar == "del":
    lines = lineCount("todo.txt")
    if lines < int(sys.argv[2]):
        print("Error: todo #" +
              str(sys.argv[2]) + " does not exist. Nothing deleted.")
    else:
        deleteInTodoFile(int(sys.argv[2]))

if inpVar == "done":
    lines = lineCount("done.txt")
    if lines < int(sys.argv[2]):
        print("Error: todo #" + str(sys.argv[2]) + " does not exist.")
    else:
        doneTodo(int(sys.argv[2]))

if inpVar == "report":
    report()
