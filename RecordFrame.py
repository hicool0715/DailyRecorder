from tkinter import *
from tkinter import ttk
from StartRecordFrame import StartRecordFrame

class RecordFrame:
    def __init__(self, root):
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(mainframe, text="请输入要记录的内容").grid(column=1, row=1, sticky=W)
        record_name = StringVar()
        ttk.Entry(mainframe, width=20, textvariable=record_name).grid(column=2, row=1, sticky=(W, E))
        ttk.Button(mainframe, text="确认", command=lambda: StartRecordFrame(root, record_name.get())).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text="返回", command=lambda:mainframe.destroy()).grid(column=2, row=2, sticky=W)

        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
