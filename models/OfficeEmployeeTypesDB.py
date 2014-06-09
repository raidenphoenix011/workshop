import db, OfficeEmployeeTypes, cgi, cgitb; cgitb.enable()

def getOfficeEmployeeTypes():
  res = db.List("OfficeEmployeeTypes")
  OfficeEmployeeTypesList = []
  for row in res:
    if row is not None:
      OfficeEmployeeType = OfficeEmployeeTypes.OfficeEmployeeTypes( str(row[0]), str(row[1]) )
      OfficeEmployeeTypes.append(OfficeEmployeeType)
      row = cur.fetchone()
  return OfficeEmployeeTypesList

def getOfficeEmployeeType(val):
  res = db.SubList("OfficeEmployeeTypes", "ID", val)
  for row in res:
    if row is not None:
      OfficeEmployeeType = OfficeEmployeeTypes.OfficeEmployeeTypes( str(row[0]), str(row[1]) )
  return OfficeEmployeeType
