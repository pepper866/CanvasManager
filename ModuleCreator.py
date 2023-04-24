# Import the Canvas class
from canvasapi import Canvas
import datetime
import AssignmentInfo
import pandas

'''
course.update(course={'name': 'New Course Name'})
name2=course.name
print(name2)

course = canvas.get_course(15578)
name = course.name
print(name)
'''


def load_assignments(filename):
    
  df = pandas.read_excel(filename, sheet_name=1)
  '''
  data = []
  with open("./Assignments.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      data.append(row)
  '''
  data = df.values
  assignments = {}
  for row in data:
      
      for i in range(len(row)):
          
          if(pandas.isna(row[i])):
              row[i] = ""
      
      thing = AssignmentInfo.AssignmentInfo(row)
      
      #thing.addData(row)
      assignments[row[0]] = thing
      print(row[0])
      #assignments1[row[0]] = thing  #does this work?????? no, can't use str keys in a list. Could use dict?

      print(thing.name)

  print("Assignments:")
  print(assignments)
  #print(assignments1[assignments1[0].name].title)
  return assignments


def load_modules(filename):
  print("Hi")
  '''data = pandas.read_excel("./Test.xlsm")
  return data'''
  
  df = pandas.read_excel(filename, sheet_name=0)
  print(df)
  
  '''
  data = []
  with open("./Syl.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
      data.append(row)
      #print(row)
      '''
  return df.values
  


def make_modules(course, filename):
  #create module

  #read file
  data = load_modules(filename)
  assignments_data = load_assignments(filename)
  existing_assignments = course.get_assignments()
  #assignments_data = None
  #create modules for each week
  mod = None
  start = False
  id = 0
  for r in range(15):  #just read first 10 lines for now
    row = data[r]

    if row[0] != '' and not pandas.isna(row[0]):
      #new week (new big module)
      print(row)
      title = "Week " + str(int(row[0]))
      mod = course.create_module(module={'name': title})
      start = True
    print(r, " ", row[1])
    if row[1] != '' and not pandas.isna(row[1]) and start:
      print(row)
      #new class day (module item subheader)
      title = "Day #" + str(int(row[1])) + " " + str(row[2])  + " " + str(row[4])
      print(title)
      mod.create_module_item(module_item={'title': title, 'type': 'SubHeader'})

      #mod #assignment info
      if row[5] != '' and not pandas.isna(row[5]):
        key = row[5]
        print(row[5])
        print("is it nan?")
        print(row[5]=="nan")
        
        #if the assignments already exist
        exists = False
        for assignment in existing_assignments:
            if assignment.name == row[5] or assignment.name == assignments_data[row[5]].title:
              #if the assignment matches the name in the syllabus or in the Assignments csv list
              #add it
              mod.create_module_item(
                module_item={
                  'title': assignment.name,
                  'type': 'assignment',
                  'content_id': assignment.id
                })
              exists = True
              break

        #new assignment
        if not exists:
          make_assignment(course, mod, assignments_data[key], id)
          id += 1
          print("Making Assignment: ", key)


def make_assignment(course, mod, data,
                    id):  #called from make_modules DO NOT CALL OTHERWISE
  #new_assign = course.create_assignment({'name': title})
  #find assignment by query
  #assignments = course.get_assignments()
  #assignment = course.get_assignment(1234)
  #assignment = assignments[0]
  #go through assignments to find our assignment
  #using the assignment ID would be easier

  # format
  format = '%m/%d/%Y'

  # convert from string format to datetime format
  date = data.due_date
  '''
  if(not data.due_date==""):
      date = datetime.datetime.strptime((data.due_date), format)
  else:
      date = ""
      '''
  new_assignment = course.create_assignment({
    'id': id,
    'name': data.title,
    'submission_types': data.submission_types,
    'allowed_extensions': data.extensions,
    'notify_of_update': True,
    'points_possible': data.points,
    'due_at': date,
    'description': data.details,
    'published': True
  })
  print(new_assignment)

  #add assignment to module by item
  #  get module
  #course.get_module(ID)
  #mods = course.get_modules()
  #mod = mods[0]
  #  add item
  mod.create_module_item(
    module_item={
      'title': new_assignment.name,
      'type': 'assignment',
      'content_id': new_assignment.id
    })


#MAIN
# Canvas API URL
def ModuleCreator(courseID, key, filename):
    
    #filename = "./Syl.xlsm"
    
    if(courseID < 0 or key == ""):
        print("Error: No Course ID or Key")
        return

    COURSE_ID = courseID #15293
    API_URL = "https://ursinus.instructure.com"
    # Canvas API key
    API_KEY = key #"6723~A2KTPfsPob1ZYugZg3xsrJWaA94bathpwkDemhIyUcZNNGMiTekg6CNtoiFAVtCW"
    
    # Initialize a new Canvas object
    canvas = Canvas(API_URL, API_KEY)
    # Grab course 123456
    course = canvas.get_course(COURSE_ID)
    
    # Access the course's name
    name = course.name
    print(name)
   
    #assignments = load_assignments(filename)
    #load_modules(filename)
    make_modules(course, filename)
    
    
#ModuleCreator(15293, "6723~A2KTPfsPob1ZYugZg3xsrJWaA94bathpwkDemhIyUcZNNGMiTekg6CNtoiFAVtCW", "./Syl.xlsm")
