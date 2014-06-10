import db, import_file
DetachmentContactPersons = import_file.import_file('DetachmentContactPersons')

def getDetachmentContactPersons():
  res = db.List("DetachmentContactPersons")
  DetachmentContactPersonsList = []
  for row in res:
    if row is not None:
      DetachmentContactPerson = DetachmentContactPersons.DetachmentContactPersons( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      DetachmentContactPersonsList.append(DetachmentContactPerson)
      row = db.cur.fetchone()
  return ClientContactPersonsList

def getDetachmentContactPerson(val):
  res = db.SubList("DetachmentContactPersons", "DetachID", val)
  DetachmentContactPersonsList = []
  for row in res:
    if row is not None:
      DetachmentContactPerson = DetachmentContactPersons.DetachmentContactPersons( int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      DetachmentContactPersonsList.append(DetachmentContactPerson)
      row = db.cur.fetchone()
  return DetachmentContactPersonsList
 