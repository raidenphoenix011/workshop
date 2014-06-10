import db, import_file
Clients = import_file.import_file('Clients')

def getAllClients():
  res = db.List("Clients")
  ClientList = []
  for row in res:
    if row is not None:
      Client = Clients.Clients( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      ClientList.append(Client)
      row = cur.fetchone()
  return ClientList

def getClient(val):
  res = db.SubList("Clients", "ID", val)
  for row in res:
    if row is not None:
      Client = Clients.Clients( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
  return Client
