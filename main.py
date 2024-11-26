import sqlite3

# 連接資料庫並建立表格
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
''')
conn.commit()

# 定義 CRUD 功能
def create_employee(name, age):
    cursor.execute('INSERT INTO employees (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print(f'已新增職員：{name}, 年齡：{age}')

def read_employees():
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    print("目前職員清單：")
    for emp in employees:
        print(emp)

def update_employee(emp_id, new_age):
    cursor.execute('UPDATE employees SET age = ? WHERE id = ?', (new_age, emp_id))
    conn.commit()
    print(f'已更新職員編號 {emp_id} 的年齡為：{new_age}')

def delete_employee(emp_id):
    cursor.execute('DELETE FROM employees WHERE id = ?', (emp_id,))
    conn.commit()
    print(f'已刪除職員編號 {emp_id}')

# 互動式指令操作
while True:
    action = input("請輸入動作 (c:新增, r:查看, u:更新, d:刪除, q:退出): ").strip().lower()

    if action == 'c':
        name = input("請輸入職員名稱: ")
        age = int(input("請輸入職員年齡: "))
        create_employee(name, age)

    elif action == 'r':
        read_employees()

    elif action == 'u':
        emp_id = int(input("請輸入要更新的職員編號: "))
        new_age = int(input("請輸入新的年齡: "))
        update_employee(emp_id, new_age)

    elif action == 'd':
        emp_id = int(input("請輸入要刪除的職員編號: "))
        delete_employee(emp_id)

    elif action == 'q':
        print("退出系統")
        break

    else:
        print("無效的指令，請重新輸入。")

# 關閉資料庫連接
conn.close()
