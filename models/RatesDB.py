import db, import_file
Rates = import_file.import_file('Rates')

def getRates():
  res = db.List("Rates")
  RatesList = []
  for row in res:
    if row is not None:
      Rate = Rates.Rates( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), str(row[15]), )
      RatesList.append(Rate)
      row = cur.fetchone()
  return RatesList

def getRate(val):
  res = db.SubList("Rates", "ID", val)
  for row in res:
    if row is not None:
      Rate = Rates.Rates( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), str(row[15]) )
  return Rate

def getPayrollRate(val):
  res = db.SubList("Rates", "DetachID", val)
  RateArray = []
  for row in res:
    if row is not None:
      Rate = Rates.Rates( int(row[0]), int(row[1]), str(row[2]), str(row[3]), str(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), str(row[15]) )
      RateArray.append(Rate)
  return RateArray