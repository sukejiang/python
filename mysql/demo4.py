import pymysql

data = {
    'id': '20120003',
    'name': 'huang',
    'age': 20
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root',
                     password='root', port=3306, db='huang')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
    table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except Exception as e:
    print('Failed', e)
    db.rollback()
db.close()
