import db, Logs, cgi, cgitb; cgitb.enable()

def getLogs():
  res = db.List("Logs")
  LogsList = []
  for row in res:
    if row is not None:
      Log = Logs.Logs( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]) )
      Logs.append(Log)
      row = cur.fetchone()
  return LogsList

def getLog(val):
  res = db.SubList("Logs", "ID", val)
  for row in res:
    if row is not None:
      Log = Logs.Logs( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]) )
  return Log
