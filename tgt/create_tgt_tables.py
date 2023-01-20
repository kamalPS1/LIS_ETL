from connection import cs

def create_tgt_tables():
    cs.execute("USE DATABASE BHATBHATENI_DWH")
    cs.execute("USE SCHEMA TGT")
    create = ["""
            CREATE OR REPLACE TABLE TGT.D_BHATBHATENI_CNTRY_T
            (
            CNTRY_ID NUMBER,
            CNTRY_KY NUMBER NOT NULL,
            CNTRY_DESC VARCHAR(50),
            OPEN_CLOSE_CD VARCHAR(1), 
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT CNTRY_PK PRIMARY key (CNTRY_KY)
            );
            """,

            """
            CREATE OR REPLACE TABLE TGT.D_BHATBHATENI_RGN_T
            (
            RGN_ID NUMBER,
            RGN_KY NUMBER NOT NULL,
            CNTRY_KY NUMBER,
            RGN_DESC VARCHAR(50),
            OPEN_CLOSE_CD VARCHAR(1),  
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT RGN_PK PRIMARY key (RGN_KY),
            CONSTRAINT CNTRY_FK FOREIGN key (CNTRY_KY) REFERENCES D_BHATBHATENI_CNTRY_T(CNTRY_KY) 
            );
            """,

            """
            CREATE OR REPLACE TABLE TGT.D_BHATBHATENI_LOCN_T
            (
            LOCN_ID NUMBER,
            LOCN_KY NUMBER NOT NULL,
            RGN_KY NUMBER,
            LOCN_DESC VARCHAR(50),
            LAST_OPEN_TMS TIMESTAMP_NTZ,
            LAST_CLOSED_TMS TIMESTAMP_NTZ,
            ACTV_FLG VARCHAR(1),
            OPEN_CLOSE_CD VARCHAR(1), 
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT LOCN_PK PRIMARY KEY (LOCN_KY),
            CONSTRAINT RGN_FK FOREIGN KEY (RGN_KY) REFERENCES D_BHATBHATENI_RGN_T(RGN_KY)
            );
            """,

            """
            CREATE TABLE IF NOT EXISTS TGT.D_BHATBHATENI_CTGRY_T
            (
            CTGRY_ID NUMBER,
            CTGRY_KY NUMBER,
            CTGRY_DESC VARCHAR(50),
            OPEN_CLOSE_CD VARCHAR(1), 
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT CTGRY_PK PRIMARY KEY (CTGRY_KY)
            );
            """,

            """
            CREATE OR REPLACE TABLE TGT.D_BHATBHATENI_SUB_CTGRY_T
            (
            SUB_CTGRY_ID NUMBER,
            SUB_CTGRY_KY NUMBER,
            CTGRY_KY NUMBER,
            SUB_CTGRY_DESC VARCHAR(50),
            OPEN_CLOSE_CD VARCHAR(1), 
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT SUB_CTGRY_PK PRIMARY KEY (SUB_CTGRY_KY),
            CONSTRAINT CTGRY_FK FOREIGN KEY (CTGRY_KY) REFERENCES D_BHATBHATENI_CTGRY_T(CTGRY_KY)
            );
            """,

            """
            CREATE  OR REPLACE TABLE TGT.D_BHATBHATENI_PDT_T
            (
            PDT_ID NUMBER,
            PDT_KY NUMBER,
            SUB_CTGRY_KY NUMBER,
            PDT_DESC VARCHAR(50),
            PRICE NUMBER(10,2),
            ACTV_FLG VARCHAR(1),
            OPEN_CLOSE_CD VARCHAR(1),  ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT PDT_PK PRIMARY KEY (PDT_KY),
            CONSTRAINT SUB_CTGRY_FK FOREIGN KEY (SUB_CTGRY_KY) REFERENCES D_BHATBHATENI_SUB_CTGRY_T(SUB_CTGRY_KY)
            );
            """,

            """
            CREATE TABLE IF NOT EXISTS TGT.D_BHATBHATENI_CUSTOMER_T
            (
            CUSTOMER_ID NUMBER,
            CUSTOMER_KY NUMBER,
            CUSTOMER_FST_NM VARCHAR(20),
            CUSTOMER_MID_NM VARCHAR(20),
            CUSTOMER_LST_NM VARCHAR(20),
            CUSTOMER_ADDR VARCHAR(20),
            OPEN_CLOSE_CD VARCHAR(1),  
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT CUSTOMER_PK PRIMARY KEY (CUSTOMER_KY)
            );
            """,

            """
            CREATE OR REPLACE TABLE TGT.F_BHATBHATENI_SLS_T
            (
            SLS_ID NUMBER,
            LOCN_KY NUMBER,
            PDT_KY NUMBER,
            CUSTOMER_KY NUMBER,
            TRANSACTION_TIME TIMESTAMP_NTZ,
            QTY NUMBER,
            AMT NUMBER(10,2),
            DSCNT NUMBER(10,2),
            OPEN_CLOSE_CD VARCHAR(1),  
            ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT SLS_PK PRIMARY KEY (SLS_ID),
            CONSTRAINT LOCN_FK FOREIGN KEY (LOCN_KY) REFERENCES D_BHATBHATENI_LOCN_T(LOCN_KY),
            CONSTRAINT PDT_FK FOREIGN KEY (PDT_KY) REFERENCES D_BHATBHATENI_PDT_T(PDT_KY),
            CONSTRAINT CUSTOMER_FK FOREIGN KEY (CUSTOMER_KY) REFERENCES D_BHATBHATENI_CUSTOMER_T(CUSTOMER_KY)
            );
            """,

            """
            CREATE TABLE IF NOT EXISTS TGT.D_BHATBHATENI_TIME_YEAR_T
            (
            ID NUMBER,
            YEAR_KY NUMBER NOT NULL,
            YEAR_START_DATE DATE NOT NULL,
            YEAR_END_DATE DATE NOT NULL,
            OPEN_CLOSE_CD VARCHAR(1),  ROW_INSRT_TMS TIMESTAMP_NTZ,
            ROW_UPDT_TMS TIMESTAMP_NTZ,
            CONSTRAINT YEAR_PK PRIMARY KEY (YEAR_KY)
            );
            """,

            """
            CREATE OR REPLACE TABLE TGT.F_BHATBHATENI_AGG_SLS_PLC_MONTH_T
            (
                PDT_KY NUMBER NOT NULL,
                LOCN_KY NUMBER NOT NULL,
            CTGRY_KY NUMBER NOT NULL,
                MONTH_KY NUMBER NOT NULL,
                TOTAL_QTY NUMBER,
                TOTAL_AMT NUMBER(10,2),
                TOTAL_DSCNT NUMBER(10,2),
                ROW_INSRT_TMS TIMESTAMP_NTZ NOT NULL,
                ROW_UPDT_TMS TIMESTAMP_NTZ NOT NULL,
                CONSTRAINT PDT_FK FOREIGN KEY (PDT_KY) REFERENCES D_BHATBHATENI_PDT_T(PDT_KY),
            CONSTRAINT LOC_FK FOREIGN KEY (LOCN_KY) REFERENCES D_BHATBHATENI_LOCN_T(LOCN_KY),
                CONSTRAINT CAT_FK FOREIGN KEY (CTGRY_KY) REFERENCES D_BHATBHATENI_CTGRY_T(CTGRY_KY)
            );
            """]
    for i in create:
        cs.execute(i)