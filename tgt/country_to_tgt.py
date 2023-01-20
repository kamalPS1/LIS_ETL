from connection import cs
from datetime import datetime

def country_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.D_BHATBHATENI_CNTRY_T tgt
                SET
                tgt.CNTRY_ID = tmp.CNTRY_ID,
                tgt.CNTRY_DESC = tmp.CNTRY_DESC,
                tgt.ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_COUNTRY tmp
                WHERE tgt.CNTRY_KY = tmp.CNTRY_KY
                """
        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.D_BHATBHATENI_CNTRY_T(CNTRY_KY, CNTRY_ID, CNTRY_DESC, OPEN_CLOSE_CD, ROW_INSRT_TMS, ROW_UPDT_TMS)
                SELECT tmp.CNTRY_KY, tmp.CNTRY_ID, tmp.CNTRY_DESC, 'O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_COUNTRY tmp
                WHERE tmp.CNTRY_KY NOT IN (SELECT CNTRY_KY FROM TGT.D_BHATBHATENI_CNTRY_T);
                """

        cs.execute(insert)
