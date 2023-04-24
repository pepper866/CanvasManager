import tkinter as tk
from ttkwidgets import CheckboxTreeview
from CanvasConnection import getAssignments
from CanvasConnection import deleteAssignments
from CanvasConnection import getModules
from CanvasConnection import deleteModules
from CanvasConnection import getFiles
from CanvasConnection import deleteFiles


def makeBulkTab(root):
    # Bulk Tab (tab2)
    # The bulk tab will be able to list the assignments from a Canvas course
    # Professers will be able to select assignments (via checkboxes) and 
    # delete them or move them to a new Module
    
    assignTree = CheckboxTreeview(root)
    modTree = CheckboxTreeview(root)
    fileTree = CheckboxTreeview(root)

    # Get list of all assignmnets from our Canvas course (found in CanvasConnection.py)
    # and create checkboxes for all assignments in this course
    def show_assignments():

        # grab the list of current assignments from our Canvas course
        # using Rachel's code (CanvasConnection.py)
        assignments = getAssignments()

        # Create a label to show our assignments
        assingmentLabel = tk.Label(root, text = "List of Assignments: ")
        assingmentLabel.pack(side="top")

        # place the list of assingments on our GUI
        assignTree.pack(side="top")
        for a in assignments:
            assignTree.insert("", "end", a.id, text=a)

        # add a button to delete all checked assignments from Canvas
        # and also remove them from our list
        deleteButton = tk.Button(root, text="Delete Assignments", command=getDeletedAssign)
        deleteButton.pack(side="top")
  
    # Create a button generate a list of all assignments
    button = tk.Button(root, text="Show Assignments", command=show_assignments)
    button.pack(side="left")
    
    # Get list of all modules from our Canvas course (found in CanvasConnection.py)
    # and create checkboxes for all modules in this course
    def show_modules():

        # grab the list of current modules from our Canvas course
        # using Rachel's code (CanvasConnection.py)
        modules = getModules()

        # Create a label to show our modules
        moduleLabel = tk.Label(root, text = "List of Modules: ")
        moduleLabel.pack(side="top")

        # place the list of modules on our GUI
        modTree.pack(side="top")
        for m in modules:
            modTree.insert("", "end", m.id, text=m)

        # add a button to delete all checked modules from Canvas
        # and also remove them from our list
        deleteButton = tk.Button(root, text="Delete Modules", command=getDeletedMods)
        deleteButton.pack(side="top")
    
    # Create a button generate a list of all modules
    button = tk.Button(root, text="Show Modules", command=show_modules)
    button.pack(side="left")
    
    # Get list of all files from our Canvas course (found in CanvasConnection.py)
    # and create checkboxes for all files in this course
    def show_files():

        # grab the list of current files from our Canvas course
        # using Rachel's code (CanvasConnection.py)
        files = getFiles()

        # Create a label to show our filws
        fileLabel = tk.Label(root, text = "List of Files: ")
        fileLabel.pack(side="top")

        # place the list of files on our GUI
        fileTree.pack(side="top")
        for f in files:
            fileTree.insert("", "end", f.id, text=f)

        # add a button to delete all checked files from Canvas
        # and also remove them from our list
        deleteButton = tk.Button(root, text="Delete Files", command=getDeletedFiles)
        deleteButton.pack(side="top")
    
    # Create a button generate a list of all files
    button = tk.Button(root, text="Show Files", command=show_files)
    button.pack(side="left")
    
    # This method will be called by the "Delete Assignments" button
    # It will grab a list of the assignments to be deleted
    # This list will be sent back to Rachel's program which deletes 
    # the assignments from Canvas
    def getDeletedAssign():
        deleted = assignTree.get_checked()
        deleteAssignments(deleted)
        for box in deleted:
            assignTree.delete(box)
            
    def getDeletedMods():
        deleted = modTree.get_checked()
        deleteModules(deleted)
        for box in deleted:
            modTree.delete(box)
            
    def getDeletedFiles():
        deleted = fileTree.get_checked()
        deleteFiles(deleted)
        for box in deleted:
            fileTree.delete(box)