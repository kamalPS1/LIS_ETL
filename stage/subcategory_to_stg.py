from connection import cs

def subcategory_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        int_stage_subcategory = """CREATE OR REPLACE STAGE int_stage_subcategory
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_subcategory)

        int_stage_subcategory = """COPY INTO @int_stage_subcategory
                        FROM BHATBHATENI.TRANSACTIONS.SUBCATEGORY
                        FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""
        cs.execute(int_stage_subcategory)

        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_SUBCATEGORY(SUBCATEGORY_ID NUMBER, CATEGORY_ID NUMBER, SUBCATEGORY_DESC VARCHAR(256))")
        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_SUBCATEGORY ")
        
        put = "COPY INTO BHATBHATENI_DWH.STG.STG_SUBCATEGORY FROM @int_stage_subcategory file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)