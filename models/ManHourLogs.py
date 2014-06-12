import db

class ManHourLogs(object):
    
    def __init__(self, ID, DetachID, FieldEmpID, NoOfFullDays, NightHours, RegHours, OTHours, LegHolidayHours, SpeHolidayHours, DateCreated, StartDate, EndDate, PeriodCode):
        self.ID = ID
        self.DetachID = DetachID
        self.FieldEmpID = FieldEmpID
        self.NoOfFullDays = NoOfFullDays
        self.NightHours = NightHours
        self.RegHours = RegHours
        self.OTHours = OTHours
        self.LegHolidayHours = LegHolidayHours
        self.SpeHolidayHours = SpeHolidayHours
        self.DateCreated = DateCreated
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.PeriodCode = PeriodCode
        
    
    def save(self):
        sql = "insert into ManHourLogs (ID, DetachID, FieldEmpID, NoOfFullDays, NightHours, RegHours, OTHours, LegHolidayHours, SpeHolidayHours, DateCreated, PeriodCode) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        params = (self.ID, self.DetachID, self.FieldEmpID, self.NoOfFullDays, self.NightHours, self.RegHours, self.OTHours, self.LegHolidayHours, self.SpeHolidayHours, self.DateCreated, self.PeriodCode)
        return db.ins(sql, params)
    
    def get(prop):
        sql = "select %s from ManHourLogs where ID = %s"
        params = (prop, self.ID)
        return db.getOne(sql, params)
    
    def set(prop, val):
        sql = "update ManHourLogs set %s = %s where ID = %s"
        params = (prop, val, self.ID)
        return db.set(sql, params)