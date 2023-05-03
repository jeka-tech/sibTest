import sqlite3, config, os
import xls_works.xls_connect as xls

os.chdir(config.project_path)       # переходим в корневую директорию проекта

con = sqlite3.connect('DBase\mydatabase.db', sqlite3.PARSE_DECLTYPES)

cursor = con.cursor()

cursor.execute(f'CREATE TABLE if not exists xsl_table{tuple(xls.ttm_korn[0])}')

cursor.execute('SELECT name from sqlite_master where type= "table"')
print(cursor.fetchall())

def insert_date():
    for row in range(1, 4):
        cursor.execute(f'INSERT INTO xsl_table VALUES{tuple(xls.ttm_korn[row])}')
    con.commit()
    con.close()

if __name__ == '__main__':
    print('Start')
    insert_date()
    print('finish')



# Удаление таблицы с предварительной проверкой, существует ли она
# cursor.execute('DROP table if exists employees')

# Чтобы вставить данные в таблицу воспользуемся оператором INSERT INTO
# entities = ('Andrew', 777, 'IT', 'Tech', '2018-02-06')
# cursor.execute('INSERT INTO table4(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', values)

# Метод commit() сохраняет все сделанные изменения
