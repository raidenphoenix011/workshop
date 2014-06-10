import db, import_file
ManHourLogs = import_file.import_file('ManHourLogs')

def getManHourLogs():
  res = db.List("ManHourLogs")
  ManHourLogsList = []
  for row in res:
    if row is not None:
      ManHourLog = ManHourLogs.ManHourLogs( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), str(row[8]), str(row[9]) )
      ManHourLogsList.append(ManHourLog)
      row = cur.fetchone()
  return ManHourLogsList

def getLog(val):
  res = db.SubList("ManHourLog", "DetachID", val)
  ManHourLogsList = []
  for row in res:
    if row is not None:
      ManHourLog = ManHourLogs.ManHourLogs( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), str(row[8]), str(row[9]) )
      ManHourLogsList.append(ManHourLog)
      row = cur.fetchone()
  return ManHourLogsList
