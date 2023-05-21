import pandas as pd

file_path = "test_excel.xlsx"
sheet = 'data'


def get_all():
    df = pd.read_excel(file_path)
    return df.head()

def fun2():
    # Прочитать второй лист файла Excel в объект Pandas DataFrame, пропустив первую строку
    df = pd.read_excel('example.xlsx', sheet_name='Sheet2', header=1)

    # Переименовать столбцы DataFrame
    df.columns = ['Column1', 'Column2', 'Column3']

    # Вывести первые пять строк DataFrame
    print(df.head())


def fun1():
    # Прочитать второй лист файла Excel в объект Pandas DataFrame, пропустив первую строку
    df = pd.read_excel(file_path, sheet_name='data', header=1)

    # Переименовать столбцы DataFrame
    df.columns = ['first_name', 'last_name']

    # Вывести первые пять строк DataFrame
    print(df.head())


def fun3():
    # Прочитать только определенные столбцы из файла Excel в DataFrame
    df = pd.read_excel(file_path, usecols=["first_name","last_name"])

    # Вывести первые 5 строк DataFrame
    print(df.head())

def fun4():
    # Прочитать только первые 100 строк файла Excel в DataFrame
    df = pd.read_excel('file.xlsx', nrows=100)

    # Вывести первые 5 строк DataFrame
    print(df.head())
