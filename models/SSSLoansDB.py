import import_file
db = import_file.import_file('db')
SSSLoans = import_file.import_file('SSSLoans')

def getAllSSSLoans():
  res = db.List("SSSLoans")
  SSSLoansList = []
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
      SSSLoansList.append(SSSLoan)
      row = db.cur.fetchone()
  return SSSLoansList

def getSSSLoan(val):
  res = db.SubList("SSSLoans", "ID", val)
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) )
  return SSSLoans

def addSSSLoan(FieldEmpID, Amount, MonthlyPay):
  sql = "CALL addSSSLoan( %s, %s, %s)"
  params = (FieldEmpID, Amount, MonthlyPay)
  try:
    db.cur.execute(sql, params)
    db.mysql.commit()
  except:
    print 'Error saving client'

def deleteSSSLoan(ID):
  db.delete("SSSLoans", ID)
  db.mysql.commit()