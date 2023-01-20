from connection import cs

def customer_to_stg():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        format = """ 
                create or replace file format ETL
                type = csv
                field_delimiter = '|'
                field_optionally_enclosed_by = '0x27'
                null_if = ('NULL');
                """
        cs.execute(format)

        int_stage_customer = """CREATE OR REPLACE STAGE int_stage_customer
                        FILE_FORMAT = 'ETL'"""
        cs.execute(int_stage_customer)

        int_stage_customer = """COPY INTO @int_stage_customer
                        FROM BHATBHATENI.TRANSACTIONS.CUSTOMER
                        FILE_FORMAT = (format_name = 'ETL' compression = none) overwrite = true;"""
        cs.execute(int_stage_customer)

        cs.execute("CREATE OR REPLACE TABLE BHATBHATENI_DWH.STG.STG_CUSTOMER(customer_id NUMBER,customer_first_name VARCHAR(256),customer_middle_name VARCHAR(256),customer_last_name VARCHAR(256),customer_address VARCHAR(256))")
        cs.execute("TRUNCATE TABLE BHATBHATENI_DWH.STG.STG_CUSTOMER ")
        
        put = "COPY INTO BHATBHATENI_DWH.STG.STG_CUSTOMER FROM @int_stage_customer file_format = (format_name = 'ETL' compression = none);"
        cs.execute(put)
