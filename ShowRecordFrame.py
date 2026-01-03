import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import datetime
from datetime import date
from YamlHandler import YamlHandler
from BasicFrame import BasicFrame

class ShowRecordFrame(BasicFrame):
    def createWidgets(self, root):
        self.main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=1, sticky=(N, W, E, S))
        self.current_date = date.today()

        date_choise_frame = ttk.Frame(self.main_frame, padding=(3, 3, 12, 12))
        date_choise_frame.pack(side=tk.TOP)
        self.label_text = tk.StringVar()
        self.label_text.set(f"今日记录内容({str(self.current_date)})：")
        self.list_val = tk.StringVar(value=[])
        ttk.Button(date_choise_frame, text="昨日", command=lambda: self.update_date(False), bootstyle=PRIMARY).pack(side=tk.LEFT, pady=5)
        ttk.Label(date_choise_frame, textvariable=self.label_text).pack(side=tk.LEFT, expand=True)
        ttk.Button(date_choise_frame, text="明日", command=lambda: self.update_date(True), bootstyle=PRIMARY).pack(side=tk.RIGHT, pady=5)


        tk.Listbox(self.main_frame, listvariable=self.list_val).pack(side=tk.LEFT, padx=3, pady=5)
        self.update_list()
        from EntranceFrame import EntranceFrame
        ttk.Button(self.main_frame, text="返回", command=lambda: self.showFrame(EntranceFrame()), bootstyle=DANGER).pack(side=tk.RIGHT, padx=12, pady=5)
        
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