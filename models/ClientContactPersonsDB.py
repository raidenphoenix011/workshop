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

#OK
def getClientContactPerson(val):
  res = db.SubList("ClientContactPersons", "ID", val)
  for row in res:
    if row is not None:
      Contact = ClientContactPersons.ClientContactPersons( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
  return Contact

#OK
def updateContact(contact):
  sql = "update ClientContactPersons set Suffix=%s, LastName=%s, FirstName=%s, MiddleName=%s, Landline=%s, MobileNo=%s, BirthDate=%s where ID=%s"
  params = (contact.Suffix, contact.LastName, contact.FirstName, contact.MiddleName, contact.Landline, contact.MobileNo, contact.BirthDate, contact.ID)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except:
    print 'Error saving contact'
    
def insertContact(contact):
  sql = "call addClientCP(%s, %s, %s, %s, %s, %s, %s, %s)"
  params = (contact.ClientID, contact.Suffix, contact.LastName, contact.FirstName, contact.MiddleName, contact.Landline, contact.MobileNo, contact.BirthDate)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except:
    print 'Error inserting contact'