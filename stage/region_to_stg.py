from connection import cs

def region_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        # STAGING AREA FOR REGION
        int_stage_region = """CREATE OR REPLACE STAGE int_stage_region
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_region)

        int_stage_region = """COPY INTO @int_stage_region
                FROM BHATBHATENI.TRANSACTIONS.REGION
                FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""
        cs.execute(int_stage_region)
        
        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_REGION(REGION_ID NUMBER, COUNTRY_ID NUMBER, REGION_DESC VARCHAR(256))")
        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_REGION ")

        put = "COPY INTO BHATBHATENI_DWH.STG.STG_REGION from @int_stage_region file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)