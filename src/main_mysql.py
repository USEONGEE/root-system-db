import pandas as pd
from sqlalchemy import create_engine

FILE_PATH = "/Users/mousebook/Downloads/GY KPI 관련 테이블.xlsx"
DATABASE_NAME = "root_system"
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
    # 데이터베이스 연결 URL 생성
    # mysql+mysqlconnector://{user}:{password}@{host}/{dbname}
    engine = create_engine(
        f"mysql+mysqlconnector://root:12345@localhost/{DATABASE_NAME}"
    )

    # 데이터프레임을 MySQL에 삽입
    # 이 예제에서는 'B_Employee'라는 이름의 테이블에 데이터를 삽입하고 있습니다.
    # 이 테이블이 이미 데이터베이스에 존재하고, 구조가 데이터프레임과 일치한다고 가정합니다.
    df.to_sql(sheet_name, engine, if_exists="append", index=False)

    print("Data inserted successfully")


for sheet_name in tables:
    run(sheet_name)
