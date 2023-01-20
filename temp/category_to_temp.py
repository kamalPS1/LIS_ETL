from connection import cs

def category_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_CATEGORY
                (
                CTGRY_KY NUMBER NOT NULL AUTOINCREMENT PRIMARY KEY,
                CTGRY_ID NUMBER NOT NULL,
                CTGRY_DESC VARCHAR(50)
                );
                """

        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_CATEGORY")

        query = """
                INSERT INTO TEMP.TEMP_CATEGORY(CTGRY_ID,CTGRY_DESC)
                SELECT STG.STG_CATEGORY.CATEGORY_ID,STG.STG_CATEGORY.CATEGORY_DESC
                FROM STG.STG_CATEGORY
                """

        cs.execute(query)