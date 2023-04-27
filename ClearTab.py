import tkinter as tk
from ttkwidgets import CheckboxTreeview
from CanvasConnection import getAssignments
from CanvasConnection import deleteAssignments
from CanvasConnection import getModules
from CanvasConnection import deleteModules
from CanvasConnection import getFiles
from CanvasConnection import deleteFiles

def makeClearTab(root):
    # Clear Tab (tab3)
    # The clear tab will be able to clear all modules, assignments, and/or files
    # from our Canvas course

    # create checkboxtree to list our three options
    tree = CheckboxTreeview(root)
    tree.pack(side="top")

    # create array to hold our options
    options = ["Modules", "Assignments", "Files"]

    # add options to our tree
    for o in options:
        tree.insert("", "end", o, text=o)

    # method to select all options
    def select_all():
        for o in options:
            if o not in tree.get_checked():
                tree.change_state(o, "checked")

    # method to clear canvas page of whichever options were chosen
    def clear_selected():
        
        # get whichever options were checked
        selected = tree.get_checked()
        
        # delete selected options from canvas
        if "Modules" in selected:
            modules = getModules()
            deleteModules(modules)
        if "Assignments" in selected:
            assignments = getAssignments()
            deleteAssignments(assignments)
        if "Files" in selected:
            files = getFiles()
            deleteFiles(files)
            
    
    selectAll = tk.Button(root, text="Select All Options", command=select_all)
    selectAll.pack(side="top", pady = 10)
    
    clearButton = tk.Button(root, text="Clear Selected", command=clear_selected)
    clearButton.pack(side="top", pady = 10)