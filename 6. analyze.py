import pymysql
import pandas as pd
from  sqlalchemy import create_engine

HOST='127.0.0.1'
PORT=3306
USER='scott'
PASS='tiger'
DB='python_schema'
TNAME = 'jdbct'
sql = f'select * from {TNAME} order by no'

print('(1) 방법 1 : pymysql(cursor) 사용하여 df로 변환 - 가현 수정 텍스트 수정//////')

conn = pymysql.connect(host=HOST, port=PORT, database=DB, user=USER, password=PASS, charset='utf8mb4')
cursor = conn.cursor()

cursor.execute(sql)
rows = cursor.fetchall()
cols = [desc[0] for desc in cursor.description] # metadata
# print(columns)          # ['no', 'name', 'rdate']
# print(type(columns))    # list

df = pd.DataFrame(rows, columns=cols)
print(df)
print()
print(df.dtypes)
print()


print('(2) 방법 2 : sqlalchemy이용하여 df로 변환 ')
engine = create_engine(f'mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{DB}?charset=utf8mb4')
df2 = pd.read_sql(sql, engine)
print(df2.head())
print(type(df2))

print('(3) dataframe 분석 ')

df['이름길이'] = df['name'].apply(len)
df.head()

print('(3) df -> DB 저장')
result_df = df[['no', 'name', '이름길이']].copy()
result_df_cols = ['no', 'name', 'name_len']

result_df.to_sql(
    name='jdbct_result', # 테이블명
    con = engine,
    if_exists='replace',
    index = False
)
print('저장완료')

print('(4) 저장된 DB테이블에서 읽어오기')
db_result = pd.read_sql("select * from jdbct_result", engine)
db_result.head()

engine.dispose() # 엔진 연결해제

cursor.close()
conn.close()