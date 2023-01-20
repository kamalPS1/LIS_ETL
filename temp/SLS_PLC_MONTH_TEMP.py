from connection import cs
from datetime import datetime

def sls_plc_month_temp():
    cs.execute("USE DATABASE BHATBHATENI_DWH")

    current_time = datetime.now()

    create = """
            CREATE OR REPLACE TABLE TEMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TEMP
            (
                PDT_KY NUMBER NOT NULL REFERENCES "BHATBHATENI_DWH"."TEMP"."TEMP_PRODUCT"(PDT_KY),
                LOCN_KY NUMBER NOT NULL REFERENCES "BHATBHATENI_DWH"."TEMP"."TEMP_LOCN"(LOCN_KY),
                CTGRY_KY NUMBER NOT NULL REFERENCES "BHATBHATENI_DWH"."TEMP"."TEMP_CATEGORY"(CTGRY_KY),
                MONTH_KY NUMBER NOT NULL,
                TOTAL_QTY NUMBER,
                TOTAL_AMT NUMBER(10,2),
                TOTAL_DSCNT NUMBER(10,2)
            );
            """
    cs.execute(create)
    cs.execute("TRUNCATE TABLE TEMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TEMP")
    
    insert = f"""
            INSERT INTO TEMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TEMP
            (PDT_KY, LOCN_KY, CTGRY_KY, MONTH_KY, TOTAL_QTY, TOTAL_AMT, TOTAL_DSCNT)
                (SELECT p.PDT_KY, l.LOCN_KY, c.CTGRY_KY, MONTH(TRANSACTION_TIME) AS MONTH_KY, SUM(s.QTY) AS TOTAL_QTY, SUM(s.AMT) AS TOTAL_AMT, SUM(s.DSCNT) AS TOTAL_DSCNT
                FROM TEMP.TEMP_SALES s
                JOIN TEMP.TEMP_LOCN l
                    ON s.LOCN_KY = l.LOCN_KY
                JOIN TEMP.TEMP_PRODUCT p
                    ON s.PDT_KY = p.PDT_KY
                JOIN TEMP.TEMP_SUBCATEGORY sc
                    ON p.SUB_CTGRY_KY = sc.SUB_CTGRY_KY
                JOIN TEMP.TEMP_CATEGORY c
                    ON sc.CTGRY_KY = c.CTGRY_KY
                GROUP BY p.PDT_KY, l.LOCN_KY, c.CTGRY_KY, MONTH_KY
                ORDER BY MONTH_KY
                );
            """
    cs.execute(insert)