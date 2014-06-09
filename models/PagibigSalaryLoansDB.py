import db, PagibigSalaryLoans, cgi, cgitb; cgitb.enable()

def getAllPagibigSalaryLoans():
  res = db.List("PagibigSalaryLoans")
  PagibigSalaryLoansList = []
  for row in res:
    if row is not None:
      PagibigSalaryLoan = PagibigSalaryLoans.PagibigSalaryLoans( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), str(row[5]) )
      PagibigSalaryLoansList.append(PagibigSalaryLoan)
      row = cur.fetchone()
  return PagibigCalamityLoansList

def getPagibigSalaryLoan(val):
  res = db.SubList("PagibigSalaryLoans", "ID", val)
  for row in res:
    if row is not None:
      PagibigSalaryLoans = PagibigSalaryLoans.PagibigSalaryLoans( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), str(row[5]) )
  return PagibigSalaryLoans
