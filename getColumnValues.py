# get column values from a table where the values are NULL
import os


def getColumnValues(database, table, column):
    with open("columnValues.hql","w") as hql:
        hql.write("use "+database+";"+"\n")
        hql.write("SELECT * FROM "+table+" WHERE isnull("+column+");"+"\n")
    hql.close()
    os.system("hive -f columnValues.hql > resultsForColumnValues.txt")
    counter = 0
    with open('resultsForColumnValues.txt', 'r') as reader:
        for i in reader:
            counter +=1 

    reader.close()
    print counter

dbName = "tpcds_parquet"
tableName = "et_customer"
columnName = "c_current_cdemo_sk"


getColumnValues(dbName, tableName, columnName)
