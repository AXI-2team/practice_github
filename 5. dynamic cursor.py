import pymysql
import time

HOST='127.0.0.1'
PORT=3306
USER='scott'
PASS='tiger'
DB='python_schema'
TNAME = 'jdbct'

conn = pymysql.connect(host=HOST, port=PORT, database=DB, user=USER, password=PASS, charset='utf8mb4')
cursor = conn.cursor()

sql = f'select * from {TNAME} order by no desc'
cursor.execute(sql)

rows = cursor.fetchall()

# fetchall 사용
print('(1) 순방향 출력')
print('-'*40)
for row in rows:
    print(f'{row[0]}\t{row[1]}\t{row[2]}')

print('\n(2) 역방향 출력')
print('-'*40)
for row in reversed(rows):
    print(f'{row[0]}\t{row[1]}\t{row[2]}')

# fetchone 사용
print('\n(3) 한 행씩 출력')
cursor.execute(sql) # 커서 초기화 진행
print('-'*40)
while True:
    row = cursor.fetchone()
    if row is None: break
    print(f'{row[0]}\t{row[1]}\t{row[2]}')

# fetchmany() 사용
print('\n(4) 특정 갯수만큼 씩 출력')
cursor.execute(sql)
print('-'*40)

while True:
    rows = cursor.fetchmany(3)
    if not rows:
        print(not rows) # rows가 []인가. 비어있는가             >> 주로 fetchmany(), fetchall()에서 사용
        print(rows is None) # rows가 null값인가. 상자조차 없는가. >> 주로 fetchone()에서 사용
        break  

    for row in rows:
        print(f'{row[0]}\t{row[1]}\t{row[2]}')

    print('-'*40)
    time.sleep(1)


    # input('다음 페이지를 보려면 enter!')


cursor.close()
conn.close()

