from connection import cs

def region_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_REGION
                (
                RGN_KY NUMBER NOT NULL AUTOINCREMENT PRIMARY KEY,
                RGN_ID NUMBER NOT NULL,
                CNTRY_KY NUMBER REFERENCES "BHATBHATENI_DWH"."TEMP".TEMP_COUNTRY(CNTRY_KY),
                RGN_DESC VARCHAR(50)
                );
                """
        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_REGION")
        
        query = """
                INSERT INTO TEMP.TEMP_REGION(RGN_ID, CNTRY_KY, RGN_DESC)
                SELECT STG.STG_REGION.REGION_ID, TEMP.TEMP_COUNTRY.CNTRY_KY, STG.STG_REGION.REGION_DESC
                FROM STG.STG_REGION
                JOIN TEMP.TEMP_COUNTRY
                ON STG.STG_REGION.COUNTRY_ID = TEMP.TEMP_COUNTRY.CNTRY_ID
                """

        cs.execute(query)
