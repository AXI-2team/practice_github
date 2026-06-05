import pymysql

HOST='127.0.0.1'
PORT=3306
USER='scott'
PASS='tiger'
DB='python_schema'
TNAME = 'jdbct'

conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, password=PASS, charset='utf8mb4')
cursor = conn.cursor()


def call_incre2(empno, rate):
    try:
        cursor.callproc('INCRE2', (empno, rate))

        print(f'호출성공 ({empno}번 사원이 {rate}% 인상 완료했습니다.)')



    except pymysql.Error as e:
        print(f'INCRE2 프로시저 호출 실패 : {e}')
    finally:
        cursor.close()
        conn.close()

call_incre2(7902, 20)
