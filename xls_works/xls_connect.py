import os, config
from openpyxl import load_workbook
data = []

os.chdir(config.project_path)       # переходим в корневую директорию проекта

workbook = load_workbook('.\\xls_works\\testPRG_vopr_db.xlsx')
worksheet = workbook['db_vopr']



for row in worksheet.rows:                              # перебираем строки в файле
    row_cells = []                                      # заведем переменную для списка ячеек в строке

    if row[1].value:                                    # если ячейка с вопросом не пустая (второй столбец имеет индекс 1), то...
        for cell in row:                                # перебираем все ячейки в этой строке
            row_cells.append(cell.value)                # и добавляем в список значения ячеек в этой строке
        for cell in row:                                # повторно перебираем все ячейки в этой строке
            if cell.fill.fgColor.rgb != '00000000':     # чтобы проверить, какая ячейка (ячейки) имеют заливку, отличную от белой (заливкой выделен правильный ответ)
                row_cells.append(cell.column - 2)       # добавляем номер правильного варианта ответа в конец списка
        data.append(row_cells)                          # и добавляем полученный список в основной массив данных

if __name__ == '__main__':
    print(data)
