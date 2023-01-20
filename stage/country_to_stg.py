from connection import cs

def country_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        # STAGING AREA FOR COUNTRY
        int_stage_country = """CREATE OR REPLACE STAGE int_stage_country
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_country)

        int_stage_country = """COPY INTO @int_stage_country
                FROM BHATBHATENI.TRANSACTIONS.COUNTRY
                FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""

        cs.execute(int_stage_country)

        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_COUNTRY(COUNTRY_ID number, COUNTRY_DESC varchar(256))")

        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_COUNTRY ")

        put = "COPY INTO BHATBHATENI_DWH.STG.STG_COUNTRY from @int_stage_country file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)