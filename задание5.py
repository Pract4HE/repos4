def задание1():
    n = int(input('Введите число чисел в последовательности: '))
    s = 0

    for i in range(n):
        i = int(input('Введите число: '))
        if (i>0) and i%2 == 0:
        
            s = s+i #суммирование
     
    print("сумма=", s)

def задание2():
    import random                  
    def sdvig(massive,k):              #функция для сдвига элементов строки
        for i in range(0,k):               #повтор сдвига на одну позиции k раз
            massive.insert(0,massive.pop())     #перестановка последнего элемента в начало списка
    print('Ввести количество строк матрицы')
    m=int(input())
    print('Ввести количество столбцов в матрице')
    n=int(input())
    print('Ввести шаг сдвига')
    k=int(input())                         
    massive=[]                   

    for i in range(0,m):             #проходимся по строкам
        massive.append([])           
        for j in range(0,n):         #проходимся по элементам строки
            massive[i].append(int(random.random() * 100))       
    print(massive)                  

    for l in range(0,m):            #проходимся по строкам массива
        if l%2==0:                  #если строка четная
            sdvig(massive[l],k)     #вызываем функцию сдвига
    print(massive)                  #печатаем получившийся

def задание3():
    a=[]
    n=int(input("Введите число чисел в массиве:"))
    for i in range(n):
        a.append(int(input("Введите элемент массива: ")))
    print(a)

    mn = min(a)
    mx = max(a)
    imn = a.index(mn)
    imx = a.index(mx)
    a[imn],a[imx] = a[imx],a[imn]
    for i in range(n):
        print(a[i], end=' ')

def задание4():
    import sqlite3

    # Указываем название файла базы данных
    conn = sqlite3.connect('mydatabase.sqlite')
    cursor = conn.cursor()

    # Создаем таблицу blog с шестью полями - id , name , kurs , group , dolg , items
    try:
        cursor.execute(
            '''CREATE TABLE blog (id integer, name text, kurs integer, group integer, dolg integer, items text)''')
    except:
        pass

    # Вставляем в таблицу blog первую запись со значениями id , name , kurs , group , dolg , items
    cursor.execute(
        "INSERT INTO blog (id , name , kurs , group , dolg , items) VALUES (' ID', 'ФИО', 'курс', 'группа', 'количество задолженностей', 'предметы')")
    conn.commit()

    # Вставляем в таблицу blog вторую запись со значениями id , name , kurs , group , dolg , items
    cursor.execute(
        "INSERT INTO blog (id , name , kurs , group , dolg , items) VALUES (' ID', 'ФИО', 'курс', 'группа', 'количество задолженностей', 'предметы')")
    conn.commit()

    # Делаем выборку всех имеющихся в таблице записей и в цикле печатаем их значения
    cursor.execute('SELECT * FROM blog')
    row = cursor.fetchone()
    while row is not None:
        print(row[0])
        print(row[1] + '\n')
        row = cursor.fetchone()

    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()
задание1()
задание2()
задание3()
задание4()
