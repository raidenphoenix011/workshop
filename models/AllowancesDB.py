<<<<<<< HEAD
import db, import_file
Allowances = import_file.import_file('Allowances')

def getAllowances():
  res = db.List("Allowances")
  AllowancesList = []
  for row in res:
    if row is not None:
      Allowance = Allowances.Allowances( int(row[0]), int(row[1]), int(row[2]), int(row[3]), str(row[4]), str(row[5]) )
      AllowancesList.append(Allowance)
      row = db.cur.fetchone()
  return AllowancesList

def getAllowance(val):
  res = db.SubList("Allowances", "ID", val)
  for row in res:
    if row is not None:
      Allowance = Allowances.Allowances( int(row[0]), int(row[1]), int(row[2]), int(row[3]), str(row[4]), str(row[5]) )
  return Allowance
=======
import db, import_file
Allowances = import_file.import_file('Allowances')

def getAllowances():
  res = db.List("Allowances")
  AllowancesList = []
  for row in res:
    if row is not None:
      Allowance = Allowances.Allowances( int(row[0]), int(row[1]), int(row[2]), int(row[3]), str(row[4]), str(row[5]) )
      AllowancesList.append(Allowance)
      row = cur.fetchone()
  return AllowancesList

def getAllowance(val):
  res = db.SubList("Allowances", "ID", val)
  for row in res:
    if row is not None:
      Allowance = Allowances.Allowances( int(row[0]), int(row[1]), int(row[2]), int(row[3]), str(row[4]), str(row[5]) )
  return Allowance
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
