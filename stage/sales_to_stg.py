from connection import cs

def sales_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        int_stage_sales = """CREATE OR REPLACE STAGE int_stage_sales
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_sales)

        int_stage_sales = """COPY INTO @int_stage_sales
                        FROM BHATBHATENI.TRANSACTIONS.SALES
                        FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""
        cs.execute(int_stage_sales)

        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_SALES(SALES_ID NUMBER, STORE_ID NUMBER, PRODUCT_ID NUMBER, CUSTOMER_ID NUMBER,TRANSACTION_TIME TIMESTAMP, QUANTITY NUMBER, AMOUNT NUMBER(20,2), DISCOUNT NUMBER(20,2))")
        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_SALES")

        put = "COPY INTO BHATBHATENI_DWH.STG.STG_SALES FROM @int_stage_sales file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)