# import pyodbc
# cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER=D32DB01;DATABASE=Circlone")
# cursor = cnxn.cursor()
#
#
# --cursor.execute("insert into test_tb values(6, 'name')")
#
# cursor.execute("select Userid, Amount from listings")
# rows = cursor.fetchall()
# for row in rows:
#     print row.Userid, row.Amount

#cd "/usr/local/lib/python2.7/"

with pymssql
connection=pymssql.connect(user='p2pcredit\  pjha',password='Prashant1~',
   host='110.121.147.57',database='circleone',as_dict=True)
cursor=connection.cursor()
cursor.execute('select top 10 Userid, Amount from listings ;')
rows=cursor.fetchall()
for row in rows:
  print(row)


