import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from ttkwidgets import CheckboxTreeview
from GuiHelpers import getDay
from CreateXLSX import createXLSX
from ModuleCreator import ModuleCreator
import os.path

def makeStartTab(root):
    # Start Tab (tab1)


    key = ""
    courseID = -1
    
    
    def selectFile():
        root.filename =  tk.filedialog.askopenfilename(initialdir = "./", title = "Select Finished Sheet")
        fileLabel = tk.Label(root, text = root.filename)
        fileLabel.pack(side = "right")
        print("hello")
        print(root.filename)
        
    def openInfoSave():
        courseIDVar, keyVar  = SaveInfoWindow()
        print(keyVar.get(), "<- key, course ID -> ", courseIDVar.get())
        print(keyVar, courseIDVar)
        nonlocal key
        key = keyVar.get()
        if courseIDVar.get():
            nonlocal courseID 
            courseID = int(courseIDVar.get())
        print(key, courseID)
        
        #write to a txt file so other tabs can use the same info
        if courseID != -1 and key !="":
            with open ("CanvasInfo.txt", 'w') as file:
                string = str(courseID)+ "\n"+ key
                file.write(string)
                file.close()
            


    def moduleCreation():
        
        if(courseID==-1 or key == ""):
            #read in the data, if it exists
            if(os.path.isfile("./CanvasInfo.txt")):
                #read in the course id and key 
                with open ("./CanvasInfo.txt", 'r') as file:
                    lines = file.readlines()
                    file.close()
                nonlocal courseID
                courseID = int(lines[0].strip())
                nonlocal key
                key = lines[1]
        
        ModuleCreator(courseID, key, root.filename) 

    # add method to create xlsx file
    def createFile():
        name = title.get() 
        first_day = cal1.get_date() 
        last_day = cal2.get_date() 
        meeting_days = dayTree.get_checked() 
        
        createXLSX(name, first_day, last_day, meeting_days, user_days_off, recurringDays)

    # add a text box to enter class title
    label = tk.Label(root, text="Class Name:")
    label.pack(side="top", pady=10)
    title = tk.Entry(root, bd=5)
    title.pack(side="top")

    # add a box to select the first day of semester
    L1 = tk.Label(root, text="Select First Day: ")
    L1.pack(side="top", pady=5)
    cal1 = DateEntry(root, selectmode='day')
    cal1.pack(side="top")

    # add a box to select the last day of semester
    L2 = tk.Label(root, text="Select Last Day: ")
    L2.pack(side="top", pady=5)
    cal2 = DateEntry(root, selectmode='day')
    cal2.pack(side="top")

    # add option to select days of the week
    # this will be a list of 5 check buttons M-F
    label_days = tk.Label(root, text="Select Days of Week:")
    label_days.pack(side="top", pady=5)

    dayTree = CheckboxTreeview(root, height = 5)
    dayTree.pack(side="top")

    days = [0, 1, 2, 3, 4]

    for day in days:
        dayTree.insert("", "end", day, text=getDay(day))

    def select_days():
        for day in days:
            if day not in dayTree.get_checked():
                dayTree.change_state(day, "checked")

    selectAll = tk.Button(root, text="Select All Days", command=select_days)
    selectAll.pack(side="top", pady = 5)
    
    # create a dictionary to hold our recurring days
    # keys are day (0-4) and values are description of recurring event (e.g. Lab Day)
    recurringDays = {}
    
    # Allow users to select recurring days off and give reasoning
    def select_recurring():
        #create a pop-up window 
        window = tk.Toplevel()
        window.title("Secondary Window")
        window.config(width=300, height=200)
        
        def add_reasoning():
            selection = "You selected " + getDay(var.get())
            optionLabel = tk.Label(window, text=selection)
            optionLabel.pack(side="top", pady=10)
            
             # add a text box to enter class title
            label = tk.Label(window, text="Enter reason for recurring day: ")
            label.pack(side="top", pady=10)
            recurr = tk.Entry(window, bd=5)
            recurr.pack(side="top")
            
            def save_day():
                day = var.get()
                reason = recurr.get()
                recurringDays[day] = reason
                window.destroy
            
            #create button to save day
            button_save = ttk.Button(window, 
                    text="Save Recurring Day",
                    command=save_day)
            button_save.pack(side="bottom")
            
            #create button to close window
            button_close = ttk.Button(window, 
                    text="Close Window",
                    command=window.destroy)
            button_close.pack(side="bottom")
            

        var = tk.IntVar()
        R1 = tk.Radiobutton(window, text="M", variable=var, value=0,
                  command=add_reasoning)
        R1.pack(side="bottom")

        R2 = tk.Radiobutton(window, text="T", variable=var, value=1,
                  command=add_reasoning)
        R2.pack(side="bottom")

        R3 = tk.Radiobutton(window, text="W", variable=var, value=2,
                  command=add_reasoning)
        R3.pack(side="bottom")
        
        R4 = tk.Radiobutton(window, text="R", variable=var, value=3,
                  command=add_reasoning)
        R4.pack(side="bottom")

        R5 = tk.Radiobutton(window, text="F", variable=var, value=4,
                  command=add_reasoning)
        R5.pack(side="bottom")
        
    
    # Add a button to select special recurring days
    reccurButton = tk.Button(root, text="Select Recurring Special Days", command=select_recurring)
    reccurButton.pack(side="top", pady = 10)

    # Add Calendar
    cal = Calendar(root, selectmode = 'day',
               year = 2023, month = 1,
               day = 1)
 
    cal.pack(side="right")

    #Create dictionary to hold our days off
    user_days_off = {}

    # Define Function to select the date
    def get_day():
        day = cal.get_date()
        if day not in dayOffBox.get("1.0", tk.END+"-1c"):
            dayOffBox.insert(tk.END, day+ "\n")
            user_days_off[day] = ""
            
            #create a pop-up window 
            window = tk.Toplevel()
            window.title("Secondary Window")
            window.config(width=300, height=200)
            
            # add option to enter reason for day off
            reasonLabel = tk.Label(window, text="Enter reason for day off on " + day + ":")
            reasonLabel.pack(side="top", pady=10)
            reason = tk.Entry(window, bd=5)
            reason.pack(side="top")
            
            def save_reason():
                user_days_off[day] = reason.get()
            
            #create button to save reason
            button_save= ttk.Button(window, 
                    text="Save Day Off Reason",
                    command=save_reason)
            button_save.pack(side="bottom")
            
            #create button to close window
            button_close= ttk.Button(window, 
                    text="Close Window",
                    command=window.destroy)
            button_close.pack(side="bottom")
            
    #Create a button to pick the days off (one at a time)
    button = tk.Button(root, text="Select Day Off", command=get_day)
    button.pack(side="right", pady = 10)

    # add text box to display all selected days off
    dayOffLabel = tk.Label(root, text = "List of Selected Days Off: ")
    dayOffLabel.pack(side="left")
    dayOffBox = tk.Text(root, height = 10, width = 30)
    dayOffBox.pack(side="left")

    # finally, add a button to generate the Xlsx template
    button = tk.Button(root, text="Create Spreadsheet", command= createFile)
    button.pack(side = "bottom", pady=10)
    
    #Create button to select File
    buttonFileSelect = tk.Button(root, text = "Select File", command = selectFile)
    buttonFileSelect.pack(side = tk.LEFT)
    
    
    #Create a button to set the course information
    buttonKeyWindow = tk.Button(root, text = "Set Canvas Information", command = openInfoSave)
    buttonKeyWindow.pack(side = tk.LEFT)  
    
    
    buttonRunModules = tk.Button(root, text = "Run Module Creation", command = moduleCreation)
    buttonRunModules.pack(side = tk.LEFT)



def SaveInfoWindow():
    
    
    keywindow = tk.Toplevel()
    keywindow.geometry("600x400")
    keywindow.title("Course Information Updater")
    
    
    # add a text box to enter course ID
    IDVar = tk.StringVar()
    courseIDLabel = tk.Label(keywindow, text="Enter Course ID:")
    courseIDLabel.pack(side="top", pady=10)
    courseIDEntry = tk.Entry(keywindow, bd=5, textvariable=IDVar)
    courseIDEntry.pack(side="top")
    
    # add a text box to enter key
    keyVar = tk.StringVar()
    keyLabel = tk.Label(keywindow, text="Enter Your Key:")
    keyLabel.pack(side="top", pady=10)
    keyEntry = tk.Entry(keywindow, bd=5, textvariable = keyVar)
    keyEntry.pack(side="top")
    
    buttonSAndQ = tk.Button(keywindow, text = "Save and Close Window", command = keywindow.destroy)
    buttonSAndQ.pack(side="bottom")
    
    buttonHelp = tk.Button(keywindow, text = "Help", command = helpWindow)
    buttonHelp.pack(side="bottom")
    
    keywindow.wait_window()
    
    print("reached end of save info stuff")
    print(IDVar.get())
    return IDVar, keyVar

    
        
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
    
    