import pymysql
#获取数据库
db = pymysql.connect(host='localhost', user='root', password='root', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE huang DEFAULT CHARACTER SET utf8mb4")
db.close()
