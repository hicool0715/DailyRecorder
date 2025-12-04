from YamlHandler import YamlHandler
from datetime import date
from tkinter import ttk
from tkinter import *

class StartRecordFrame:
    def __init__(self, root, record_name):
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.record_name = record_name
        self.yaml_message = YamlHandler(YamlHandler.record_dir,str(date.today())+'.yaml').read_yaml()
        if self.yaml_message is None:
            self.yaml_message = {}
            self.yaml_message[self.record_name] = 0
        if self.record_name not in self.yaml_message:
            self.yaml_message[self.record_name] = 0
        self.record_text = StringVar()
        self.record_text.set(f"记录内容：{self.record_name}  当前次数：{self.yaml_message[self.record_name]}")
        ttk.Label(mainframe, textvariable=self.record_text).grid(column=1, row=1, sticky=W)
        ttk.Button(mainframe, text="增加次数", command=lambda: self.update_count(True)).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text="减少次数", command=lambda: self.update_count(False)).grid(column=2, row=2, sticky=W)
        ttk.Button(mainframe, text="保存并返回", command=lambda: self.save_record(mainframe) ).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text="取消并返回", command=lambda: mainframe.destroy()).grid(column=2, row=3, sticky=W)
    
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def update_count(self,is_plus):
        if is_plus:
            self.yaml_message[self.record_name] += 1
        else:
            self.yaml_message[self.record_name] -= 1
        self.record_text.set(f"记录内容：{self.record_name}  当前次数：{self.yaml_message[self.record_name]}")

    def save_record(self, mainframe):
        YamlHandler(YamlHandler.record_dir,str(date.today())+'.yaml').write_yaml(self.yaml_message)
        mainframe.destroy()
