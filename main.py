import pyodbc
import pandas as pd
import xlsxwriter

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=GML1GALTUNBULAK\SQLEXPRESS01;'
                      'Database=trial1;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

SQL_Query = pd.read_sql_query(
    '''SELECT name, age, city, dogAge FROM trial1.dbo.Persons''', conn)

df1 = pd.DataFrame(SQL_Query, columns=['name', 'age'])
df1.insert(loc=0, column='row_num', value=df1.reset_index().index)

SQL_Query2 = pd.read_sql_query(
    '''SELECT name, horseAge, elephantAge, duckAge FROM trial1.dbo.AnimalAge''', conn)

df2 = pd.DataFrame(SQL_Query2, columns=['horseAge', 'elephantAge', 'duckAge'])
df2.insert(loc=0, column='row_num', value=df2.reset_index().index)

result = pd.merge(df1,df2,how='left',on='row_num')

writer = pd.ExcelWriter(r'C:\Users\interngaltunbulak\Desktop\result.xlsx',engine= 'xlsxwriter')
result.to_excel(writer, sheet_name='tab_name')

writer.save()



