import insertUtil as ut
import MySQLdb

con = MySQLdb.connect(host='database-aura.cluster-cn4gbnrdol43.us-east-1.rds.amazonaws.com', user ='admin', passwd = 'thang1610',db = 'aurora', port = '3306')
print('Connect Successfully');
ut.insert(con);
ut.select(con);
con.close()
print('Success')