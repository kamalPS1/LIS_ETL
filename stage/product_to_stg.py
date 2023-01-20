from connection import cs

def product_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        int_stage_product = """CREATE OR REPLACE STAGE int_stage_product
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_product)

        int_stage_product = """COPY INTO @int_stage_product
                        FROM BHATBHATENI.TRANSACTIONS.PRODUCT
                        FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""
        cs.execute(int_stage_product)

        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_PRODUCT(product_id NUMBER, subcategory_id NUMBER, product_desc VARCHAR(256))")
        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_PRODUCT ")

        put = "COPY INTO BHATBHATENI_DWH.STG.STG_PRODUCT FROM @int_stage_product file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)
