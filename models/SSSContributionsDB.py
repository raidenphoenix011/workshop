<<<<<<< HEAD
import db, import_file
SSSContributions = import_file.import_file('SSSContributions')

def getSSSContributions():
  res = db.List("SSSContributions")
  SSSContributionsList = []
  for row in res:
    if row is not None:
      SSSContribution = SSSContributions.SSSContributions( str(row[0]), str(row[1]) )
      SSSContributionsList.append(SSSContribution)
      row = db.cur.fetchone()
  return SSSContributionsList

def getSSSContribution(val):
  res = db.SubList("SSSContributions", "ID", val)
  for row in res:
    if row is not None:
      SSSContribution = SSSContributions.SSSContributions( str(row[0]), str(row[1]) )
  return SSSContributions
=======
import db, import_file
SSSContributions = import_file.import_file('SSSContributions')

def getSSSContributions():
  res = db.List("SSSContributions")
  SSSContributionsList = []
  for row in res:
    if row is not None:
      SSSContribution = SSSContributions.SSSContributions( str(row[0]), str(row[1]) )
      SSSContributionsList.append(SSSContribution)
      row = cur.fetchone()
  return SSSContributionsList

def getSSSContribution(val):
  res = db.SubList("SSSContributions", "ID", val)
  for row in res:
    if row is not None:
      SSSContribution = SSSContributions.SSSContributions( str(row[0]), str(row[1]) )
  return SSSContributions
>>>>>>> c9e5dac83acf4b96337960900277a7a396e23b87
