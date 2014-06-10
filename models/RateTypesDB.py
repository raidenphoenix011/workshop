<<<<<<< HEAD
import db, import_file
RateTypes = import_file.import_file('RateTypes')

def getRateTypes():
  res = db.List("RateTypes")
  RateTypesList = []
  for row in res:
    if row is not None:
      RateType = RateTypes.RateTypes( str(row[0]), str(row[1]) )
      RateTypesList.append(RateType)
      row = db.cur.fetchone()
  return RateTypesList

def getRateType(val):
  res = db.SubList("RateTypes", "ID", val)
  for row in res:
    if row is not None:
      RateType = RateTypes.RateTypes( str(row[0]), str(row[1]) )
  return RateType
=======
import db, import_file
RateTypes = import_file.import_file('RateTypes')

def getRateTypes():
  res = db.List("RateTypes")
  RateTypesList = []
  for row in res:
    if row is not None:
      RateType = RateTypes.RateTypes( str(row[0]), str(row[1]) )
      RateTypesList.append(RateType)
      row = cur.fetchone()
  return RateTypesList

def getRateType(val):
  res = db.SubList("RateTypes", "ID", val)
  for row in res:
    if row is not None:
      RateType = RateTypes.RateTypes( str(row[0]), str(row[1]) )
  return RateType
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
