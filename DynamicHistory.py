import sqlite3

conn=sqlite3.connect(r"C:\Users\yy\AppData\Local\Google\Chrome\User Data\Default\History")
cursor=conn.cursor()

search_value="github"       #Search Value

id=0
id_lst=[]

for row in cursor.execute("select id,url  from  urls where url like '%"+search_value+"%'"):
    print(row)
    id=row[0]
    id_lst.append((id,))

cursor.executemany('Delete from urls where id=?',id_lst)
conn.commit()

conn.close()

