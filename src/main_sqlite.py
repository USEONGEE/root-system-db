import pandas as pd
from sqlalchemy import create_engine

FILE_PATH = "/Users/mousebook/Downloads/GY KPI 관련 테이블.xlsx"
DATABASE_FILE = "root_system.db"  # SQLite 파일 이름
##
# B_WorkTime
# C_CommonCode
# B_Item
# B_Machine
# B_CycleTime
# B_DownTime
# P_Production_Result
# P_Production_Result_Bad
# P_Production_Result_Emp
# B_Employee
##
tables = [
    "B_WorkTime",
    "C_CommonCode",
    "B_Item",
    "B_Machine",
    "B_CycleTime",
    "B_DownTime",
    "P_Production_Result",
    "P_Production_Result_Bad",
    "P_Production_Result_Emp",
    "B_Employee",
]


def run(sheet_name):
    # Pandas를 사용하여 지정된 시트 읽기
    df = pd.read_excel(FILE_PATH, sheet_name=sheet_name)
    # SQLite 데이터베이스 파일 경로 생성
    db_url = f"sqlite:///{DATABASE_FILE}"

    # SQLite 엔진 생성
    engine = create_engine(db_url)

    # 데이터프레임을 SQLite에 삽입
    df.to_sql(sheet_name, engine, if_exists="append", index=False)

    print("Data inserted successfully")


for sheet_name in tables:
    run(sheet_name)
