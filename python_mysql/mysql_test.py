import MySQLdb
 
try:
    conn = MySQLdb.connect(host='localhost',user='root',passwd='luyi123',db='test',port=3306)
    cur = conn.cursor()
    cur.execute("SELECT VERSION()")
    data = cur.fetchone()
    print "Database version : %s" % data
     
                       
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" %(e.args[0], e.args[1])
    
finally:
    if cur:
        cur.close()
