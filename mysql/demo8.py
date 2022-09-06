import pymysql

data = {
    'id':'20220810',
    'name':'WEI',
    'age':18
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s']*len(data))

db = pymysql.connect(host='localhost',user='root',
                     password='root',port=3306,database='huang')
cursor = db.cursor()
sql = 'insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql,tuple(data.values())):
        db.commit()
        print('sucessful')
except Exception as e:
        db.rollback()
        print("failed",e)
db.close