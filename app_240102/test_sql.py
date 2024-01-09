import pandas as pd
import pymysql
from sqlalchemy import create_engine
import os
from pathlib import Path

def call_query(query_string):

    # 데이터베이스 연결 설정
    conn =  {
                "host":"15.165.253.214",
                "port":3306,
                "user":"boosta_crawl",
                "passwd":"boosta_crawl11!!",
                "db":"boosters",
                "charset":"utf8"
            }

        
    # SQLAlchemy 엔진 생성
    engine = create_engine(f"mysql+pymysql://{conn['user']}:{conn['passwd']}@{conn['host']}:3306/{conn['db']}")


    # SQL 쿼리 실행
    query = query_string  # 'your_table_name'을 실제 테이블 이름으로 변경하세요.
    df = pd.read_sql(query, engine)

    print(df)
    # 데이터 확인
    return df





