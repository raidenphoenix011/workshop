import db, import_file
PagibigCalamityLoans = import_file.import_file('PagibigCalamityLoans')

def getAllPagibigCalamityLoans():
  res = db.List("PagibigCalamityLoans")
  PagibigCalamityLoansList = []
  for row in res:
    if row is not None:
      PagibigCalamityLoan = PagibigCalamityLoans.PagibigCalamityLoans( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), str(row[5]) )
      PagibigCalamityLoansList.append(PagibigCalamityLoan)
      row = db.cur.fetchone()
  return PagibigCalamityLoansList

def getOfficeEmployeeType(val):
  res = db.SubList("PagibigCalamityLoan", "ID", val)
  for row in res:
    if row is not None:
      PagibigCalamityLoan = PagibigCalamityLoans.PagibigCalamityLoans( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), str(row[5]) )
  return PagibigCalamityLoan
