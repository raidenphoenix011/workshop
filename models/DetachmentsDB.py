import db, import_file, MySQLdb
Detachments = import_file.import_file('Detachments')

#OK
def getAllDetachments():
  res = db.List("Detachments")
  DetachmentsList = []
  for row in res:
    if row is not None:
      Detachment = Detachments.Detachments( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      DetachmentsList.append(Detachment)
      row = db.cur.fetchone()
  return DetachmentsList

#OK
def getAllDetachmentsbyID(val):
  res = db.SubList("Detachments", "ClientID", val)
  DetachmentList = []
  for row in res:
    if row is not None:
      Detachment = Detachments.Detachments( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
      DetachmentList.append(Detachment)
      row = db.cur.fetchone()
  return DetachmentList

#OK
def getDetachment(val):
  res = db.SubList("Detachments", "ID", val)
  for row in res:
    if row is not None:
      Detachment = Detachments.Detachments( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]) )
  return Detachment

#OK
def insertDetachment(detachment):
  sql = "call addDetachment(%s, %s, %s, %s, %s, %s, %s)"
  params = (detachment.ClientID, detachment.Name, detachment.Address, detachment.City, detachment.StartDate, detachment.EndDate, detachment.Status)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except MySQLdb.Error, e:
    print str(e.args[0]) + ': ' + str(e.args[1])
    #print 'Error retrieving data from the database'
    return None

def updateDetachment(detachment):
  sql = "update Detachments set Name=%s, Status=%s, StartDate=%s, EndDate=%s, City=%s, Address=%s where ID=%s"
  params = (detachment.Name, detachment.Status, detachment.StartDate, detachment.EndDate, detachment.City, detachment.Address, detachment.ID)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except MySQLdb.Error, e:
    print str(e.args[0]) + ': ' + str(e.args[1])
    #print 'Error retrieving data from the database'
    return None