<<<<<<< HEAD
import db, import_file
IncentiveMOR = import_file.import_file('IncentiveMOR')

def getAllIncentiveMOR():
  res = db.List("IncentiveMOR")
  IncentiveMORList = []
  for row in res:
    if row is not None:
      IncentiveMOR = IncentiveMOR.IncentiveMOR( str(row[0]), str(row[1]) )
      IncentiveMOR.append(IncentiveMOR)
      row = db.cur.fetchone()
  return IncentiveMORList

def getIncentiveMOR(val):
  res = db.SubList("IncentiveMOR", "ID", val)
  for row in res:
    if row is not None:
      IncentiveMOR = IncentiveMOR.IncentiveMOR( str(row[0]), str(row[1]) )
  return IncentiveMOR
=======
import db, import_file
IncentiveMOR = import_file.import_file('IncentiveMOR')

def getAllIncentiveMOR():
  res = db.List("IncentiveMOR")
  IncentiveMORList = []
  for row in res:
    if row is not None:
      IncentiveMOR = IncentiveMOR.IncentiveMOR( str(row[0]), str(row[1]) )
      IncentiveMOR.append(IncentiveMOR)
      row = cur.fetchone()
  return IncentiveMORList

def getIncentiveMOR(val):
  res = db.SubList("IncentiveMOR", "ID", val)
  for row in res:
    if row is not None:
      IncentiveMOR = IncentiveMOR.IncentiveMOR( str(row[0]), str(row[1]) )
  return IncentiveMOR
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
