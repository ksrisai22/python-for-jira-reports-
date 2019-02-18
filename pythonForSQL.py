
import pyodbc 
conn = pyodbc.connect(driver='{SQL Server}',host='MD1PRDVMSSQL02', database='JIRA727',
                       user='jirauser_read', password='jira123$56',trusted_connection='yes')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.jiraissue')

for row in cursor:
    print(row)
'''
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server= MD1PRDVMSSQL02;'
                      'Database=JIRA727;'
                      'username = jirauser_read;'
                      'password = jira123$56;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.jiradb')

for row in cursor:
    print(row)

'''
