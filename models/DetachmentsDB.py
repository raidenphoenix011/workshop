import db, Detachments, cgi, cgitb; cgitb.enable()

def getAllDetachments():
  res = db.List("Detachments")
  DetachmentsList = []
  for row in res:
    if row is not None:
      Detachment = Detachments.Detachments( int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]) )
      DetachmentsList.append(Detachment)
      row = cur.fetchone()
  return DetachmentsList

def getDetachments(val):
  res = db.SubList("Detachments", "ID", val)
  DetachmentsList = []
  for row in res:
    if row is not None:
      Detachment = Detachments.Detachments( int(row[0]), int(row[1]), int(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]) )
      DetachmentsList.append(Detachment)
      row = cur.fetchone()
  return DetachmentsList