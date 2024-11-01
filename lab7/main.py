import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='mrxsss',
            password='12345678',
            database='main_database'
        )
        print("Підключено до MySQL бази даних")
    except Error as e:
        print(f"Помилка: '{e}'")

    return connection

def create_table(connection):
    cursor = connection.cursor()
    create_errors_table = """
    CREATE TABLE IF NOT EXISTS Errors (
        error_code INT AUTO_INCREMENT PRIMARY KEY,
        error_description TEXT NOT NULL,
        date_received DATE NOT NULL,
        error_level VARCHAR(20) NOT NULL,
        functionality_category VARCHAR(50),
        source VARCHAR(50)
    );
    """
    cursor.execute(create_errors_table)
    print("Таблиця Errors створена")

    create_programmers_table = """
    CREATE TABLE IF NOT EXISTS Programmers (
        programmer_code INT AUTO_INCREMENT PRIMARY KEY,
        last_name VARCHAR(50) NOT NULL,
        first_name VARCHAR(50) NOT NULL,
        phone VARCHAR(15)
    );
    """
    cursor.execute(create_programmers_table)
    print("Таблиця Programmers створена")

    create_fixes_table = """
    CREATE TABLE IF NOT EXISTS Fixes (
        fix_code INT AUTO_INCREMENT PRIMARY KEY,
        error_code INT,
        start_date DATE,
        fix_duration INT,
        programmer_code INT,
        daily_cost DECIMAL(10, 2),
        FOREIGN KEY (error_code) REFERENCES Errors (error_code),
        FOREIGN KEY (programmer_code) REFERENCES Programmers (programmer_code)
    );
    """
    cursor.execute(create_fixes_table)
    print("Таблиця Fixes створена")
    connection.commit()

def insert_data(connection):
    cursor = connection.cursor()

    errors_data = [
        ("NullPointerException", "2024-10-01", "Критична", "Інтерфейс", "Користувач"),
        ("IndexOutOfBoundsException", "2024-10-02", "Важлива", "Дані", "Тестувальник"),
        ("TypeError", "2024-10-03", "Помірна", "Логіка", "Програміст"),
        ("ValueError", "2024-10-04", "Критична", "Форма", "Користувач"),
        ("KeyError", "2024-10-05", "Важлива", "Дані", "Тестувальник"),
        ("AttributeError", "2024-10-06", "Критична", "Інтерфейс", "Користувач"),
        ("IOError", "2024-10-07", "Помірна", "Файл", "Системний адміністратор"),
        ("NameError", "2024-10-08", "Критична", "Логіка", "Програміст"),
        ("ImportError", "2024-10-09", "Важлива", "Імпорт", "Тестувальник"),
        ("RuntimeError", "2024-10-10", "Помірна", "Процес", "Користувач"),
        ("AssertionError", "2024-10-11", "Критична", "Тест", "Тестувальник"),
        ("IndexError", "2024-10-12", "Важлива", "Дані", "Програміст"),
        ("MemoryError", "2024-10-13", "Критична", "Пам'ять", "Системний адміністратор"),
        ("StopIteration", "2024-10-14", "Помірна", "Цикл", "Програміст"),
        ("KeyboardInterrupt", "2024-10-15", "Критична", "Користувач", "Користувач"),
        ("RecursionError", "2024-10-16", "Важлива", "Рекурсія", "Програміст"),
        ("IndentationError", "2024-10-17", "Помірна", "Код", "Тестувальник"),
        ("FloatingPointError", "2024-10-18", "Критична", "Обчислення", "Програміст"),
        ("UnboundLocalError", "2024-10-19", "Важлива", "Логіка", "Користувач"),
        ("OSError", "2024-10-20", "Помірна", "Система", "Системний адміністратор"),
        ("BufferError", "2024-10-21", "Критична", "Пам'ять", "Програміст"),
        ("ReferenceError", "2024-10-22", "Важлива", "Посилання", "Тестувальник"),
        ("ModuleNotFoundError", "2024-10-23", "Помірна", "Імпорт", "Програміст")
    ]
    
    for error in errors_data:
        cursor.execute("""
            INSERT INTO Errors (error_description, date_received, error_level, functionality_category, source)
            VALUES (%s, %s, %s, %s, %s)
        """, error)

    programmers_data = [
        ("Іванов", "Іван", "123456789"),
        ("Петров", "Петро", "987654321"),
        ("Сидоров", "Сидір", "543216789"),
        ("Шевченко", "Тарас", "321654987")
    ]

    for programmer in programmers_data:
        cursor.execute("""
            INSERT INTO Programmers (last_name, first_name, phone)
            VALUES (%s, %s, %s)
        """, programmer)

    connection.commit()
    print("Дані успішно вставлені")

def execute_queries(connection):
    cursor = connection.cursor()

    print("\nКритичні помилки:")
    cursor.execute("SELECT * FROM Errors WHERE error_level = 'Критична' ORDER BY error_code;")
    for row in cursor.fetchall():
        print(row)

    print("\nКількість помилок кожного рівня:")
    cursor.execute("SELECT error_level, COUNT(*) FROM Errors GROUP BY error_level;")
    for row in cursor.fetchall():
        print(row)

    print("\nВартість роботи програміста при виправленні помилки:")
    cursor.execute("""
        SELECT E.error_code, (F.fix_duration * F.daily_cost) AS total_cost
        FROM Fixes F
        JOIN Errors E ON F.error_code = E.error_code;
    """)
    for row in cursor.fetchall():
        print(row)

    source = 'Користувач'
    print(f"\nПомилки від джерела '{source}':")
    cursor.execute("SELECT * FROM Errors WHERE source = %s;", (source,))
    for row in cursor.fetchall():
        print(row)

    print("\nКількість помилок від користувачів та тестувальників:")
    cursor.execute("""
        SELECT source, COUNT(*) FROM Errors WHERE source IN ('Користувач', 'Тестувальник') GROUP BY source;
    """)
    for row in cursor.fetchall():
        print(row)

    print("\nКількість помилок за рівнем, виправлених кожним програмістом:")
    cursor.execute("""
        SELECT P.last_name, E.error_level, COUNT(F.error_code) AS count
        FROM Programmers P
        LEFT JOIN Fixes F ON P.programmer_code = F.programmer_code
        LEFT JOIN Errors E ON F.error_code = E.error_code
        GROUP BY P.last_name, E.error_level;
    """)
    for row in cursor.fetchall():
        print(row)

    cursor.close()

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        create_table(conn)
        insert_data(conn)
        execute_queries(conn)
        conn.close()
