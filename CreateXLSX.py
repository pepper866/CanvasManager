import xlsxwriter
from datetime import timedelta
from datetime import datetime
from GuiHelpers import daterange
from GuiHelpers import getDay

# Given start of semester, days of week class meets, and special days off (breaks and other days) 
# create the schedule template as xlsx file so prof can start planning
def createXLSX(name, first_day, last_day, meeting_days, user_days_off, recurringDays):

  # change meeting days to ints so it works with our code
  meeting_days = list(map(int, meeting_days))

  # create variable to keep track of first day of week
  first_of_week = meeting_days[0]

  # create dictionary to hold Professor's days off
  days_off = {}

  # add all of the professors day off to our dictionary
  for d in user_days_off:
    d = datetime.strptime(d, "%m/%d/%y").date()
    days_off[d] = "[reason for day off]"

  # create array to hold xlsx data
  data = []

  # index to track which day we are on in the list
  # add one every time a valid row is added (i.e. a row with a class day)
  index = 1

  # counter for which week # we are in
  week_num = 1

  # create headers for the columns
  data.append(["Week", "Class", "Date", "Day", "Topic", "Assignment", "Notes"])

  # iterate though each day of the semester
  for single_date in daterange(first_day, last_day + timedelta(days=1)):
    # create array to hold data for current date
    data_row = []

    # get weekday as integer
    day = single_date.weekday()

    # check : 1) if current date is one of the meeting days
    #         2) if current date is Saturday (5) or Sunday (6)
    if (day in meeting_days and day != 5 and day != 6):
      #if this is a valid day, add a row to our xlsx file
      data_row = [
        "", index, str(single_date),
        getDay(day), "[topic]", "[assignment]", "[notes]"
      ]

      # if this is the first day, print the week number
      # or if it's a Monday and not the first day, print the week number
      if single_date == first_day or (day == first_of_week and single_date != first_day):
        data_row[0] = week_num
        week_num += 1

      # if the current day is one of the days off, keep the row
      # but print reason for day off in the topic column (data_row[4])
      if single_date in days_off:
        data_row[4] = "NO CLASS - " + days_off[single_date]
       
      # if the current day is a recurring day, 
      # print the recurring day reason in the notes column (data_row[6]) 
      if day in recurringDays:
        data_row[6] = recurringDays[day]

      # add row to our xlsx array
      data.append(data_row)
      index += 1

    # add one blank row if we get to a weekend (i.e. we get to Friday)
    if day == 4:
      data.append([])

  # generate xlsx to hold data
  workbook = xlsxwriter.Workbook(name + '.xlsx')
  worksheet = workbook.add_worksheet()
  
  # write all of our data to the xlsx file
  for row_num, row_data in enumerate(data):
    for col_num, col_data in enumerate(row_data):
      worksheet.write(row_num, col_num, col_data)

  # generate second worksheet for assignments
  worksheet2 = workbook.add_worksheet("Assignments")

  #create list of headers for our second tab
  assignData = ["key", "Name", "Due Date", "Type", "Details", "Submission", 
                     "File Extension", "Points", "Group"]

  # write the headers to our Assignments tab
  worksheet2.write_row(0, 0, assignData)

  workbook.close()
