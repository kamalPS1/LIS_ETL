from connection import cs
from datetime import datetime

def store_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.D_BHATBHATENI_LOCN_T tgt
                SET
                tgt.LOCN_ID = tmp.LOCN_ID,
                tgt.LOCN_DESC = tmp.LOCN_DESC,
                tgt. ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_LOCN tmp
                WHERE tgt.LOCN_KY = tmp.LOCN_KY;
                """

        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.D_BHATBHATENI_LOCN_T(LOCN_KY,LOCN_ID,RGN_KY,LOCN_DESC,LAST_OPEN_TMS,ACTV_FLG,OPEN_CLOSE_CD,ROW_INSRT_TMS,ROW_UPDT_TMS)
                SELECT LOCN_KY, LOCN_ID, RGN_KY, LOCN_DESC, '{current_time}','Y','O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_LOCN
                WHERE LOCN_KY NOT IN (SELECT LOCN_KY FROM TGT.D_BHATBHATENI_LOCN_T)
                """

        cs.execute(insert)


        not_active_N = f"""
        UPDATE TGT.D_BHATBHATENI_LOCN_T
        SET
        ACTV_FLG = 'N',
        LAST_CLOSED_TMS = '{current_time}',
        ROW_UPDT_TMS = '{current_time}'
        WHERE LOCN_KY NOT IN 
        (SELECT LOCN_KY FROM TEMP.TEMP_LOCN)
        AND ACTV_FLG = 'Y' ;
                """
        cs.execute(not_active_N)

        active_Y = f"""
        UPDATE TGT.D_BHATBHATENI_LOCN_T
        SET
        ACTV_FLG = 'Y',
        LAST_CLOSED_TMS = NULL,
        ROW_UPDT_TMS = '{current_time}'
        WHERE ACTV_FLG = 'N' and LOCN_KY IN
        (SELECT LOCN_KY FROM TEMP.TEMP_LOCN);
        """
        cs.execute(active_Y)