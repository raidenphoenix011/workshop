import db, OfficeEmployees, hashlib, cgi, cgitb; cgitb.enable()

def getOfficeEmployees():
  res = db.List("OfficeEmployees")
  OfficeEmployeesList = []
  for row in res:
    if row is not None:
      OfficeEmployee = OfficeEmployees.OfficeEmployees( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), int(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]) )
      OfficeEmployeesList.append(OfficeEmployee)
      row = cur.fetchone()
  return OfficeEmployeesList

def getOfficeEmployee(val):
  res = db.SubList("OfficeEmployees", "Username", val)
  for row in res:
    if row is not None:
      OfficeEmployee = OfficeEmployees.OfficeEmployees( int(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), int(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]) )
  return OfficeEmployee

def login(username, password):
  sql = "SELECT Username, Password FROM OfficeEmployees WHERE Username = '%s'" % username
  res = db.get(sql)
  for row in res:
    if row is not None:
      if hashlib.sha1(password).hexdigest() == row:
        return True
  return None

