import db

    
class PagibigCalamityLoans(object):
  def __init__(self, ID, FieldEmpID, Amount, MonthlyPay, Balance, DateCreated):
        self.ID=ID
        self.FieldEmpID=FieldEmpID
        self.Amount=Amount
        self.MonthlyPay=MonthlyPay
        self.Balance=Balance
        self.DateCreated=DateCreated
        self.FieldEmpName='name'
        
  def setFEName(self, val):
    self.FieldEmpName = db.getFEName(val)           
    
  def save(self):
    sql = "insert into PagibigCalamityLoans (FieldEmpID, Amount, MonthlyPay, Balance, Status) values (%s, %s, %s, %s, %s)"
    params = (self.FieldEmpID, self.Amount, self.MonthlyPay, self.Balance, self.Status)
    db.ins(sql,params)
    
  def get(prop):
    sql = "select %s from PagibigCalamityLoans where ID=%s"
    params =(prop, self.ID)
    return db.getOne(sql, params)
    
  def set(prop, val):
    sql = "update PagibigCalamityLoans set %s=%s where ID = %s"
    params =(prop, val, self.ID)
    return db.set(sql,params)

