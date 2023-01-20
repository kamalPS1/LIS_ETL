from connection import cs

def create_schema_stg():
    cs.execute('USE DATABASE BHATBHATENI_DWH')
    cs.execute("CREATE OR REPLACE SCHEMA STG")

def create_schema_temp():
    cs.execute('USE DATABASE BHATBHATENI_DWH')
    cs.execute("CREATE OR REPLACE SCHEMA TEMP")

def create_schema_tgt():
    cs.execute('USE DATABASE BHATBHATENI_DWH')
    cs.execute("CREATE OR REPLACE SCHEMA TGT")