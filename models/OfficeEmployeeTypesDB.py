<<<<<<< HEAD
import db, import_file
OfficeEmployeeTypes = import_file.import_file('OfficeEmployeeTypes')

def getOfficeEmployeeTypes():
  res = db.List("OfficeEmployeeTypes")
  OfficeEmployeeTypesList = []
  for row in res:
    if row is not None:
      OfficeEmployeeType = OfficeEmployeeTypes.OfficeEmployeeTypes( str(row[0]), str(row[1]) )
      OfficeEmployeeTypes.append(OfficeEmployeeType)
      row = db.cur.fetchone()
  return OfficeEmployeeTypesList

def getOfficeEmployeeType(val):
  res = db.SubList("OfficeEmployeeTypes", "ID", val)
  for row in res:
    if row is not None:
      OfficeEmployeeType = OfficeEmployeeTypes.OfficeEmployeeTypes( str(row[0]), str(row[1]) )
  return OfficeEmployeeType
=======
import db, import_file
OfficeEmployeeTypes = import_file.import_file('OfficeEmployeeTypes')

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
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
