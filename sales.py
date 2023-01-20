import csv
from database import run_database
from connection import cs

run_database(cs)
def salesCSV():
    # Exporting Data from Sales table in CSV format
    header_sales =['ID','STORE_ID','PRODUCT_ID','CUSTOMER_ID','TRANSACTION_TIME','QUANTITY','AMOUNT','DISCOUNT']
    sales = cs.execute("SELECT * FROM SALES")
    with open('csvfile/sales.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(header_sales)
        writer.writerows(sales)