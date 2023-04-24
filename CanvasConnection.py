#												SETUP
# Import the Canvas class
from canvasapi import Canvas

# Canvas API URL
API_URL = "https://ursinus.instructure.com"
# Canvas API key
API_KEY = "6723~A2KTPfsPob1ZYugZg3xsrJWaA94bathpwkDemhIyUcZNNGMiTekg6CNtoiFAVtCW"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

# Grab course 123456
course = canvas.get_course(15293)

# Access the course's name
name= course.name
print(name)




'''


#												ASSIGNMENTS
# CREATE ASSIGNMENT GROUP
groups = course.get_assignment_groups()
for group in groups:
    print(group)
	

new_group= course.create_assignment_group()
({ 
  # the name of the Assignment Group
  "name": "Labs",
  # the position of the Assignment Group
  "position": 7,
  # the weight of the Assignment Group
  "group_weight": 20,
  # the sis source id of the Assignment Group
  "sis_source_id": "1234"
  # the integration data of the Assignment Group
  #the assignments in this Assignment Group (see the Assignment API for a detailed list of fields)
})

print(new_group)


# CREATE ASSIGNMENT
from datetime import datetime
new_assignment = course.create_assignment({
    'name': 'Hello',
	'group_id': 11,
    'submission_types': ['online_upload', 'online_text_entry', 'online_url'],
    'allowed_extensions': ['docx', 'doc', 'pdf'],
    'notify_of_update': True,
    'points_possible': 100,
    'due_at': datetime(2023, 2, 1, 11, 59),
    'description': 'Hello World',
    'published': True
})
print(new_assignment)


# GRADE ASSSIGNMENT
assignmentid= new_assignment.id

# Get single assignment
assignment= course.get_assignment(assignmentid)
submission = assignment.get_submission(1742) # 1742 is the student's id
submission.edit(submission={'posted_grade':100.0})
submission.edit(submission={'update_comment': 'Great work!'})
# submission.create_submission_item(submission_item={'comment': Good job!!!!, 'type': type})


# EDIT

# Update Assignment Name
updated_assignment = new_assignment.edit(assignment={'name': 'Updated Name'})

# Edit Submission Type and Description #
updated_assignment = new_assignment.edit(assignment={'submission_types': ['on_paper']})

updated_assignment = new_assignment.edit(assignment={'description': ['Hello World']})

# Edit a Module
mods = course.get_modules()
for module in mods:
	for item in module.get_module_items():
		if item.type=='SubHeader':
			item.delete()

'''	

# Bulk Operations

# method to get assignments
def getAssignments():
    return course.get_assignments()

# Delete Assignments

assignments = course.get_assignments()
# get all assignments and print them in a list


# insert code by John to select from the list in the GUI
# put the users selected assignments in a list to be deleted
def deleteAssignments(checkedAssignments):
    for a in checkedAssignments:
        assignment = course.get_assignment(a)
        assignment.delete()
	
# method to get modules
def getModules():
    return course.get_modules()

def deleteModules(checkedModules):
    for m in checkedModules:
        module = course.get_module(m)
        module.delete()

# method to get files
def getFiles():
    return course.get_files()

def deleteFiles(checkedFiles):
    for f in checkedFiles:
        file = course.get_file(f)
        file.delete()

'''
#Delete Modules
mods = course.get_modules()
for module in mods:
	print(module)
# insert code by John to select from the list in the GUI
# put the users selected modules in a list to be deleted
for module in checkedmods:
	module.delete()


# Move Modules
mods = course.get_modules()
for module in mods:
	print(module)
# insert code by John to select from the list in the GUI
# put the users selected modules in a list to be moved
for module in checkedmods:
	newposition= module.edit('position': position +1) 

# 
'''