from connection import cs

def country_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_COUNTRY
                (
                CNTRY_KY NUMBER NOT NULL AUTOINCREMENT PRIMARY KEY,
                CNTRY_ID NUMBER NOT NULL,
                CNTRY_DESC VARCHAR(50)
                );
                """
        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_COUNTRY")
        
        query = """
                INSERT INTO TEMP.TEMP_COUNTRY(CNTRY_ID,CNTRY_DESC)
                SELECT STG.STG_COUNTRY.COUNTRY_ID, STG.STG_COUNTRY.COUNTRY_DESC
                FROM STG.STG_COUNTRY
                """

        cs.execute(query)