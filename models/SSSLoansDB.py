import db, SSSLoans, cgi, cgitb; cgitb.enable()

def getAllSSSLoans():
  res = db.List("SSSLoans")
  SSSLoansList = []
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( str(row[0]), str(row[1]) )
      SSSLoansList.append(SSSLoan)
      row = cur.fetchone()
  return SSSLoansList

def getSSSLoan(val):
  res = db.SubList("SSSLoans", "ID", val)
  for row in res:
    if row is not None:
      SSSLoan = SSSLoans.SSSLoans( str(row[0]), str(row[1]) )
  return SSSLoans
