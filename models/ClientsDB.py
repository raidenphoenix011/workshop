import db, import_file, MySQLdb
Clients = import_file.import_file('Clients')

#OK
def getAllClients():
  res = db.List("Clients")
  ClientList = []
  for row in res:
    if row is not None:
      Client = Clients.Clients( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      ClientList.append(Client)
      row = db.cur.fetchone()
  return ClientList

#OK
def getClient(val):
  res = db.SubList("Clients", "ID", val)
  for row in res:
    if row is not None:
      Client = Clients.Clients( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
  return Client

#OK
def saveClient(client):
  sql = "update Clients set Name=%s, BillingAddress=%s, City=%s, Landline=%s where ID=%s"
  params = (client.Name, client.BillingAddress, client.City, client.Landline, client.ID)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except:
    print 'Error saving client'

#OK
def insertClient(client):
  sql = "call addClient(%s, %s, %s, %s)"
  params = (client.Name, client.BillingAddress, client.City, client.Landline)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except:
    print 'Error saving client'

#OK
def getClientName(val):
  try: 
    db.cur.execute("select Name from Clients where ID = %s" % (val))
    res = db.cur.fetchone()
    return res[0]
  except MySQLdb.Error, e:
    print str(e.args[0]) + ': ' + str(e.args[1])
    #print 'Error retrieving data from the database'
    return None

#OK
def getClientID(name):
  try: 
    db.cur.execute("select ID from Clients where Name = '%s'" % (name))
    res = db.cur.fetchone()
    return res[0]
  except MySQLdb.Error, e:
    print str(e.args[0]) + ': ' + str(e.args[1])
    print 'Error retrieving data from the database'
    return None