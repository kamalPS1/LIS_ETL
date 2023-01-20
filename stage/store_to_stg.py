from connection import cs

def store_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        # STAGING AREA FOR STORE
        int_stage_store = """CREATE OR REPLACE STAGE int_stage_store
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_store)

        int_stage_store = """COPY INTO @int_stage_store
                FROM BHATBHATENI.TRANSACTIONS.STORE
                FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""
        cs.execute(int_stage_store)

        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_STORE(STORE_ID NUMBER, REGION_ID NUMBER, STORE_DESC VARCHAR(256))")
        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_STORE ")

        put = "COPY INTO BHATBHATENI_DWH.STG.STG_STORE from @int_stage_store file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)