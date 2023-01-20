from connection import cs

def create_database():
    cs.execute("CREATE DATABASE IF NOT EXISTS BHATBHATENI_DWH")