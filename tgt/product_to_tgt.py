from connection import cs
from datetime import datetime

def product_to_tgt():
        cs.execute("USE DATABASE BHATBHATENI_DWH")

        current_time = datetime.now()

        update = f"""
                UPDATE TGT.D_BHATBHATENI_PDT_T tgt
                SET
                tgt.PDT_ID = tmp.PDT_ID,
                tgt.PDT_DESC = tmp.PDT_DESC,
                tgt. ROW_UPDT_TMS = '{current_time}'
                FROM TEMP.TEMP_PRODUCT tmp
                WHERE tgt.PDT_KY = tmp.PDT_KY;
                """

        cs.execute(update)

        insert = f"""
                INSERT INTO TGT.D_BHATBHATENI_PDT_T(PDT_KY,PDT_ID,SUB_CTGRY_KY,PDT_DESC,ACTV_FLG,OPEN_CLOSE_CD,ROW_INSRT_TMS,ROW_UPDT_TMS)
                SELECT PDT_KY, PDT_ID, SUB_CTGRY_KY, PDT_DESC,'Y','O', '{current_time}', '{current_time}'
                FROM TEMP.TEMP_PRODUCT
                WHERE PDT_KY NOT IN (SELECT PDT_KY FROM TGT.D_BHATBHATENI_PDT_T)
                """

        cs.execute(insert)


        not_active_N = f"""
        UPDATE TGT.D_BHATBHATENI_PDT_T
        SET
        ACTV_FLG = 'N',
        ROW_UPDT_TMS = '{current_time}'
        WHERE PDT_KY NOT IN 
        (SELECT PDT_KY FROM TEMP.TEMP_PRODUCT)
        AND ACTV_FLG = 'Y' ;
                """
        cs.execute(not_active_N)

        active_Y = f"""
        UPDATE TGT.D_BHATBHATENI_PDT_T
        SET
        ACTV_FLG = 'Y',
        ROW_UPDT_TMS = '{current_time}'
        WHERE ACTV_FLG = 'N' and PDT_KY IN
        (SELECT PDT_KY FROM TEMP.TEMP_PRODUCT);
        """
        cs.execute(active_Y)