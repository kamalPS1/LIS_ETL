from connection import cs

def store_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_LOCN
                (
                LOCN_KY NUMBER NOT NULL AUTOINCREMENT PRIMARY KEY,
                LOCN_ID NUMBER NOT NULL,
                RGN_KY NUMBER REFERENCES "BHATBHATENI_DWH"."TEMP".TEMP_REGION(RGN_KY),
                LOCN_DESC VARCHAR(50)
                );
                """
        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_LOCN")
        
        query = """
                INSERT INTO TEMP.TEMP_LOCN(LOCN_ID,RGN_KY,LOCN_DESC)
                SELECT STG.STG_STORE.STORE_ID, TEMP.TEMP_REGION.RGN_KY, STG.STG_STORE.STORE_DESC
                FROM STG.STG_STORE
                JOIN TEMP.TEMP_REGION
                ON STG.STG_STORE.REGION_ID = TEMP.TEMP_REGION.RGN_ID
                """

        cs.execute(query)