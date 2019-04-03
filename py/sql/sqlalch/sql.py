import sqlite3

conn = sqlite3.Connection("testdb")
# conn.execute("CREATE TABLE abc(name varchar)")
res = conn.execute("SELECT COUNT(*) FROM abc")
for row in res:
  print(row)
# conn.commit()
conn.close()

content = ""
info = content.split(",")
hostname = info[0]
locators = info[5].split(" ")