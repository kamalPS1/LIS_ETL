from connection import cs

def sales_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_SALES
                (
                SLS_ID NUMBER PRIMARY KEY,
                LOCN_KY NUMBER REFERENCES "BHATBHATENI_DWH"."TEMP".TEMP_LOCN(LOCN_KY),
                PDT_KY NUMBER REFERENCES "BHATBHATENI_DWH"."TEMP".TEMP_PRODUCT(PDT_KY),
                CUSTOMER_KY NUMBER REFERENCES "BHATBHATENI_DWH"."TEMP".TEMP_CUSTOMER(CUSTOMER_KY),
                TRANSACTION_TIME TIMESTAMP_NTZ,
                QTY NUMBER,
                AMT NUMBER(10,2),
                DSCNT NUMBER(10,2)
                );
                """
        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_SALES")
        
        query = """
                INSERT INTO TEMP.TEMP_SALES(SLS_ID, LOCN_KY, PDT_KY, CUSTOMER_KY, TRANSACTION_TIME, QTY, AMT, DSCNT)
                SELECT s.SALES_ID, l.LOCN_KY, p.PDT_KY, c.CUSTOMER_KY,
                s.TRANSACTION_TIME, s.QUANTITY, s.AMOUNT, s.DISCOUNT
                FROM STG.STG_SALES s
                INNER JOIN TEMP.TEMP_LOCN l 
                ON s.store_id = l.locn_id
                INNER JOIN TEMP.TEMP_PRODUCT p
                ON s.product_id = p.PDT_ID
                INNER JOIN TEMP.TEMP_CUSTOMER c
                ON s.CUSTOMER_ID = c.CUSTOMER_ID
                """

        cs.execute(query)