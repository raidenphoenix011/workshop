import db

    
class PayrollRecord(object):
  def __init__(self, MHLogID, Regular, Overtime, NDifferential, ECOLA, LegalHoliday, SpecialHoliday, Allowance, SSSCon,SSSLoan, CalamityLoan, SalaryLoan, CholFee, FileFee, NetPays):
        
        self.MHLogID=MHLogID 
        self.Regular=Regular
        self.Overtime=Overtime
        self.NDifferential=NDifferential
        self.ECOLA=ECOLA        
        self.LegalHoliday=LegalHoliday
        self.SpecialHoliday=SpecialHoliday
        self.Allowance=Allowance

        self.SSSCon=SSSCon
        self.SSSLoan=SSSLoan
        self.CalamityLoan=CalamityLoan
        self.SalaryLoan=SalaryLoan    
        self.Cashbond= 100
        self.UniformDepo= 175
        self.CholFee=CholFee
        self.FileFee=FileFee

        self.NetPays=NetPays


  def get(prop):
    sql = "select %s from PayrollRecord where ID=%s"
    params =(prop, self.ID)
    return db.getOne(sql, params)
    
  def set(prop, val):
    sql = "update PayrollRecord set %s=%s where ID = %s"
    params =(prop, val, self.ID)
    return db.set(sql,params)
