import db, import_file
HolidayMOR = import_file.import_file('HolidayMOR')

def getAllHolidayMOR():
  res = db.List("HolidayMOR")
  HolidayMORList = []
  for row in res:
    if row is not None:
      HolidayMOR = HolidayMOR.HolidayMOR( str(row[0]), str(row[1]) )
      HolidayMORList.append(HolidayMOR)
      row = cur.fetchone()
  return HolidayMORList

def getHolidayMOR(val):
  res = db.SubList("HolidayMOR", "ID", val)
  for row in res:
    if row is not None:
      HolidayMOR = HolidayMOR.HolidayMOR( str(row[0]), str(row[1]) )
  return HolidayMOR
