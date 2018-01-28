#cm
#com
##########
import cx_Oracle

con_cred = ''

sql_str = '''select t1.id, t1.data ,t2.id, t2.data
from t1,t2
where t1.id = t2.id'''

v_from = sql_str.find('from')
v_where = sql_str.find('where')

str_select = sql_str[7:v_from]
str_from = sql_str[v_from+5:v_where]
str_where = sql_str[v_where+6:]


for a in str_select.split(','):
    k,v = a.strip().split('.')
    print(k,v)


#d_t1 = dict(zip(  [str_from],[]   )   )

print("select %s from %s where %s" %(str_select, str_from, str_where))


connection = cx_Oracle.connect(con_cred)
cursor = connection.cursor()
cursor.execute(sql_str)
for a in cursor:
    print(a[0],a[1])
del cursor
connection.close()
