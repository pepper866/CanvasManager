import tkinter as tk
from tkinter import ttk
from StartTab import makeStartTab
from BulkTab import makeBulkTab
from ClearTab import makeClearTab

# create our tKinter object
root = tk.Tk()

# set the size of the window
root.geometry("700x1000") 

# add a title to the window
root.title("XLSX Template Creator v3")

# Create our three tabs (Start, Bulk, Clear)
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

# add some title for our tabs
tabControl.add(tab1, text ='Start')
tabControl.add(tab2, text ='Bulk')
tabControl.add(tab3, text ='Clear')
tabControl.pack(expand = 1, fill ="both")

# create our start tab (StartTab.py)
makeStartTab(tab1)

# create our bulk tab (BulkTab.py)
makeBulkTab(tab2)

# create our clear tab (ClearTab.py)
makeClearTab(tab3)

# run our tkinter loop
root.mainloop()