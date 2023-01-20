from connection import cs
from datetime import datetime

def subcategory_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.D_BHATBHATENI_SUB_CTGRY_T tgt
                SET
                tgt.SUB_CTGRY_ID = tmp.SUB_CTGRY_ID,
                tgt.SUB_CTGRY_DESC = tmp.SUB_CTGRY_DESC,
                tgt.ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_SUBCATEGORY tmp
                WHERE tgt.SUB_CTGRY_KY = tmp.SUB_CTGRY_KY
                """
        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.D_BHATBHATENI_SUB_CTGRY_T(SUB_CTGRY_ID, SUB_CTGRY_KY, CTGRY_KY, SUB_CTGRY_DESC, OPEN_CLOSE_CD, ROW_INSRT_TMS, ROW_UPDT_TMS)
                SELECT tmp.SUB_CTGRY_ID, tmp.SUB_CTGRY_KY, tmp.CTGRY_KY, tmp.SUB_CTGRY_DESC, 'O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_SUBCATEGORY tmp
                WHERE tmp.SUB_CTGRY_KY NOT IN (SELECT SUB_CTGRY_KY FROM TGT.D_BHATBHATENI_SUB_CTGRY_T);
                """

        cs.execute(insert)
