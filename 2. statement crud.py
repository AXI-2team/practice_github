import pymysql

HOST='127.0.0.1'
PORT=3306
USER='scott'
PASS='tiger'
DB='python_schema'
TNAME = 'jdbct'

conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, password=PASS, charset='utf8mb4')
cursor = conn.cursor()

def create_table():
    sql = f'''create table if not exists {TNAME}(
            no int primary key,
            name varchar(10),
            rdate datetime
        )'''
    
    cursor.execute(sql)

    print(f' {TNAME} Create 생성 완료 ')


def insert_table(no, name):
    sql = f'insert into {TNAME} values ({no}, "{name}", now())'
    result = cursor.execute(sql)
    conn.commit()

    if result > 0:
        print(f"{result}개의 row insert 성공")
    else :
        print('insert 실패')


def drop_table():
    sql = f"drop table if exists {TNAME}"
    cursor.execute(sql)
    print(f"{TNAME} drop 완료")
    
def select_all():
    sql = f"select * from {TNAME} order by no desc"
    cursor.execute(sql)

    rows = cursor.fetchall()
    print('번호\t이름\t날짜')
    print('-'*40)
    for row in rows:
        no, name, rdate = row
        print(f'{no}\t{name}\t{rdate}')
    print('-'*40)
    print(f"총 {len(rows)}개의 row가 검색됨.")

    conn.close()

def update_row(no, name):
    sql = f"update {TNAME} set name=%s where no=%s"
    result = cursor.execute(sql, (name, no))
    conn.commit()

    if result > 0 : 
        print("수정 성공")
    else: 
        print('수정 실패')

def delete_row(no):
    sql = f"delete from {TNAME} where no = %s"
    result = cursor.execute(sql, (no, ))
    conn.commit()

    if result > 0:
        print("삭제 성공")
    else :
        print("삭제 실패")

SQL_INSERT = f'inert into {TNAME} values (%s, %s, now())'



# create_table()
# insert_table(1, '이순신')
# insert_table(2, '홍길동')
# insert_table(3, '유관순')
# drop_table()

# update_row(3, '강감찬')
select_all()

cursor.close()
conn.close()