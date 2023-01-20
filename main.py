from connection import cs
import logging
logging.basicConfig(level=logging.DEBUG, filename='my_log.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

from create_database import create_database
from sales import salesCSV
from location_hierarchy import location_hierarchy
from create_schema import create_schema_stg
from stage.country_to_stg import country_to_stg
from stage.region_to_stg import region_to_stg
from stage.store_to_stg import store_to_stg
from stage.category_to_stg import category_to_stg
from stage.subcategory_to_stg import subcategory_to_stg
from stage.product_to_stg import product_to_stg
from stage.customer_to_stg import customer_to_stg
from stage.sales_to_stg import sales_to_stg

from create_schema import create_schema_temp
from temp.country_to_temp import country_to_temp
from temp.region_to_temp import region_to_temp
from temp.store_to_temp import store_to_temp
from temp.category_to_temp import category_to_temp
from temp.subcategory_to_temp import subcategory_to_temp
from temp.product_to_temp import product_to_temp
from temp.customer_to_temp import customer_to_temp
from temp.sales_to_temp import sales_to_temp
from temp.SLS_PLC_MONTH_TEMP import sls_plc_month_temp

from tgt.create_tgt_tables import create_tgt_tables
from create_schema import create_schema_tgt
from tgt.country_to_tgt import country_to_tgt
from tgt.region_to_tgt import region_to_tgt
from tgt.store_to_tgt import store_to_tgt
from tgt.category_to_tgt import category_to_tgt
from tgt.subcategory_to_tgt import subcategory_to_tgt
from tgt.product_to_tgt import product_to_tgt
from tgt.customer_to_tgt import customer_to_tgt
from tgt.sales_to_tgt import sales_to_tgt
from tgt.SLS_PLC_MONTH_TGT import sls_plc_month_tgt


print("--------------CSV DOWNLOADING--------------")
salesCSV()
location_hierarchy()
print("--------------ETL STARTED--------------")
logging.debug('-----ETL STARTED-----')
logging.debug('-----CREATING DATABASE-----')
create_database()
logging.debug('-----CREATING STAGE SCHEMA-----')
country_to_stg()
logging.debug('-----COUNTRY TO STAGE-----')
country_to_stg()
logging.debug('-----REGION TO STAGE-----')
region_to_stg()
logging.debug('-----STORE TO STAGE-----')
store_to_stg()
logging.debug('-----CATEGORY TO STAGE-----')
category_to_stg()
logging.debug('-----SUBCATEGORY TO STAGE-----')
subcategory_to_stg()
logging.debug('-----PRODUCT TO STAGE-----')
product_to_stg()
logging.debug('-----CUSTOMER TO STAGE-----')
customer_to_stg()
logging.debug('-----SALES TO STAGE-----')
sales_to_stg()

logging.debug('-----CREATING TEMP SCHEMA-----')
create_schema_temp()
logging.debug('-----COUNTRY TO TEMP-----')
country_to_temp()
logging.debug('-----REGION TO TEMP-----')
region_to_temp()
logging.debug('-----STORE TO TEMP-----')
store_to_temp()
logging.debug('-----CATEGORY TO TEMP-----')
category_to_temp()
logging.debug('-----SUBCATEGORY TO TEMP-----')
subcategory_to_temp()
logging.debug('-----PRODUCT TO TEMP-----')
product_to_temp()
logging.debug('-----CUSTOMER TO TEMP-----')
customer_to_temp()
logging.debug('-----SALES TO TEMP-----')
sales_to_temp()
logging.debug('-----SALES_AGGREGATE_MONTH TO TEMP-----')
sls_plc_month_temp()

logging.debug('-----CREATING TGT SCHEMA-----')
create_schema_tgt()
logging.debug('-----CREATING TGT TABLES-----')
create_tgt_tables()
logging.debug('-----COUNTRY TO TARGET-----')
country_to_tgt()
logging.debug('-----REGION TO TARGET-----')
region_to_tgt()
logging.debug('-----STORE TO TARGET-----')
store_to_tgt()
logging.debug('-----CATEGORY TO TARGET-----')
category_to_tgt()
logging.debug('-----SUBCATEGORY TO TARGET-----')
subcategory_to_tgt()
logging.debug('-----PRODUCT TO TARGET-----')
product_to_tgt()
logging.debug('-----CUSTOMER TO TARGET-----')
customer_to_tgt()
logging.debug('-----SALES TO TARGET-----')
sales_to_tgt()
logging.debug('-----SALES_AGGREGATE_MONTH TO TARGET-----')
sls_plc_month_tgt()

logging.debug('-----ETL COMPLETED-----')
print("--------------ETL COMPLETED--------------")
