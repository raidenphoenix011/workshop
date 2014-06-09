import db, Receivables, cgi, cgitb; cgitb.enable()

def getReceivables():
  res = db.List("Receivables")
  ReceivablesList = []
  for row in res:
    if row is not None:
      Receivable = Receivables.Receivables( str(row[0]), str(row[1]) )
      ReceivablesList.append(Receivable)
      row = cur.fetchone()
  return ReceivablesList

def getReceivable(val):
  res = db.SubList("Receivables", "ID", val)
  for row in res:
    if row is not None:
      Receivable = Receivables.Receivables( str(row[0]), str(row[1]) )
  return Receivables
