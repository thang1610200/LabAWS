import insertUtil as ut
import psycopg2

con = psycopg2.connect(database = 'postgre_covid',host='database-postgre.cn4gbnrdol43.us-east-1.rds.amazonaws.com', user ='postgres', password = 'thang1610', port = '5432')
print('Connect Successfully');
ut.insert(con);
ut.select(con);
con.close()
print('Success')