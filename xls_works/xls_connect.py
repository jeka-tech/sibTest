

import os, config, pandas as pd
from openpyxl import load_workbook
data = []

os.chdir(config.project_path)       # переходим в корневую директорию проекта

workbook = load_workbook('.\\xls_works\\testPRG_vopr_db.xlsx')
worksheet = workbook['db_vopr']



cwd = os.getcwd()
cwd

# mart (x, y) = 0

for row in worksheet.rows:                              # перебираем строки в файле
    row_cells = []                                      # заведем переменную для списка ячеек в строке
    res_ans = []                                        # заведем переменную для списка верных ответов в строке
    if row[1].value:                                    # если ячейка с вопросом не пустая (второй столбец имеет индекс 1), то...
        for cell in row:                                # перебираем все ячейки в этой строке
            row_cells.append(cell.value)                # и добавляем в список значения ячеек в этой строке
        for cell in row:                                # повторно перебираем все ячейки в этой строке
            if cell.fill.fgColor.rgb != '00000000':     # чтобы проверить, какая ячейка (ячейки) имеют заливку, отличную от белой (заливкой выделен правильный ответ)
               res_ans.append(cell.column - 2)          # и добавляем во вложенный список для фиксации ячеек с правильным ответом
        row_cells.insert(2, res_ans)                    # добавляем список правильного(ых) варианта(ов) ответа(ов) в начало списка вопросов
    print(row_cells)
    data.append(row_cells)                              # и добавляем полученный список в основной массив данных



# df2 = []
# Указать writer библиотеки
# df2 = pd.ExcelWriter('testPRG_vopr_db_new.xlsx')
# data.to_excel(df2, 'Sheet1')
# Сохраним результат
# df2.save()
# data.to_excel("example.xlsx", 'Sheet1')

if __name__ == '__main__':
   print(data)
#   pass