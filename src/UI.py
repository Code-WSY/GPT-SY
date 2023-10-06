# -----------------------------------------------------------------------------------#
# ----------------------------------导入窗口------------------------------------------#
from Bottom_Submit_ChatCompletion import *
from Bottom_Submit_Completion import *
from Bottom_Submit_Edit import *
from Bottom_Submit_Embeding import *
from Menu_file import *
from Menu_clear import *
from Menu_setting import *
from Menu_mode import *
from Menu_login import *
"""
设计：
    所有的UI设计都在这里
"""
#菜单栏：
# -----------------------------------------------------------------------------------#
menubar.add_cascade(label="文件", menu=filemenu_file)
menubar.add_cascade(label="模式", menu=filemenu_mode)
menubar.add_cascade(label="清空", menu=filemenu_clear)
menubar.add_cascade(label="设置", menu=filemenu_setting)
menubar.add_cascade(label="登录", menu=filemenu_login)

# ----------------------------------------------------------------------------------#
# ------------------------------------设计排列---------------------------------------#
# ----------------------------------------------------------------------------------#
def init_UI():
    # 1
    Dialog_box.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)
    #Dialog_box_scrollbar.grid(row=0, column=1, sticky=tk.NSEW,ipady=100)
    # 2
    Message_box.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW)
    #model_message_box_scrollbar.grid(row=1, column=1, sticky=tk.NSEW,ipady=100)
    # 3
    temperature_label.grid(row=2, column=0, sticky=tk.E)
    temperature_box.grid(row=2, column=1, sticky=tk.W)
    max_tokens_label.grid(row=2, column=2, sticky=tk.E)
    max_tokens_box.grid(row=2, column=3, sticky=tk.W)
    # 4
    Label_model.grid(row=3, column=0, sticky=tk.E)
    model_list.grid(row=3, column=1, sticky=tk.W)
    Label_func.grid(row=3, column=2, sticky=tk.E)
    prompts_list.grid(row=3, column=3, sticky=tk.W)
    # 5
    Input_box.grid(row=4, column=0, columnspan=4, sticky=tk.NSEW)
    # 6
    submit_button_ChatCompletion.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW)

def Completion_UI():
    submit_button_Completion.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW)


def ChatCompletion_UI():
    # 6
    submit_button_ChatCompletion.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW)

def Edit_UI():
    # 6
    submit_button_Edit.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW)
def Embedding_UI():
    # 6
    submit_button_Embeding.grid(row=5, column=1, columnspan=2, sticky=tk.NSEW)

def foget_all():
    submit_button_Completion.grid_forget()
    submit_button_ChatCompletion.grid_forget()
    submit_button_Edit.grid_forget()


def change_UI():
    if selected_mode.get() == 'ChatCompletion':
        foget_all()
        ChatCompletion_UI()
        print("ChatCompletion")
    elif selected_mode.get() == 'Completion':
        foget_all()
        Completion_UI()
        print("Completion")
    elif selected_mode.get() == 'Edit':
        foget_all()
        Edit_UI()
        print("Edit")
    elif selected_mode.get() == "Embedding":
        foget_all()
        Embedding_UI()
        print("Embedding")


init_UI()
# trace:当变量改变时，执行函数
selected_mode.trace("w", lambda *args: change_UI())
if __name__ == "__main__":
    window.mainloop()
