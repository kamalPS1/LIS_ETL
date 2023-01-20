from connection import cs
from datetime import datetime

def customer_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.D_BHATBHATENI_CUSTOMER_T tgt
                SET
                tgt.CUSTOMER_ID = tmp.CUSTOMER_ID,
                tgt.CUSTOMER_FST_NM = tmp.CUSTOMER_FST_NM,
                tgt.CUSTOMER_MID_NM = tmp.CUSTOMER_MID_NM,
                tgt.CUSTOMER_LST_NM = tmp.CUSTOMER_LST_NM,
                tgt.CUSTOMER_ADDR = tmp.CUSTOMER_ADDR,
                tgt.ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_CUSTOMER tmp
                WHERE tgt.CUSTOMER_KY = tmp.CUSTOMER_KY
                """
        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.D_BHATBHATENI_CUSTOMER_T(CUSTOMER_KY, CUSTOMER_ID, CUSTOMER_FST_NM, CUSTOMER_MID_NM, CUSTOMER_LST_NM, CUSTOMER_ADDR, OPEN_CLOSE_CD, ROW_INSRT_TMS, ROW_UPDT_TMS)
                SELECT tmp.CUSTOMER_KY, tmp.CUSTOMER_ID, tmp.CUSTOMER_FST_NM, tmp.CUSTOMER_MID_NM, tmp.CUSTOMER_LST_NM, tmp.CUSTOMER_ADDR, 'O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_CUSTOMER tmp
                WHERE tmp.CUSTOMER_KY NOT IN (SELECT CUSTOMER_KY FROM TGT.D_BHATBHATENI_CUSTOMER_T);
                """

        cs.execute(insert)
