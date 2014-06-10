<<<<<<< HEAD
import db, import_file
PersonalPayables = import_file.import_file('PersonalPayables')

def getPersonalPayables():
  res = db.List("PersonalPayables")
  PersonalPayablesList = []
  for row in res:
    if row is not None:
      PersonalPayable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]) )
      PersonalPayablesList.append(PersonalPayable)
      row = db.cur.fetchone()
  return PersonalPayables

def getPayrollRecord(val):
  res = db.SubList("PersonalPayables", "ID", val)
  for row in res:
    if row is not None:
      PersonalPayable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]) )
  return PersonalPayables
=======
import db, import_file
PersonalPayables = import_file.import_file('PersonalPayables')

def getPersonalPayables():
  res = db.List("PersonalPayables")
  PersonalPayablesList = []
  for row in res:
    if row is not None:
      PersonalPayable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]) )
      PersonalPayablesList.append(PersonalPayable)
      row = cur.fetchone()
  return PersonalPayables

def getPayrollRecord(val):
  res = db.SubList("PersonalPayables", "ID", val)
  for row in res:
    if row is not None:
      PersonalPayable = PersonalPayables.PersonalPayables( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]) )
  return PersonalPayables
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
