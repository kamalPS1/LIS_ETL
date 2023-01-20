from connection import cs

def subcategory_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_SUBCATEGORY
                (
                SUB_CTGRY_KY NUMBER NOT NULL AUTOINCREMENT PRIMARY KEY,
                SUB_CTGRY_ID NUMBER NOT NULL,
                CTGRY_KY NUMBER REFERENCES "BHATBHATENI_DWH"."TEMP".TEMP_CATEGORY(CTGRY_KY),
                SUB_CTGRY_DESC VARCHAR(50)
                );
                """
        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_SUBCATEGORY")
        
        query = """
                INSERT INTO TEMP.TEMP_SUBCATEGORY(SUB_CTGRY_ID,CTGRY_KY,SUB_CTGRY_DESC)
                SELECT STG.STG_SUBCATEGORY.SUBCATEGORY_ID, TEMP.TEMP_CATEGORY.CTGRY_KY, STG.STG_SUBCATEGORY.SUBCATEGORY_DESC
                FROM STG.STG_SUBCATEGORY
                JOIN TEMP.TEMP_CATEGORY
                ON TEMP.TEMP_CATEGORY.CTGRY_ID = STG.STG_SUBCATEGORY.CATEGORY_ID
                """

        cs.execute(query)