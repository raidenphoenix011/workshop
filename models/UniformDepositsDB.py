<<<<<<< HEAD
import db, import_file
UniformDeposits = import_file.import_file('UniformDeposits')

def getUniformDeposits():
  res = db.List("UniformDeposits")
  UniformDepositsList = []
  for row in res:
    if row is not None:
      UniformDeposit = UniformDeposits.UniformDeposits( str(row[0]), str(row[1]) )
      UniformDepositsList.append(UniformDeposit)
      row = db.cur.fetchone()
  return UniformDepositsList

def getUniformDeposit(val):
  res = db.SubList("UniformDeposits", "ID", val)
  for row in res:
    if row is not None:
      UniformDeposit = UniformDeposits.UniformDeposits( str(row[0]), str(row[1]) )
  return UniformDeposit
=======
import db, import_file
UniformDeposits = import_file.import_file('UniformDeposits')

def getUniformDeposits():
  res = db.List("UniformDeposits")
  UniformDepositsList = []
  for row in res:
    if row is not None:
      UniformDeposit = UniformDeposits.UniformDeposits( str(row[0]), str(row[1]) )
      UniformDepositsList.append(UniformDeposit)
      row = cur.fetchone()
  return UniformDepositsList

def getUniformDeposit(val):
  res = db.SubList("UniformDeposits", "ID", val)
  for row in res:
    if row is not None:
      UniformDeposit = UniformDeposits.UniformDeposits( str(row[0]), str(row[1]) )
  return UniformDeposit
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
