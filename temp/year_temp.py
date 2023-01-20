from connection import cs
from datetime import datetime

def year_temp():
    cs.execute("USE DATABASE BHATBHATENI_DWH")

    current_time = datetime.now()

    create = """
            CREATE OR REPLACE TABLE TEMP.D_BHATBHATENI_TIME_YEAR_TEMP
            (
            ID NUMBER,
            YEAR_KY NUMBER NOT NULL PRIMARY KEY,
            YEAR_START_DATE DATE NOT NULL,
            YEAR_END_DATE DATE NOT NULL,
            OPEN_CLOSE_CD VARCHAR(1),
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ
            );
            """
    cs.execute(create)
    cs.execute("TRUNCATE TABLE TEMP.D_BHATBHATENI_TIME_YEAR_TEMP")
    
    query = f"""
        INSERT INTO TEMP.D_BHATBHATENI_TIME_YEAR_TEMP 
        (ID, YEAR_KY, YEAR_START_DATE, YEAR_END_DATE, OPEN_CLOSE_CD, ROW_INSRT_TMS, ROW_UPDT_TMS)
            (SELECT EXTRACT(YEAR FROM s.TRANSACTION_TIME), 
                    CASE
                        WHEN EXTRACT(YEAR FROM s.TRANSACTION_TIME) = 2020 THEN 0
                        WHEN EXTRACT(YEAR FROM s.TRANSACTION_TIME) = 2021 THEN 1
                        ELSE EXTRACT(YEAR FROM s.TRANSACTION_TIME) %  10
                    END AS YEAR_KY,
                    CONCAT(YEAR(s.TRANSACTION_TIME),'-01-01'),
                    CONCAT(YEAR(s.TRANSACTION_TIME),'-12-31'),
                    'O',
                    '{current_time}',
                    '{current_time}'
        FROM "BHATBHATENI_DWH"."TEMP".TEMP_SALES s
        ORDER BY YEAR_KY);
            """

    cs.execute(query)

year_temp()