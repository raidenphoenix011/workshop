import import_file
ManHourLogs = import_file.import_file('ManHourLogs')
db = import_file.import_file('db')

def getManHourLogs():
  res = db.List("ManHourLogs")
  ManHourLogsList = []
  for row in res:
    if row is not None:
      ManHourLog = ManHourLogs.ManHourLogs( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), str(row[9]), str(row[10]) )
      ManHourLogsList.append(ManHourLog)
      row = db.cur.fetchone()
  return ManHourLogsList

def getLog(val1):
  res = db.SubList("ManHourLogs", "DetachID", val1)
  ManHourLogsList = []
  for row in res:
    if row is not None:
      ManHourLog = ManHourLogs.ManHourLogs( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), str(row[9]), str(row[10]) )
      ManHourLogsList.append(ManHourLog)
      row = db.cur.fetchone()
  return ManHourLogsList

def getLog2(val1, val2):
  res = db.SubList2("ManHourLogs", "DetachID", val1, "PeriodCode", val2)
  ManHourLogsList = []
  for row in res:
    if row is not None:
      ManHourLog = ManHourLogs.ManHourLogs( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), str(row[9]), str(row[10]) )
      ManHourLogsList.append(ManHourLog)
      row = db.cur.fetchone()
  return ManHourLogsList
