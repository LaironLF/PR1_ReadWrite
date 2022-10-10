from io import TextIOWrapper
from os import system
system('cls')
### ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ###


### ЗАПИСЬ ###
def writeFile():
    with open('dataBase.txt', 'a', encoding='utf-8') as db:
        while True:
            print("Введите через пробел данные: фамилия, имя, отчество, год рождения", "Для выхода напишите - exit", end="\n")
            n = input()
            if(n == 'exit'):
                system('cls') 
                break
            
            try: writeFileProccess(db, n)
            except Exception as e:
                system('cls') 
                print(e)

def writeFileProccess(db : TextIOWrapper, n : str):
    a = [i for i in n.split()]
    if len(a) != 4: raise Exception("Введите 4 элемента: Фамилия, Имя, Отчество, Год рождения")
    try: int(a[len(a)-1])
    except: raise Exception("Год должен состоять из чисел")
    else:
        for line in a:
            db.write(line)
            db.write(" ")
        db.write("\n")
        raise Exception("☆ ☆ ☆ Данные успешно записаны! ☆ ☆ ☆")
    

    
### ЧТЕНИЕ ###
def readFile():
    while True:
        print("Фамилия", "Имя", "\tОтчество", "Год рождения", sep=" \t ")
        with open('dataBase.txt', 'r', encoding='utf-8') as db:
            n=db.readline()
            while n != '':
                a=[i for i in n.split()]
                for i in range(4):
                    print(a[i], end=" \t ")
                print()
                n=db.readline()
        print("exit - выход")
        n = input()
        if(n == 'exit'): 
            system('cls')
            break

def readFilePretty():
    pass                

while True:
    print("--| Чтение и запись в файл |--\n1 - Записать в файл данные\n2 - Прочитать данные в файле\nexit - выход")
    n :int
    try:
        n = input()
        system('cls')
        if(n == 'exit'): break
        if(n == '1'):
            writeFile()
        elif(n == '2'):
            readFile()
        else: raise Exception("Введите вариант из списка предложенных!")
    except Exception as e:
        system('cls')
        print(e)