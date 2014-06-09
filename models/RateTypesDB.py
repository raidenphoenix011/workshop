import db, RateTypes, cgi, cgitb; cgitb.enable()

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
