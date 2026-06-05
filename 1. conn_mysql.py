import pymysql

HOST='127.0.0.1'
PORT=3306
USER='scott'
PASS='tiger'
DB='python_schema'

try:

    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, password=PASS, charset='utf8mb4')
    print(f"myriadb 연결 성공! {conn}")
    conn.close()
    print(f"연결종료 성공")

except pymysql.Error as e:
    print(f"에러발생 : {e}")