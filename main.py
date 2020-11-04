import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=GML1GALTUNBULAK\SQLEXPRESS01;'
                      'Database=trial1;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
table = 'trial1.dbo.Persons'


def print_data():
    for row in cursor:
        print(row)


def show_data(x):
    """"
    :param x is the number of data asked, enter 0 if all to be shown
    :type
    :return a list
    """
    if x == 'all':
        cursor.execute('SELECT * FROM trial1.dbo.Persons')
    else:
        cursor.execute(f'SELECT TOP {x} * FROM trial1.dbo.Persons')

    for row in cursor:
        print(row)


def insert_data(*args):
    cursor.execute(f'SELECT * FROM {table}')

    cursor.execute(f'''
                    INSERT INTO {table} (Name, Age, City)
                    VALUES
                    {args}
                    ''')
    conn.commit()


def take_avg(col_name):
    """
    :param col_name: str: column name
    :return: float: average
    """

    cursor.execute(f"SELECT AVG({col_name}) AS average FROM dbo.Persons")

    result = cursor.fetchall()

    for i in result:
        average = float(i[0])

    return (average)


def take_sum(col_name):
    """
    :param col_name: str: column name
    :return: float: sum
    """

    cursor.execute(f"SELECT SUM({col_name}) AS sum FROM dbo.Persons")

    result = cursor.fetchall()

    for i in result:
        sum = float(i[0])

    return (sum)


def take_count(col_name, condition):
    """
    :param col_name: str: column name
    :param condition
    :return: float: sum
    """

    cursor.execute(f"SELECT COUNT({col_name}) AS count FROM dbo.Persons WHERE {condition}")

    result = cursor.fetchall()

    for i in result:
        count = float(i[0])

    return (count)


"""
cursor.execute('''
                UPDATE dbo.Persons
                SET City = 'Paris'
                WHERE Name = 'Emily'
                ''')
cursor.execute('SELECT * From dbo.Persons order by name, age')

print(take_avg('age'))
print(take_sum('age'))
print(take_count('city', "city='Paris'"))

cursor.execute('''
                UPDATE dbo.Persons
                SET City = 'Florence'
                WHERE City = 'Florance'
                ''')

cursor.execute('SELECT * From dbo.Persons order by name, age')
cursor.execute('''
                select count([Name ]), City
                from [dbo].[Persons]
                where [Name ]='Emily'
                group by City
                order by count([Name ]) 
                ''')

cursor.execute('''
                alter table dbo.persons
                add DogAge as Age/3.63
                ''')
conn.commit()

cursor.execute('SELECT * From dbo.Persons order by DogAge')"""



print_data()



