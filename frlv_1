

from numpy import *

A = zeros((2, 3))
A[1][2] = 7

# print(A)

B = [0] * 3
C = zeros( (len(B), len(B)) )
# print(C)


# import win32com.client
# Excel = win32com.client.Dispatch("Excel.Application")


# Import `os`
import os

# Retrieve current working directory (`cwd`)
from pandas import ExcelFile

cwd = os.getcwd()
cwd

# Change directory
# C:\Users\admin\PycharmProjects\pythonProject
os.chdir("/Users/admin/PycharmProjects/pythonProject")
# /path/to/your/folder


# List all files and directories in current directory
os.listdir('.')



# Для Windows
# python -m pip install -U pip setuptools
# импорт библиотеки pandas
import pandas as pd
# Загружаем ваш файл в переменную `file` / вместо 'example' укажите название свого файла из текущей директории
file = 'testPRG_vopr_db.xlsx'

# Загружаем spreadsheet в объект pandas
xl = pd.ExcelFile(file)

# Печатаем название листов в данном файле
# print(xl.sheet_names)
z = xl.sheet_names[0]

# Загрузить лист в DataFrame по его имени: df1
df1 = xl.parse(z)
# print(df1)


# df1.to_excel("example.xlsx", 'Sheet1')


# Установим `XlsxWriter`
# pip install XlsxWriter

# Указать writer библиотеки
df2 = pd.ExcelWriter('testPRG_vopr_db_new.xlsx')
#  df2 = df1
# Записать ваш DataFrame в файл
df1.to_excel(df2, 'Sheet1')

# Сохраним результат
# df2.save()
df1.to_excel("example.xlsx", 'Sheet1')



