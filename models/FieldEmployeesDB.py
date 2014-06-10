<<<<<<< HEAD
import db, import_file
FieldEmployees = import_file.import_file('FieldEmployees')


def getAllFieldEmployees():
  res = db.List("FieldEmployees")
  FieldEmployeesList = []
  for row in res:
    if row is not None:
      FieldEmployee = FieldEmployees.FieldEmployees( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), int(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]), str(row[19]), str(row[20]) )
      FieldEmployeesList.append(FieldEmployees)
      row = db.cur.fetchone()
  return FieldEmployeesList

def getFieldEmployee(val):
  res = db.SubList("FieldEmployees", "Username", val)
  print db.SubList("FieldEmployees", "Username", val)
  for row in res:
    if row is not None:
      FieldEmployee = FieldEmployees.FieldEmployees( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), int(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]), str(row[19]), str(row[20]) )
  return FieldEmployees
=======
import db, import_file
FieldEmployees = import_file.import_file('FieldEmployees')

#OK
def getAllFieldEmployees():
  res = db.List("FieldEmployees")
  FieldEmployeesList = []
  for row in res:
    if row is not None:
      FieldEmployee = FieldEmployees.FieldEmployees( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), int(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]), str(row[19]), str(row[20]) )
      FieldEmployeesList.append(FieldEmployee)
      row = db.cur.fetchone()
  return FieldEmployeesList

#OK
def getFieldEmployee(val):
  res = db.SubList("FieldEmployees", "ID", val)
  for row in res:
    if row is not None:
      FieldEmployee = FieldEmployees.FieldEmployees( str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]), str(row[7]), str(row[8]), str(row[9]), str(row[10]), str(row[11]), str(row[12]), str(row[13]), int(row[14]), str(row[15]), str(row[16]), str(row[17]), str(row[18]), str(row[19]), str(row[20]) )
  return FieldEmployee
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
