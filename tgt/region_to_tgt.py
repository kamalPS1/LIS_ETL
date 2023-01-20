from connection import cs
from datetime import datetime

def region_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.D_BHATBHATENI_RGN_T tgt
                SET
                tgt.RGN_ID = tmp.RGN_ID,
                tgt.RGN_DESC = tmp.RGN_DESC,
                tgt.ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_REGION tmp
                WHERE tgt.RGN_KY =tmp.RGN_KY
                """

        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.D_BHATBHATENI_RGN_T(RGN_ID, RGN_KY, CNTRY_KY, RGN_DESC, OPEN_CLOSE_CD, ROW_INSRT_TMS, ROW_UPDT_TMS)
                SELECT tmp.RGN_ID, tmp.RGN_KY, tmp.CNTRY_KY, tmp.RGN_DESC,'O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_REGION tmp
                WHERE tmp.RGN_KY NOT IN (SELECT RGN_KY FROM TGT.D_BHATBHATENI_RGN_T)
                """

        cs.execute(insert)