import db, import_file
AuthorizedManHours = import_file.import_file('AuthorizedManHours')

def getAuthorizedManHours():
  res = db.List("AuthorizedManHours")
  AuthorizedManHoursList = []
  for row in res:
    if row is not None:
      AuthorizedManHours = AuthorizedManHours.AuthorizedManHours( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), str(row[5]) )
      AuthorizedManHoursList.append(AuthorizedManHours)
      row = cur.fetchone()
  return AuthorizedManHoursList

def getAuthorizedManHour(val):
  res = db.SubList("AuthorizedManHours", "ID", val)
  for row in res:
    if row is not None:
      AuthorizedManHours = AuthorizedManHours.AuthorizedManHours( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), str(row[5]) )
  return Allowance
