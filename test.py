import cx_Oracle
from sys import modules

tns_names = cx_Oracle.makedsn('orcl11-aws.c0ivdp1t5vqz.us-east-1.rds.amazonaws.com',1521,'ORCL')
print(tns_names)

db = cx_Oracle.connect('admin','Admin14!',tns_names)

cursor = db.cursor()

cursor.execute('select * from dual')
print(cursor.fetchone())

create_table = """
CREATE TABLE python_modules (
module_name VARCHAR2(50) NOT NULL,
file_path VARCHAR2(300) NOT NULL
)
"""

cursor.execute(create_table)

M = []
for m_name, m_info in modules.items():
    try:
        M.append((m_name,m_info.__file__))
    except AttributeError:
        pass 


print(len(M))

cursor.prepare( "Insert into python_modules (module_name, file_path) values (:1,:2)"  )

cursor.executemany(None,M)

db.commit()



