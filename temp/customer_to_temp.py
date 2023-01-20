from connection import cs

def customer_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_CUSTOMER
                (
                CUSTOMER_KY NUMBER NOT NULL AUTOINCREMENT PRIMARY KEY,
                CUSTOMER_ID NUMBER NOT NULL,
                CUSTOMER_FST_NM VARCHAR(20),
                CUSTOMER_MID_NM VARCHAR(20),
                CUSTOMER_LST_NM VARCHAR(20),
                CUSTOMER_ADDR VARCHAR(20)
                );
                """
        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_CUSTOMER")
        
        query = """
                INSERT INTO TEMP.TEMP_CUSTOMER (CUSTOMER_ID, CUSTOMER_FST_NM, CUSTOMER_MID_NM, CUSTOMER_LST_NM, CUSTOMER_ADDR)
                SELECT STG.STG_CUSTOMER.customer_id, STG.STG_CUSTOMER.customer_first_name, STG.STG_CUSTOMER.customer_middle_name, STG.STG_CUSTOMER.customer_last_name, STG.STG_CUSTOMER.customer_address
                FROM STG.STG_CUSTOMER
                """

        cs.execute(query)