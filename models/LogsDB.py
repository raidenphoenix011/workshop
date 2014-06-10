<<<<<<< HEAD
import db, import_file
Logs = import_file.import_file('Logs')

def getLogs():
  res = db.List("Logs")
  LogsList = []
  for row in res:
    if row is not None:
      Log = Logs.Logs( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]) )
      Logs.append(Log)
      row = db.cur.fetchone()
  return LogsList

def getLog(val):
  res = db.SubList("Logs", "ID", val)
  for row in res:
    if row is not None:
      Log = Logs.Logs( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]) )
  return Log
=======
import db, import_file
Logs = import_file.import_file('Logs')

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
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
