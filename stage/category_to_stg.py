from connection import cs

def category_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")
        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        int_stage_category = """CREATE OR REPLACE STAGE int_stage_category 
        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_category)

        int_stage_category = """COPY INTO @int_stage_category
                                FROM BHATBHATENI.TRANSACTIONS.CATEGORY
                                FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""

        cs.execute(int_stage_category)

        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_CATEGORY(CATEGORY_ID NUMBER, CATEGORY_DESC VARCHAR(1024))")
        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_CATEGORY ")
        
        put = """COPY INTO BHATBHATENI_DWH.STG.STG_CATEGORY FROM @int_stage_category
                file_format = (format_name = 'ETL' compression = none);"""
        cs.execute(put)
