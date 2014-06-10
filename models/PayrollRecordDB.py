import db, import_file
PayrollRecord = import_file.import_file('PayrollRecord')

def getPayrollRecords():
  res = db.List("PayrollRecord")
  PayrollRecordList = []
  for row in res:
    if row is not None:
      PayrollRecord = PayrollRecord.PayrollRecord( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]) )
      PayrollRecordList.append(PayrollRecord)
      row = db.cur.fetchone()
  return PayrollRecordList

def getPayrollRecord(val):
  res = db.SubList("PayrollRecord", "ID", val)
  for row in res:
    if row is not None:
      PayrollRecord = PayrollRecord.PayrollRecord( int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]) )
  return PayrollRecord
