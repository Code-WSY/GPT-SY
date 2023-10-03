# -----------------------------------------------------------------------------------#
# ----------------------------------导入窗口------------------------------------------#
# -----------------------------------------------------------------------------------#
import tkinter as tk
from Box_Dialog import Dialog_box
from Box_Message import model_message_box
from Box_Input import Input_box, temperature_box, max_tokens_box, temperature_label, max_tokens_label
from Cbox_Model import model_list, Label_model
from Cbox_Promot import func_list, Label_func
from Button_Load import import_button,import_label
from Bottom_Submit import submit_button
"""
设计：
    所有的UI设计都在这里
输出：
    load_UI()：导入模式的UI
    chat_UI()：聊天模式的UI
    foget_all()：隐藏所有的组件
"""
# ----------------------------------------------------------------------------------#
# ------------------------------------设计排列---------------------------------------#
# ----------------------------------------------------------------------------------#
def load_UI():
    # 1
    Dialog_box.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
    # 2
    model_message_box.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW)
    # 3
    temperature_label.grid(row=2, column=0, sticky=tk.E)
    temperature_box.grid(row=2, column=1, sticky=tk.W)
    max_tokens_label.grid(row=2, column=2, sticky=tk.E)
    max_tokens_box.grid(row=2, column=3, sticky=tk.W)
    # 4
    Label_model.grid(row=3, column=0, sticky=tk.E)
    model_list.grid(row=3, column=1, sticky=tk.W)
    import_label.grid(row=3, column=2, sticky=tk.E)
    import_button.grid(row=3, column=3, columnspan=1, sticky=tk.NSEW)
    # 5
    Input_box.grid(row=4, column=0, columnspan=4, sticky=tk.NSEW)
    # 6
    submit_button.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW)

def chat_UI():
    #1
    Dialog_box.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
    #2
    model_message_box.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW)
    #3
    temperature_label.grid(row=2, column=0,sticky=tk.E)
    temperature_box.grid(row=2, column=1,sticky=tk.W)
    max_tokens_label.grid(row=2, column=2,sticky=tk.E)
    max_tokens_box.grid(row=2, column=3,sticky=tk.W)
    #4
    Label_model.grid(row=3, column=0, sticky=tk.E)
    model_list.grid(row=3, column=1, sticky=tk.W)
    Label_func.grid(row=3, column=2, sticky=tk.E)
    func_list.grid(row=3, column=3, sticky=tk.W)
    #5
    Input_box.grid(row=4, column=0, columnspan=4, sticky=tk.NSEW)
    #6
    submit_button.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW)

def foget_all():
    Dialog_box.grid_forget()
    model_message_box.grid_forget()
    temperature_label.grid_forget()
    temperature_box.grid_forget()
    max_tokens_label.grid_forget()
    max_tokens_box.grid_forget()
    # 模型及功能
    Label_model.grid_forget()
    model_list.grid_forget()
    Label_func.grid_forget()
    func_list.grid_forget()
    import_button.grid_forget()

    Input_box.grid_forget()
    submit_button.grid_forget()

if __name__ == "__main__":
    pass
