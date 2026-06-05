import pymysql

HOST='127.0.0.1'
PORT=3306
USER='scott'
PASS='tiger'
DB='python_schema'
TNAME = 'jdbct'

conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, password=PASS, charset='utf8mb4')
cursor = conn.cursor()
SQL_INSERT = f'insert into {TNAME} values (%s, %s, now())'
SQL_SEL_LIKE = f'select * from {TNAME} where name like %s'

def insert_row(no, name):
    cursor.execute(SQL_INSERT, (no, name))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f'{cursor.rowcount}개의 row 입력 성공')
    else:
        print("입력 실패")

def search(name):
    cursor.execute(SQL_SEL_LIKE, (f'%{name}%', ))

    rows = cursor.fetchall()

    select_all(rows)

  
def select_all(rows):

    print('번호\t이름\t날짜')
    print('-'*40)
    for row in rows:
        no, name, rdate = row
        print(f'{no}\t{name}\t{rdate}')
    print('-'*40)
    print(f"총 {len(rows)}개의 row가 검색됨.")

# insert_row(6, '홍길순')
# insert_row(7, '홍길자')
search('홍')

cursor.close()
conn.close()