import sqlite3 as sq

conn1 = sq.connect("C:\\Users\\70894\\Desktop\\recognize\\ObjectReco(35).db")
cursor1 = conn1.cursor()
cursor1.execute('select * from table1')
va1 = cursor1.fetchall()
cursor1.close()

conn1 = sq.connect("C:\\Users\\70894\\Desktop\\recognize\\400_v.db")
cursor1 = conn1.cursor()

'''for temp in va1:
    print(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12],temp[13],temp[14],temp[15],temp[16],temp[17],temp[18])'''

for temp in va1:
    conn1.execute("insert into table1 values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7],temp[8],temp[9],temp[10],temp[11],temp[12],temp[13],temp[14],temp[15],temp[16],temp[17],temp[18],0))
conn1.commit()
cursor1.close()