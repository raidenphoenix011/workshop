
import db, import_file
DetachmentContactPersons = import_file.import_file('DetachmentContactPersons')


def getDetachmentContactPersons(val):
  res = db.SubList("DetachmentContactPersons", "DetachID", val)
  DetachmentContactPersonsList = []
  for row in res:
    if row is not None:
      DetachmentContactPerson = DetachmentContactPersons.DetachmentContactPersons( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      DetachmentContactPersonsList.append(DetachmentContactPerson)
      row = db.cur.fetchone()
  return DetachmentContactPersonsList

#OK
def getDetachmentContactPerson(val):
  res = db.SubList("DetachmentContactPersons", "ID", val)
  for row in res:
    if row is not None:
      Contact = DetachmentContactPersons.DetachmentContactPersons( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
  return Contact

#OK
def insertContact(contact):
  sql = "call addDetachmentCP(%s, %s, %s, %s, %s, %s, %s, %s)"
  params = (contact.DetachID, contact.Suffix, contact.LastName, contact.FirstName, contact.MiddleName, contact.Landline, contact.MobileNo, contact.BirthDate)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except:
    print 'Error inserting contact'
    
#OK
def updateContact(contact):
  sql = "update DetachmentContactPersons set Suffix=%s, LastName=%s, FirstName=%s, MiddleName=%s, Landline=%s, MobileNo=%s, BirthDate=%s where ID=%s"
  params = (contact.Suffix, contact.LastName, contact.FirstName, contact.MiddleName, contact.Landline, contact.MobileNo, contact.BirthDate, contact.ID)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except:
    print 'Error saving contact'