# getting column count from a specified databases' table
import os

def getColumnCount(database, table, column):
    with open("gettingColumnCount.hql", "w") as hql:
        hql.write("USE "+database+";"+"\n")
        hql.write("SELECT COUNT("+column+") FROM "+table+";"+"\n")
    hql.close()
    os.system("cat gettingColumnCount.hql")


dbName = "tpcds_parquet"
tableName = "et_customer"
columnName = "c_customer_id"

getColumnCount(dbName, tableName, columnName)
