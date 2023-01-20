from connection import cs
from datetime import datetime

def sls_plc_month_tgt():
    cs.execute("USE DATABASE BHATBHATENI_DWH")

    current_time = datetime.now()

    insert = f"""
            INSERT INTO TGT.F_BHATBHATENI_AGG_SLS_PLC_MONTH_T
            (PDT_KY, LOCN_KY, CTGRY_KY, MONTH_KY, TOTAL_QTY, TOTAL_AMT, TOTAL_DSCNT, ROW_INSRT_TMS, ROW_UPDT_TMS)
                (SELECT tmp.PDT_KY, tmp.LOCN_KY, tmp.CTGRY_KY, tmp.MONTH_KY, tmp.TOTAL_QTY, tmp.TOTAL_AMT, tmp.TOTAL_DSCNT, '{current_time}', '{current_time}'
                FROM TEMP.F_BHATBHATENI_AGG_SLS_PLC_MONTH_TEMP tmp)
                """

    cs.execute(insert)