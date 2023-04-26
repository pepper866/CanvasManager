import tkinter as tk
from ttkwidgets import CheckboxTreeview
from CanvasConnection import getAssignments
from CanvasConnection import deleteAssignments

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

    def select_all():
        for o in options:
            if o not in tree.get_checked():
                tree.change_state(o, "checked")

    def clear_selected():
        return
    
    selectAll = tk.Button(root, text="Select All Options", command=select_all)
    selectAll.pack(side="top", pady = 10)
    
    clearButton = tk.Button(root, text="Clear Selected", command=clear_selected)
    clearButton.pack(side="top", pady = 10)