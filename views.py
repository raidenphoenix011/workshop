#!/usr/bin/env python
# -*- coding: latin-1 -*-

from flask import Flask, flash, render_template, session, escape, request, redirect, url_for
import db, hashlib
import import_file, logging

Allowances = import_file.import_file('models/Allowances.py')
AuthorizedManHours = import_file.import_file('models/AuthorizedManHours.py')
ClientContactPersons = import_file.import_file('models/ClientContactPersons.py')
Clients = import_file.import_file('models/Clients.py')
DetachmentContactPersons = import_file.import_file('models/DetachmentContactPersons.py')
Detachments = import_file.import_file('models/Detachments.py')
FieldEmployees = import_file.import_file('models/FieldEmployees.py')
FieldEmployeeTypes = import_file.import_file('models/FieldEmployeeTypes.py')
HolidayMOR = import_file.import_file('models/HolidayMOR.py')
IncentiveMOR = import_file.import_file('models/IncentiveMOR.py')
Logs = import_file.import_file('models/Logs.py')
ManHourLogs = import_file.import_file('models/ManHourLogs.py')
OfficeEmployees = import_file.import_file('models/OfficeEmployees.py')
OfficeEmployeeTypes = import_file.import_file('models/OfficeEmployeeTypes.py')
PagibigCalamityLoans = import_file.import_file('models/PagibigCalamityLoans.py')
PagibigSalaryLoans = import_file.import_file('models/PagibigSalaryLoans.py')
PayrollRecord = import_file.import_file('models/PayrollRecord.py')
PersonalPayables = import_file.import_file('models/PersonalPayables.py')
Rates = import_file.import_file('models/Rates.py')
RateTypes = import_file.import_file('models/RateTypes.py')
Receivables = import_file.import_file('models/Receivables.py')
SSSContributions = import_file.import_file('models/SSSContributions.py')
SSSLoans = import_file.import_file('models/SSSLoans.py')
UniformDeposits = import_file.import_file('models/UniformDeposits.py')


AllowancesDB = import_file.import_file('models/AllowancesDB')
AuthorizedManHoursDB = import_file.import_file('models/AuthorizedManHoursDB')
ClientsDB = import_file.import_file('models/ClientsDB')
ClientContactPersonsDB = import_file.import_file('models/ClientContactPersonsDB')
DetachmentContactPersonsDB = import_file.import_file('models/DetachmentContactPersonsDB')
DetachmentsDB = import_file.import_file('models/DetachmentsDB')
FieldEmployeesDB = import_file.import_file('models/FieldEmployeesDB')
FieldEmployeeTypesDB = import_file.import_file('models/FieldEmployeeTypesDB')
HolidayMORDB = import_file.import_file('models/HolidayMORDB')
IncentiveMORDB = import_file.import_file('models/IncentiveMORDB')
LogsDB = import_file.import_file('models/LogsDB')
ManHourLogsDB = import_file.import_file('models/ManHourLogsDB')
OfficeEmployeesDB = import_file.import_file('models/OfficeEmployeesDB')
OfficeEmployeeTypesDB = import_file.import_file('models/OfficeEmployeeTypesDB')
PagibigCalamityLoansDB = import_file.import_file('models/PagibigCalamityLoansDB')
PagibigSalaryLoansDB = import_file.import_file('models/PagibigSalaryLoansDB')
PayrollRecordDB = import_file.import_file('models/PayrollRecordDB')
PersonalPayablesDB = import_file.import_file('models/PersonalPayablesDB')
RatesDB = import_file.import_file('models/RatesDB')
RateTypeDB = import_file.import_file('models/RateTypesDB')
ReceivablesDB = import_file.import_file('models/ReceivablesDB')
SSSContributionsDB = import_file.import_file('models/SSSContributionsDB')
SSSLoansDB = import_file.import_file('models/SSSLoansDB')
UniformDepositsDB = import_file.import_file('models/UniformDepositsDB')


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def root():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():

  if 'usertype' in session:
    if session['usertype'] == 'ADM':
        return redirect(url_for('admin'))
    elif session['usertype'] == 'HR':
        return redirect(url_for('listEmployees'))
    elif session['usertype'] == 'BiO':
        return redirect(url_for('listClients'))   
    elif session['usertype'] == 'MO':
        return redirect(url_for('listDetachmentsManhour'))
    elif session['usertype'] == 'PrO':
        return redirect(url_for('listDetachmentsPayroll'))
    
    #----TO BE ADDED -----
    elif session['usertype'] == 'PyO':
        return redirect(url_for('listDetachmentsPayables'))
    elif session['usertype'] == 'BeO':
        return redirect(url_for('viewPeriodsBenefits'))
    elif session['usertype'] == 'RO':
        return redirect(url_for('viewPeriodsBenefits'))
    elif session['usertype'] == 'DO':
        return redirect(url_for('viewPeriodsBenefits'))

  elif request.method == 'POST':
    if OfficeEmployeesDB.login(request.form['username'], request.form['password']):
      session['usertype'] = OfficeEmployeesDB.getOfficeEmployee(request.form['username']).Type
      session['user'] = request.form['username']
      return redirect(url_for('login'))
    else:
      flash('Please check your login credentials')
      return redirect(url_for('login'))
  else:
    return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('user', None)
  session.pop('usertype', None)
  flash('Successfully logged out')
  return redirect(url_for('login'))

@app.route('/admin', methods=['POST', 'GET'])
def admin(user=None):
  if 'usertype' in session:
    if session['usertype'] != 'ADM':
      flash('Unauthorized access')
      return redirect(url_for('logout'))
    return render_template('admin.html', OEs = OfficeEmployeesDB.getOfficeEmployees(), user=escape(session['user']))

@app.route('/employees', methods=['POST', 'GET'])
def listEmployees(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'HR' or session['usertype'] == 'ADM':
      return render_template('employee_search.html', FEs = FieldEmployeesDB.getAllFieldEmployees(), user=escape(session['user']))
    else:
      flash('Unauthorized user access')
      return redirect(url_for('logout'))
  
@app.route('/employees/get/<ID>', methods=['POST', 'GET'])
def viewEmployee(ID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'HR' or session['usertype'] == 'ADM':
      return render_template('employee.html', FE = FieldEmployeesDB.getFieldEmployee(ID), user=escape(session['user']), )
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/employees/add', methods=['POST', 'GET'])
def addFieldEmployee(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'HR' or session['usertype'] == 'ADM':
      return render_template('employee_blank.html', user=escape(session['user']), )
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))
  
@app.route('/clients', methods=['POST', 'GET'])
def listClients(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      return render_template('client_search.html', goto='listDetachments', CLs=ClientsDB.getAllClients(), user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/get/<ID>', methods=['POST', 'GET'])
def viewClient(ID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      return render_template('client_view.html', Client = ClientsDB.getClient(ID), Detachments = DetachmentsDB.getAllDetachmentsbyID(ID), ContactPersons = ClientContactPersonsDB.getClientContactPersons(ID), user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/get/<ID>/edit/', methods=['POST', 'GET'])
def editClient(ID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        return render_template('client_edit.html', Client=ClientsDB.getClient(ID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/save', methods=['POST', 'GET'])
def updateClient(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        client = Clients.Clients(request.form['client_id'], request.form['client_code'], request.form['client_name'], request.form['client_address'], request.form['client_city'], request.form['client_landline'])
        ClientsDB.saveClient(client)
        flash('Client record successfully updated.')
        return redirect(url_for('viewClient', ID=client.ID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/add', methods=['POST', 'GET'])
def addClient(user=None): 
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      return render_template('client_add.html', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/insert', methods=['POST', 'GET'])
def insertClient(user=None): 
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        client = Clients.Clients('0', '0', request.form['client_name'], request.form['client_address'], request.form['client_city'], request.form['client_landline'])
        ClientsDB.insertClient(client)
        clientID = ClientsDB.getClientID(client.Name)
        flash('Client successfully added.')
        return redirect(url_for('viewClient', ID=clientID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))


# CLIENT CONTACT PERSONS -------------------------

@app.route('/clients/get/<ID>/contacts/get/<ContactID>/edit', methods=['POST', 'GET'])
def editClientContact(ID, ContactID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        Client=ClientsDB.getClient(ID)
        Contact=ClientContactPersonsDB.getClientContactPerson(ContactID)
        return render_template('client_contact_edit.html', Client=Client, Contact=Contact)
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/contacts/update', methods=['POST', 'GET'])
def updateClientContact(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        if request.form['birthdate']:
            birthdate = request.form['birthdate']
        else:
            birthdate = '0000-00-00'
        contact = ClientContactPersons.ClientContactPersons(request.form['id'], request.form['clientid'], request.form['suffix'], request.form['lastname'], request.form['firstname'], request.form['middlename'], request.form['landline'], request.form['mobile'], birthdate)
        ClientContactPersonsDB.updateContact(contact)
        flash('Contact information successfully updated.')
        return redirect(url_for('viewClient', ID=contact.ClientID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/get/<ClientID>/contacts/add', methods=['POST', 'GET'])
def addClientContact(ClientID, user=None): 
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      return render_template('client_contact_add.html', Client = ClientsDB.getClient(ClientID), user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/get/contacts/insert', methods=['POST', 'GET'])
def insertClientContact(user=None): 
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      if request.form['birthdate']:
        birthdate = request.form['birthdate']
      else:
        birthdate = '0000-00-00'
      contact = ClientContactPersons.ClientContactPersons('0', request.form['clientid'], request.form['suffix'], request.form['lastname'], request.form['firstname'], request.form['middlename'], request.form['landline'], request.form['mobile'], birthdate)
      ClientContactPersonsDB.insertContact(contact)
      clientID = contact.ClientID
      flash('Contact successfully added.')
      return redirect(url_for('viewClient', ID=clientID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/get/<ID>/contacts/<ContactID>/delete', methods=['POST', 'GET'])
def deleteClientContact(ID, ContactID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      ClientContactPersonsDB.deleteContact(ContactID)
      flash('Contact Person successfully deleted.')
      return redirect(url_for('viewClient', ID=ID))

@app.route('/detachments/lists/', methods=['POST', 'GET'])
def listDetachments(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'ADM' or session['usertype'] == 'BiO':
      listDE = DetachmentsDB.getAllDetachments()
      for DE in listDE:
        DE.setClientName(DE.ClientID)
      return render_template('detachment_search.html', DEs = listDE, user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/detachments/get/<ID>', methods=['POST', 'GET'])
def viewDetachment(ID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      DE = DetachmentsDB.getDetachment(ID)
      ClientID = DE.ClientID
      Client = ClientsDB.getClient(ClientID)
      return render_template('detachment_view.html', DE = DE, Client = Client, ContactPersons = DetachmentContactPersonsDB.getDetachmentContactPersons(ID), user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/detachments/get/<DetachID>/contacts/get/<ContactID>/edit', methods=['POST', 'GET'])
def editDetachmentContact(DetachID, ContactID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        Detachment=DetachmentsDB.getDetachment(DetachID)
        Contact=DetachmentContactPersonsDB.getDetachmentContactPerson(ContactID)
        return render_template('detachment_contact_edit.html', Detachment=Detachment, Contact=Contact)
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/detachments/contacts/update', methods=['POST', 'GET'])
def updateDetachmentContact(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        if request.form['birthdate']:
            birthdate = request.form['birthdate']
        else:
            birthdate = '0000-00-00'
        contact = DetachmentContactPersons.DetachmentContactPersons(request.form['id'], request.form['detachid'], request.form['suffix'], request.form['lastname'], request.form['firstname'], request.form['middlename'], request.form['landline'], request.form['mobile'], birthdate)
        DetachmentContactPersonsDB.updateContact(contact)
        flash('Contact information successfully updated.')
        return redirect(url_for('viewDetachment', ID=contact.DetachID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/detachments/get/<ID>/contacts/<ContactID>/delete', methods=['POST', 'GET'])
def deleteDetachmentContact(ID, ContactID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      DetachmentContactPersonsDB.deleteContact(ContactID)
      flash('Contact Person successfully deleted.')
      return redirect(url_for('viewDetachment', ID=ID))

@app.route('/clients/get/<ID>/detachments/add/', methods=['POST', 'GET'])
def addDetachment(ID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        Client = ClientsDB.getClient(ID)
        return render_template('detachment_add.html', user=escape(session['user']), Client=Client)
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/get/<ID>/detachments/insert', methods=['POST', 'GET'])
def insertDetachment(ID, user=None): 
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        if request.form['start']:
            start = request.form['start']
        else:
            start = '0000-00-00'
        detachment = Detachments.Detachments('0', ID, '1', '0', request.form['name'], request.form['address'], request.form['city'], start, '0000-00-00', request.form['status'])
        DetachmentsDB.insertDetachment(detachment)
        ID = DetachmentsDB.getDetachmentID(detachment.Name)
        flash('Detachment successfully added.')
        return redirect(url_for('viewDetachment', ID=ID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/clients/<ClientID>/detachments/get/<DetachID>/edit', methods=['POST', 'GET'])
def editDetachment(ClientID, DetachID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        Client=ClientsDB.getClient(ClientID)
        Detachment=DetachmentsDB.getDetachment(DetachID)
        return render_template('detachment_edit.html', Client=Client, Detachment=Detachment)
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))    

@app.route('/detachments/update', methods=['POST', 'GET'])
def updateDetachment(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
        if request.form['end_date']:
          enddate = request.form['end_date']
        else:
          enddate = '0000-00-00'
        detachment = Detachments.Detachments(request.form['ID'], request.form['client_ID'], '1', request.form['code'], request.form['name'], request.form['address'], request.form['city'], request.form['start_date'], enddate, request.form['status'] )
        DetachmentsDB.updateDetachment(detachment)
        flash('Detachment information successfully updated.')
        return redirect(url_for('viewDetachment', ID=detachment.ID))
    else:
        flash('Unauthorized access')
        return redirect(url_for('logout'))
    
@app.route('/detachments/get/<DetachID>/contacts/add', methods=['POST', 'GET'])
def addDetachmentContact(DetachID, user=None): 
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      return render_template('detachment_contact_add.html', Detachment = DetachmentsDB.getDetachment(DetachID), user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/detachments/contacts/insert', methods=['POST', 'GET'])
def insertDetachmentContact(user=None): 
  if 'usertype' in session:
    if session['usertype'] == 'BiO' or session['usertype'] == 'ADM':
      if request.form['birthdate']:
        birthdate = request.form['birthdate']
      else:
        birthdate = '0000-00-00'
      contact = DetachmentContactPersons.DetachmentContactPersons('0', request.form['detachid'], request.form['suffix'], request.form['lastname'], request.form['firstname'], request.form['middlename'], request.form['landline'], request.form['mobile'], birthdate)
      DetachmentContactPersonsDB.insertContact(contact)
      detachID = contact.DetachID
      flash('Contact successfully added.')
      return redirect(url_for('viewDetachment', ID=detachID))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))
 
@app.route('/manhours/detachments/get/id/add', methods=['POST', 'GET'])
def addManhour(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'MO' or session['usertype'] == 'ADM':
      return render_template('detachment_search_manhour.html', user=escape(session['user']), navtitle='MANHOUR RECORDS', mode='manhour')
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/manhours/<ID>/<Code>', methods=['POST', 'GET'])
def manhour(ID, Code, user=None):
    if 'usertype' in session:
        if session['usertype'] == 'MO' or session['usertype'] == 'ADM':
            Detachment = DetachmentsDB.getDetachment(ID)
            Log=ManHourLogsDB.getLog2(ID, Code)
            Period = Log[0].PeriodCode
            return render_template('manhour.html', Log=Log, Detachment=Detachment, PeriodCode=Period, user=escape(session['user']), dept='manhour')
        else:
            flash('Unauthorized access')
            return redirect(url_for('logout'))

@app.route('/manhours/detachments', methods=['POST', 'GET'])
def listDetachmentsManhour(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'ADM' or session['usertype'] == 'MO':
      return render_template('detachment_search_manhour.html', DEs = DetachmentsDB.getAllDetachments(), user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/payroll/detachments', methods=['POST', 'GET'])
def listDetachmentsPayroll(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PrO' or session['usertype'] == 'ADM':
      return render_template('detachment_search_payroll.html', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))
 
@app.route('/detachments/<usertype>', methods=['POST', 'GET'])
def listDetachmentsAdmin(usertype, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PrO' or session['usertype'] == 'ADM' or session['usertype'] == 'BiO' or session['usertype'] == 'MO':
      if session['usertype'] =='BiO':
        return render_template('detachment_search.html', user=escape(session['user']),  goto='viewDetachment',navtitle='CLIENT RECORDS', mode='viewDetachment')
      elif session['usertype'] == 'PrO':
        return render_template('detachment_search.html', user=escape(session['user']), goto='payroll', navtitle='PAYROLL SYSTEM', mode='viewPeriods')
      elif session['usertype'] == 'MO':
        return render_template('detachment_search.html', user=escape(session['user']),  goto='manhour',navtitle='MANHOUR RECORDS', mode='viewPeriods')
      else:
        flash('Unauthorized access')
        return redirect(url_for('logout'))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/payroll/detachments/get', methods=['POST', 'GET'])
def viewPayroll(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PrO' or session['usertype'] == 'ADM':
      return render_template('payroll.html', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/manhours/detachments/get/<ID>/records', methods=['POST', 'GET'])
def viewPeriodsManhour(ID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'MO' or session['usertype'] == 'ADM':
      DE = DetachmentsDB.getDetachment(ID)
      MH = ManHourLogsDB.getLog(ID)
      return render_template('period_search_manhour.html', Detachment=DE, MH=MH, user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/payroll/detachments/get/<ID>/records', methods=['POST', 'GET'])
def viewPeriodsPayroll(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PrO' or session['usertype'] == 'ADM':
      return render_template('period_search_payroll.html', view='payroll', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/payroll/detachments/get/ID/records/Period', methods=['POST', 'GET'])
def viewPayrollRoster(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PrO' or session['usertype'] == 'ADM':
      return render_template('payroll_roster.html', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

#PAYABLES ----TO BE ADDED ------

@app.route('/payables/detachments', methods=['POST', 'GET'])
def listDetachmentsPayables(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PyO' or session['usertype'] == 'ADM':
      return render_template('detachment_search_payables.html', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/payables/detachments/get/ID/records', methods=['POST', 'GET'])
def viewPeriodsPayables(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PyO' or session['usertype'] == 'ADM':
      return render_template('period_search_payables.html', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/payables/detachments/get/id/period', methods=['POST', 'GET'])
def viewPayables(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'PyO' or session['usertype'] == 'ADM':
      return render_template('payables.html', user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

#BENEFITS ---TO BE ADDED -----

@app.route('/benefits/SSS', methods=['POST', 'GET'])
def viewLoansSSS(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BeO' or session['usertype'] == 'ADM':

#      listDE = db.getAllDetachments()
#      for DE in listDE:
#        DE.setClientName(DE.ClientID)
#      return render_template('detachment_search.html', DEs = listDE, user=escape(session['user']))
     listSSS = db.getAllSSSLoans()
     for SSS in listSSS:
        SSS.setFEName(SSS.FieldEmpID) 
        return render_template('loan_SSS.html', SSSs = listSSS, user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/benefits/SSS/<ID>', methods=['POST', 'GET'])
def deleteLoansSSS(ID, user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BeO' or session['usertype'] == 'ADM':
      return redirect(url_for('viewLoanSSS'))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))  

@app.route('/benefits/pagibig_calamity', methods=['POST', 'GET'])
def viewLoansCalamity(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BeO' or session['usertype'] == 'ADM':
       listPIC = db.getAllPagibigCalamityLoans()
       for PIC in listPIC:
        PIC.setFEName(PIC.FieldEmpID) 

        return render_template('loan_PagibigCalamity.html', PICs= listPIC, user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))

@app.route('/benefits/pagibig_salary', methods=['POST', 'GET'])
def viewLoansSalary(user=None):
  if 'usertype' in session:
    if session['usertype'] == 'BeO' or session['usertype'] == 'ADM':
      listPIS = db.getAllPagibigSalaryLoans()
      for PIS in listPIS:
        PIS.setFEName(PIS.FieldEmpID) 

        return render_template('loan_PagibigSalary.html', PISs=listPIS, user=escape(session['user']))
    else:
      flash('Unauthorized access')
      return redirect(url_for('logout'))
    
#@app.route('/benefits/deleteSSSLoan', methods=['POST', 'GET'])
#def deleteSSSloan(ID, user=None)
#    db.deleteSSSLoan(ID)
#    return redirect(url_for('viewLoanSSS'))

if __name__ == '__main__':
    app.debug = True
    app.run()