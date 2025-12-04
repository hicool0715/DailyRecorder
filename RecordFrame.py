
from datetime import date
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from BasicFrame import BasicFrame
from YamlHandler import YamlHandler
from StartRecordFrame import StartRecordFrame

class RecordFrame(BasicFrame):
    def __init__(self, record_name):
        self.record_name = record_name

    def createWidgets(self, root):
        self.main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        
        self.yaml_message = YamlHandler(YamlHandler.record_dir,str(date.today())+'.yaml').read_yaml()
        if self.yaml_message is None:
            self.yaml_message = {}
            self.yaml_message[self.record_name] = 0
        if self.record_name not in self.yaml_message:
            self.yaml_message[self.record_name] = 0
        self.record_text = tk.StringVar()
        self.record_text.set(f"记录内容：{self.record_name}  当前次数：{self.yaml_message[self.record_name]}")
        ttk.Label(self.main_frame, textvariable=self.record_text).grid(column=1, row=1, sticky=W)
        ttk.Button(self.main_frame, text="增加次数", command=lambda: self.update_count(True), bootstyle=PRIMARY).grid(column=1, row=2, sticky=W)
        ttk.Button(self.main_frame, text="减少次数", command=lambda: self.update_count(False), bootstyle=PRIMARY).grid(column=2, row=2, sticky=W)
        ttk.Button(self.main_frame, text="保存并返回", command=lambda: self.save_record(), bootstyle=SUCCESS).grid(column=1, row=3, sticky=W)
        ttk.Button(self.main_frame, text="取消并返回", command=lambda: self.showFrame(StartRecordFrame()), bootstyle=DANGER).grid(column=2, row=3, sticky=W)
    
        self.main_frame.columnconfigure(2, weight=1)
        for child in self.main_frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def update_count(self,is_plus):
        if is_plus:
            self.yaml_message[self.record_name] += 1
        else:
            self.yaml_message[self.record_name] -= 1
        self.record_text.set(f"记录内容：{self.record_name}  当前次数：{self.yaml_message[self.record_name]}")

    def save_record(self):
        YamlHandler(YamlHandler.record_dir,str(date.today())+'.yaml').write_yaml(self.yaml_message)
        self.showFrame(StartRecordFrame())
