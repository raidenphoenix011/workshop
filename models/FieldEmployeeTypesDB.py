<<<<<<< HEAD
import db, import_file
FieldEmployeeTypes = import_file.import_file('FieldEmployeeTypes')

def getFieldEmployeeTypes():
  res = db.List("FieldEmployeeTypes")
  FieldEmployeeTypesList = []
  for row in res:
    if row is not None:
      FieldEmployeeType = FieldEmployeeTypes.FieldEmployeeTypes( str(row[0]), str(row[1]) )
      FieldEmployeeTypesList.append(FieldEmployeeType)
      row = db.cur.fetchone()
  return FieldEmployeeTypesList

def getFieldEmployeeTypes(val):
  res = db.SubList("FieldEmployeeTypes", "ID", val)
  for row in res:
    if row is not None:
      FieldEmployeeType = FieldEmployeeTypes.FieldEmployeeTypes( str(row[0]), str(row[1]) )
  return Detachment
=======
import db, import_file
FieldEmployeeTypes = import_file.import_file('FieldEmployeeTypes')

def getFieldEmployeeTypes():
  res = db.List("FieldEmployeeTypes")
  FieldEmployeeTypesList = []
  for row in res:
    if row is not None:
      FieldEmployeeType = FieldEmployeeTypes.FieldEmployeeTypes( str(row[0]), str(row[1]) )
      FieldEmployeeTypesList.append(FieldEmployeeType)
      row = cur.fetchone()
  return FieldEmployeeTypesList

def getFieldEmployeeTypes(val):
  res = db.SubList("FieldEmployeeTypes", "ID", val)
  for row in res:
    if row is not None:
      FieldEmployeeType = FieldEmployeeTypes.FieldEmployeeTypes( str(row[0]), str(row[1]) )
  return Detachment
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
