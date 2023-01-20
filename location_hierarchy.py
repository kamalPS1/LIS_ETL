import csv
from database import run_database
from connection import cs

def location_hierarchy():
    run_database(cs) #use database and schema from database.py

    # Exporting Data from Store table in CSV format
    header_store =['ID','REGION_ID','STORE_DESC']
    store = cs.execute("SELECT * FROM STORE")
    with open('csvfile/store.csv','w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header_store)
        csv_writer.writerows(store)

    # Exporting Data from Region table in CSV format
    header_region = ['ID','COUNTRY_ID','REGION_DESC']
    region = cs.execute("SELECT * FROM REGION")
    with open('csvfile/region.csv','w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header_region)
        csv_writer.writerows(region)

    # Exporting Data from Country table in CSV format
    header_country = ['ID','COUNTRY_DESC']
    country = cs.execute("SELECT * FROM COUNTRY")
    with open('csvfile/country.csv','w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(header_country)
        csv_writer.writerows(country)

location_hierarchy()