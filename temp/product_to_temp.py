from connection import cs

def product_to_temp():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        

        create = """
                CREATE OR REPLACE TABLE TEMP.TEMP_PRODUCT
                (
                PDT_KY NUMBER NOT NULL AUTOINCREMENT PRIMARY KEY,
                PDT_ID NUMBER NOT NULL,
                SUB_CTGRY_KY NUMBER REFERENCES "BHATBHATENI_DWH"."TEMP".TEMP_SUBCATEGORY(SUB_CTGRY_KY),
                PDT_DESC VARCHAR(50)
                );
                """
        cs.execute(create)
        cs.execute("TRUNCATE TABLE TEMP.TEMP_PRODUCT")
        
        query = """
                INSERT INTO TEMP.TEMP_PRODUCT(PDT_ID, SUB_CTGRY_KY, PDT_DESC)
                SELECT STG.STG_PRODUCT.PRODUCT_ID, TEMP.TEMP_SUBCATEGORY.SUB_CTGRY_KY, STG.STG_PRODUCT.PRODUCT_DESC
                FROM STG.STG_PRODUCT
                JOIN TEMP.TEMP_SUBCATEGORY
                ON STG.STG_PRODUCT.SUBCATEGORY_ID = TEMP.TEMP_SUBCATEGORY.SUB_CTGRY_ID
                """

        cs.execute(query)