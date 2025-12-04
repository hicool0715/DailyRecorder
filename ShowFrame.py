from tkinter import *
from tkinter import ttk
import datetime
from datetime import date
from YamlHandler import YamlHandler


class ShowFrame:
    def __init__(self, root):
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.current_date = date.today()
        self.label_text = StringVar()
        self.label_text.set(f"今日记录内容({str(self.current_date)})：")
        self.list_val = StringVar(value=[])
        ttk.Button(mainframe, text="昨日", command=lambda: self.update_date(False)).grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, textvariable=self.label_text).grid(column=2, row=1, sticky=W)
        ttk.Button(mainframe, text="明日", command=lambda: self.update_date(True)).grid(column=3, row=1, sticky=W)
        Listbox(mainframe, listvariable=self.list_val).grid(column=1, row=2, sticky=(W, E))

        self.update_list()

        ttk.Button(mainframe, text="返回", command=lambda:mainframe.destroy()).grid(column=1, row=3, sticky=W)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
    def update_date(self, is_next):
        oneday=datetime.timedelta(days=1) 
        if is_next:
            self.current_date = self.current_date + oneday
        else:
            self.current_date = self.current_date - oneday
        self.update_list()
        self.label_text.set(f"今日记录内容({str(self.current_date)})：")
            
    def update_list(self):
        yaml_message = YamlHandler(YamlHandler.record_dir, str(self.current_date) + '.yaml').read_yaml()
        if yaml_message is not None:
            display_list = [f"{key} : {value}" for key, value in yaml_message.items()]
            self.list_val.set(display_list)
        else:
            self.list_val.set([])