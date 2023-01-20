from connection import cs
from datetime import datetime

def sales_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.F_BHATBHATENI_SLS_T tgt
                SET
                tgt.TRANSACTION_TIME = tmp.TRANSACTION_TIME,
                tgt.QTY = tmp.QTY,
                tgt.AMT = tmp.AMT,
                tgt.DSCNT = tmp.DSCNT,
                tgt.ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_SALES tmp
                WHERE tgt.SLS_ID = tmp.SLS_ID
                """
        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.F_BHATBHATENI_SLS_T(SLS_ID, LOCN_KY, PDT_KY, CUSTOMER_KY, TRANSACTION_TIME, QTY, AMT, DSCNT, OPEN_CLOSE_CD, ROW_INSRT_TMS, ROW_UPDT_TMS)
                SELECT tmp.SLS_ID, tmp.LOCN_KY, tmp.PDT_KY, tmp.CUSTOMER_KY, tmp.TRANSACTION_TIME, tmp.QTY, tmp.AMT, tmp.DSCNT, 'O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_SALES tmp
                WHERE tmp.SLS_ID NOT IN (SELECT SLS_ID FROM TGT.F_BHATBHATENI_SLS_T);
                """

        cs.execute(insert)
