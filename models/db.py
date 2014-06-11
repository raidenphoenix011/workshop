import MySQLdb, hashlib
from flask import flash

mysql = MySQLdb.connect('localhost','AdminPayroll','Password','Eaglewatch')
cur = mysql.cursor()

def get(sql):
    try:
        cur.execute(sql)
        res = cur.fetchone()
        return res
    except MySQLdb.Error, e:
        print str(e.args[0]) + ': ' + str(e.args[1])
        #print 'Error retrieving data from the database'
        return None

def getAll(sql):
    try:
        cur.execute(sql)
        res = cur.fetchall()
        return res
    except MySQLdb.Error, e:
        print str(e.args[0]) + ': ' + str(e.args[1])
        #print 'Error retrieving data from the database'
        return None

def List(tableName):
    sql = "SELECT * FROM %s" % tableName
    res = getAll(sql)
    return res

def SubList(tableName, foreignKey, value):
    sql = "SELECT * FROM %s WHERE %s = '%s'" % (tableName, foreignKey, value)
    res = getAll(sql)
    return res

def SubList2(tableName, foreignKey1, value1, foreignKey2, value2):
    sql = "SELECT * FROM %s WHERE %s = '%s' AND %s = '%s'" % (tableName, foreignKey1, value1, foreignKey2, value2)
    res = getAll(sql)
    return res