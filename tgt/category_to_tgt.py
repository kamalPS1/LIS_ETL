from connection import cs
from datetime import datetime

def category_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.D_BHATBHATENI_CTGRY_T tgt
                SET
                tgt.CTGRY_ID = tmp.CTGRY_ID,
                tgt.CTGRY_DESC = tmp.CTGRY_DESC,
                tgt.ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_CATEGORY tmp
                WHERE tgt.CTGRY_KY = tmp.CTGRY_KY
                """
        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.D_BHATBHATENI_CTGRY_T(CTGRY_KY, CTGRY_ID, CTGRY_DESC, OPEN_CLOSE_CD, ROW_INSRT_TMS, ROW_UPDT_TMS)
                SELECT tmp.CTGRY_KY, tmp.CTGRY_ID, tmp.CTGRY_DESC, 'O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_CATEGORY tmp
                WHERE tmp.CTGRY_KY NOT IN (SELECT CTGRY_KY FROM TGT.D_BHATBHATENI_CTGRY_T);
                """

        cs.execute(insert)
