import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class BasicFrame:
    def createWidgets(self, root):
        pass

    def showFrame(self, target_frame):
        self.destroyWidgets()
        target_frame.createWidgets(self.main_frame.master)

    def destroyWidgets(self):
        self.main_frame.destroy()