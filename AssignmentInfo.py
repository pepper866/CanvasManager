class AssignmentInfo:
  def __init__(self, row):
    self.name = row[0]
    self.title = row[1]
    self.due_date = row[2]
    self.type = row[3]
    self.details = row[4]
    self.submission_types = row[5]
    self.extensions = row[6]
    self.points = row[7]

  def addData(self, row):
    self.name = row[0]
    self.title = row[1]
    self.due_date = row[2]
    self.type = row[3]
    self.details = row[4]
    self.submission_types = row[5]
    self.extensions = row[6]
    self.points = row[7]