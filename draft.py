import cx_Oracle

connection_string = 'eldar/eldar@192.168.1.12/orcl'
user = 'eldar'
pas = 'eldar'
tns = cx_Oracle.makedsn('192.168.1.12','1521','orcl')
#print(tns)

sql_str = '''select  t1.data , t2.data
from t1,t2
where t1.id = t2.id'''

v_from = sql_str.find('from')
v_where = sql_str.find('where')

str_select = sql_str[7:v_from]
str_from = sql_str[v_from+5:v_where]
str_where = sql_str[v_where+6:]


mapping_dict = {}

for tables in str_from.strip().split(','):
    mapping_dict.setdefault(tables,[])

for columns in str_select.split(','):
    k,v = columns.strip().split('.')
    #d.setdefault(k,[v
    mapping_dict[k].append(v)

for wheres in str_where.split('='):
    k,v = wheres.strip().split('.')
    mapping_dict[k].append(v)

print(mapping_dict)
#mapping_dict = dict(zip(  [str_from],[]   )   )

## need to be done:
## modify sql_string by concatinating additional columns to select clause
#new_sql =
#then pass it ot oracle cursor
print("select %s form %s where %s " % (str_select,str_from,str_where) )
##

connection = cx_Oracle.connect(connection_string)
#connection = cx_Oracle.connect(user,pas,tns)
cursor = connection.cursor()
#print(connection.version)
cursor.execute(sql_str)
for a in cursor:
    print(a[0],a[1])

header = [i[0] for i in cursor.description]
print(header)

cursor.close()
connection.close()
