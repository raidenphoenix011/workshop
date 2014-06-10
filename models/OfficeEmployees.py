import db
    
class OfficeEmployees(object):
  def __init__(self, ID, Type, Username, Password, Suffix, LastName, FirstName, MiddleName, Landline, MobileNo, Address, BirthDate, Gender, CivilStatus, Dependents, Position, DateHired, DateResigned, EmpStatus):

        self.ID=ID
        self.Type=Type
        self.Username=Username
        self.Password=Password
        self.Suffix=Suffix
        self.LastName=LastName
        self.FirstName=FirstName
        self.MiddleName=MiddleName
        self.Landline=Landline
        self.MobileNo=MobileNo
        self.Address=Address
        self.BirthDate=BirthDate
        self.Gender=Gender
        self.CivilStatus=CivilStatus
        self.Dependents=Dependents
        self.Position=Position
        self.DateHired=DateHired
        self.DateResigned=DateResigned
        self.EmpStatus=EmpStatus
