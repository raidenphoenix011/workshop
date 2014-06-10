import MySQLdb, hashlib, cgi, cgitb; cgitb.enable()
import logging
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
