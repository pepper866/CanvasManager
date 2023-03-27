import xlsxwriter
from datetime import date
from datetime import datetime
from datetime import timedelta
import tkinter as tk
from tkcalendar import Calendar, DateEntry



def keyWindow():
    window = tk.Tk()
    window.geometry("600x400")
    window.title("Course Information Updater")
    buttonSAndQ = tk.Button(window, text = "Save and Close Window", command = window.destroy)
    buttonSAndQ.pack(side="bottom")
    
    # add a text box to enter course ID
    course = tk.Label(window, text="Enter Course ID:")
    course.pack(side="top", pady=10)
    courseID = tk.Entry(window, bd=5)
    courseID.pack(side="top")
    
    # add a text box to enter key
    course = tk.Label(window, text="Enter Your Key:")
    course.pack(side="top", pady=10)
    courseID = tk.Entry(window, bd=5)
    courseID.pack(side="top")
    
    buttonHelp = tk.Button(window, text = "Help", command = helpWindow)
    buttonHelp.pack(side="bottom")
    
def helpWindow():
    helpWindow = tk.Tk()
    helpWindow.geometry("800x200")
    helpWindow.title("Course Information Helper")
    buttonExit = tk.Button(helpWindow, text = "Exit", command = helpWindow.destroy)
    buttonExit.pack(side="bottom")
    
    course = tk.Label(helpWindow, text="For Course ID: 1. Go to the Canvas for the course. \n2. In the URL link at the top, copy the numbers. Ex: https://ursinus.instructure.com/courses/#####")
    course.pack(side="top")
    
    course = tk.Label(helpWindow, text="For Key: 1. In Canvas, click on your Account -> Settings. \n2. Scroll down past \" Approved Integrations\" and click on \"New Access Token\". \n3. Enter anything for the purpose (Course Setup) and expiration whenever. \n4. Lastly, once it is created you MUST copy the key since it disappears afterwards. Then just enter it into our text box." )
    course.pack(side="bottom")
    
    
    
# Given start of semester, days of week class meets, and special days off (breaks and other days) 
# create the schedule template as xlsx file so prof can start planning
def createXLSX():
  name = title.get()
  first_day = cal1.get_date()
  last_day = cal2.get_date()
  meeting_days = []
  # check the buttons to see which days we need
  if CheckbuttonM.get() == 1:
    meeting_days.append(0)
  if CheckbuttonT.get() == 1:
    meeting_days.append(1)
  if CheckbuttonW.get() == 1:
    meeting_days.append(2)
  if CheckbuttonR.get() == 1:
    meeting_days.append(3)
  if CheckbuttonF.get() == 1:
    meeting_days.append(4)

  # create variable to keep track of first day of week
  first_of_week = meeting_days[0]

  days_off = {date(2023, 2, 3): "Study Day", date(2023, 2, 13): "In Service Day"}
    
  # create array to hold csv data
  data = []

  # index to track which day we are on in the list
  # add one every time a valid row is added (i.e. a row with a class day)
  index = 1

  # counter for which week # we are in
  week_num = 1

  # create headers for the columns
  data.append(["Week", "Class", "Date", "Day", "Topic", "Assignment", "Notes"])

  # iterate though each day of the semester
  for single_date in daterange(first_day, last_day):
    # create array to hold data for current date
    data_row = []

    # get weekday as integer, change that integer to a string
    day = single_date.weekday()

    # check : 1) if current date is one of the meeting days
    #         2) if current date is Saturday (5) or Sunday (6)
    if (day in meeting_days and day != 5 and day != 6):
      #if this is a valid day, add a row to our csv file
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

      # add row to our CSV array
      data.append(data_row)
      index += 1

    # add one blank row if we get to a weekend (i.e. we get to Friday)
    if day == 4:
      data.append([])

    # generate xlsx to hold data
    workbook = xlsxwriter.Workbook(name + '.xlsx')
    worksheet = workbook.add_worksheet()

    for row_num, row_data in enumerate(data):
      for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)

    workbook.close()

# create our tKinter object
root = tk.Tk()

# set the size of the window
root.geometry("600x400")

# add a title to the window
root.title("XLSX Template Creator v3")

# add a text box to enter class title
label = tk.Label(root, text="Enter Class Name:")
label.pack(side="top", pady=10)
title = tk.Entry(root, bd=5)
title.pack(side="top")

# add a box to select the first day of semester
L1 = tk.Label(root, text="Select First Day: ")
L1.pack(side="top", pady=10)
cal1 = DateEntry(root, selectmode='day')
cal1.pack(side="top")

# add a box to select the last day of semester
L2 = tk.Label(root, text="Select Last Day: ")
L2.pack(side="top", pady=10)
cal2 = DateEntry(root, selectmode='day')
cal2.pack(side="top")

# add button to select days of week
# this will be a list of 5 check buttons M-F
label_days = tk.Label(root, text="Select Days of Week:")
label_days.pack(side="top", pady=10)

# add five checkbuttons, one for each for each day of week (M-F)
# I know it's clunky but trust me it's the only way
CheckbuttonM = tk.IntVar()
ButtonM = tk.Checkbutton(root,
                          text="M",
                          variable=CheckbuttonM,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=5)

ButtonM.pack(side="left", anchor='n', padx=(130,0))

CheckbuttonT = tk.IntVar()
ButtonT = tk.Checkbutton(root,
                          text="T",
                          variable=CheckbuttonT,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=5)

ButtonT.pack(side="left", anchor='n')

CheckbuttonW = tk.IntVar()
ButtonW = tk.Checkbutton(root,
                          text="W",
                          variable=CheckbuttonW,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=5)

ButtonW.pack(side="left", anchor='n')

CheckbuttonR = tk.IntVar()
ButtonR = tk.Checkbutton(root,
                          text="R",
                          variable=CheckbuttonR,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=5)

ButtonR.pack(side="left", anchor='n')

CheckbuttonF = tk.IntVar()
ButtonF = tk.Checkbutton(root,
                          text="F",
                          variable=CheckbuttonF,
                          onvalue=1,
                          offvalue=0,
                          height=2,
                          width=5)

ButtonF.pack(side="left", anchor='n')

# finally, add a button to generate the Xlsx template
button = tk.Button(root, text="Create XLSX File", command= createXLSX)
button.pack(side = "bottom", pady=10)

buttonKeyWindow = tk.Button(root, text = "Set Course Information", command = keyWindow)
buttonKeyWindow.pack(side = "bottom", pady = 10)

# helper method for date range
# All credit goes to this source:
# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# helper method to get abbreviation for the day
def getDay(x):
  if x == 0:
    return "M"
  elif x == 1:
    return "T"
  elif x == 2:
    return "W"
  elif x == 3:
    return "R"
  elif x == 4:
    return "F"
  
    
root.mainloop()