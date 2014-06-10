<<<<<<< HEAD
import db, import_file
ClientContactPersons = import_file.import_file('ClientContactPersons')

def getAllClientContactPersons():
  res = db.List("ClientContactPersons")
  ClientContactPersonsList = []
  for row in res:
    if row is not None:
      ClientContactPerson = ClientContactPersons.ClientContactPersons( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      ClientContactPersonsList.append(ClientContactPerson)
      row = db.cur.fetchone()
  return ClientContactPersonsList

def getClientContactPersons(val):
  res = db.SubList("ClientContactPersons", "ClientID", val)
  ClientContactPersonsList = []
  for row in res:
    if row is not None:
      ClientContactPerson = ClientContactPersons.ClientContactPersons( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      ClientContactPersonsList.append(ClientContactPerson)
      row = db.cur.fetchone()
  return ClientContactPersonsList
=======
import db, import_file
ClientContactPersons = import_file.import_file('ClientContactPersons')

def getAllClientContactPersons():
  res = db.List("ClientContactPersons")
  ClientContactPersonsList = []
  for row in res:
    if row is not None:
      ClientContactPerson = ClientContactPersons.ClientContactPersons( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      ClientContactPersonsList.append(ClientContactPerson)
      row = db.cur.fetchone()
  return ClientContactPersonsList

#OK
def getClientContactPersons(val):
  res = db.SubList("ClientContactPersons", "ClientID", val)
  ClientContactPersonsList = []
  for row in res:
    if row is not None:
      ClientContactPerson = ClientContactPersons.ClientContactPersons( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      ClientContactPersonsList.append(ClientContactPerson)
      row = db.cur.fetchone()
  return ClientContactPersonsList
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
