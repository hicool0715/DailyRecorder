# from pynput import keyboard
# import os
# from datetime import date
# import yaml
# import time
# import sys
# class uiOperations:
#     def showChoices(self):
#         os.system('cls')
#         print("-------------------")
#         print("请选择操作：")
#         print("1. 开始记录")
#         print("2. 查看记录")
#         print("3. 退出")
#         print("-------------------")
#         print("请输入选项（1/2/3）：")
#         with keyboard.Events() as events:
#             for event in events:
#                 if isinstance(event, keyboard.Events.Release):
#                     match event.key.char:
#                         case '1': 
#                             self.startRecord()
#                         case '2': 
#                             self.showRecord()
#                         case '3': exit()
#                         case _: 
#                             print("无效选项，请重新输入。")
#                             self.showChoices()

#     def startRecord(self): 
#         os.system('cls')
#         print("-------------------")
#         print("请输入记录内容：")
#         print("-------------------")
#         name = input()
#         key_counter = 0
#         os.system('cls')
#         print("开始记录按键次数，按上箭头增加次数，按下箭头减少次数，按Esc键结束记录。")
#         print(f"当前次数：{key_counter}")
#         with keyboard.Events() as events:
#             for event in events:
#                 if isinstance(event, keyboard.Events.Release):
#                     if event.key == keyboard.Key.up:
#                         key_counter += 1
#                     elif event.key == keyboard.Key.down:
#                         if key_counter == 0:
#                             print("当前数值为0,不能再减少")
#                         else:
#                             key_counter -= 1
#                     elif event.key == keyboard.Key.esc:
#                         break  
#                 os.system('cls')
#                 print("开始记录按键次数，按上箭头增加次数，按下箭头减少次数，按Esc键结束记录。")
#                 print(f"当前次数：{key_counter}")
            

#         yaml_handler = YamlHandler('records.yaml')
#         data = yaml_handler.read_yaml()
#         data[str(date.today())][name] = key_counter
#         yaml_handler.write_yaml(data)
#         os.system('cls')
#         print("已记录：[{name}] : [{key_counter}]\n按[esc]按键返回上级目录，按[q]键退出程序。")
#         # The event listener will be running in this block
#         with keyboard.Events() as events:
#             for event in events:
#                 if isinstance(event, keyboard.Events.Release):
#                     if event.key == keyboard.Key.esc:
#                         self.showChoices()
#                     elif event.key.char == 'q':
#                         exit()

#     def showRecord(self): pass



# class YamlHandler:
#     def __init__(self, filepath):
#         self.filepath = filepath

#     def read_yaml(self):
#         with open(self.filepath, 'r', encoding='utf-8') as file:
#             data = yaml.safe_load(file)
#         return data

#     def write_yaml(self, data):
#         with open(self.filepath, 'w', encoding='utf-8') as file:
#             yaml.dump(data, file, allow_unicode=True)


# # # TimesRecord().startRecord()
# # today = date.today()
# # print(today)
# uiOperations().showChoices()

from tkinter import *
from tkinter import ttk
import datetime   
from datetime import date
import os
import yaml
import time

class YamlHandler:
    def __init__(self, file_dir, file_name):
        self.filepath = f"{file_dir}/{file_name}"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as file: pass

    def read_yaml(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return data

    def write_yaml(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            yaml.dump(data, file, allow_unicode=True)

class EntranceFrame:
    def __init__(self):
        root = Tk()
        root.title("o mini beimei hong")
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(mainframe, text="请选择操作：").grid(column=1, row=1, sticky=W)
        ttk.Button(mainframe, text="开始记录", command=lambda:RecordFrame(root)).grid(column=1, row=2, sticky=W)
        ttk.Button(mainframe, text="查看记录", command=lambda:ShowFrame(root)).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text="退出", command=lambda: root.quit()).grid(column=1, row=4, sticky=W)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        root.mainloop() 

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

class StartRecordFrame:
    def __init__(self, root, record_name):
        mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.record_name = record_name
        self.yaml_message = YamlHandler('records',str(date.today())+'.yaml').read_yaml()
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
        YamlHandler('records',str(date.today())+'.yaml').write_yaml(self.yaml_message)
        mainframe.destroy()

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
        yaml_message = YamlHandler('records', str(self.current_date) + '.yaml').read_yaml()
        if yaml_message is not None:
            display_list = [f"{key} : {value}" for key, value in yaml_message.items()]
            self.list_val.set(display_list)
        else:
            self.list_val.set([])


EntranceFrame()