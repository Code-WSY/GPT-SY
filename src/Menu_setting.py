from Box_Dialog import *
from Box_Input import *
from Box_Message import *
# -----------------------------------------------------------------------------------#
font_size_range= [4, 25]
def set_font():
    Dialog_box.config(font=(selected_setting_font_Dialog_box.get(), selected_setting_fontsize_Dialog_box.get()))
    Input_box.config(font=(selected_setting_font_Input_box.get(), selected_setting_fontsize_Input_box.get()))
    Message_box.config(font=(selected_setting_font_message_box.get(), selected_setting_fontsize_message_box.get()))
def set_color():
    Dialog_box.config(bg=selected_setting_color_bg_Dialog_box.get(), fg=selected_setting_color_fg_Dialog_box.get())
    Input_box.config(bg=selected_setting_color_bg_Input_box.get(), fg=selected_setting_color_fg_Input_box.get())
    Message_box.config(bg=selected_setting_color_bg_message_box.get(), fg=selected_setting_color_fg_message_box.get())

# -----------------------------------------------------------------------------------#
# 初始化字体和字号
font_list = [
    "Arial",
    "Calibri",
    "Cambria",
    "Comic Sans MS",
    "Courier New",
    "Georgia",
    "Helvetica",
    "Impact",
    "Lucida Console",
    "Lucida Sans Unicode",
    "Palatino",
    "Tahoma",
    "Times New Roman",
    "Trebuchet MS",
    "Verdana",
    "Consolas",
    "微软雅黑",
    "宋体",
    "楷体",
    "黑体",
    "仿宋",
    "隶书",
    "幼圆",
    "方正舒体",
    "方正姚体"
]
#颜色
color_list = [
    "white",
    "black",
    "red",
    "green",
    "blue",
    "yellow",
    "cyan",
    "magenta",
    "gray",
    "lightgray",
    "darkgray",
    "orange",
    "pink",
    "purple",
    "brown",
    "gold",
    "silver",
    "lightblue",
    "lightgreen",
    "lightyellow",
    "lightcyan",
    "lightpink",
    "darkblue",
    "darkgreen",
    "darkcyan",
    "darkmagenta",
]
# -----------------------------------------------------------------------------------#
# 初始化字体和字号和颜色
selected_setting_font_Dialog_box = tk.StringVar()
selected_setting_font_Dialog_box.set(font_style)
selected_setting_fontsize_Dialog_box = tk.StringVar()
selected_setting_fontsize_Dialog_box.set(font_size)
selected_setting_color_bg_Dialog_box = tk.StringVar()
selected_setting_color_bg_Dialog_box.set(colors[0])
selected_setting_color_fg_Dialog_box = tk.StringVar()
selected_setting_color_fg_Dialog_box.set(colors[1])
selected_setting_font_message_box = tk.StringVar()
selected_setting_font_message_box.set(font_style)
selected_setting_fontsize_message_box = tk.StringVar()
selected_setting_fontsize_message_box.set(font_size)
selected_setting_color_bg_message_box = tk.StringVar()
selected_setting_color_bg_message_box.set(colors[2])
selected_setting_color_fg_message_box = tk.StringVar()
selected_setting_color_fg_message_box.set(colors[3])
selected_setting_font_Input_box = tk.StringVar()
selected_setting_font_Input_box.set(font_style)
selected_setting_fontsize_Input_box = tk.StringVar()
selected_setting_fontsize_Input_box.set(font_size)
selected_setting_color_bg_Input_box = tk.StringVar()
selected_setting_color_bg_Input_box.set(colors[4])
selected_setting_color_fg_Input_box = tk.StringVar()
selected_setting_color_fg_Input_box.set(colors[5])


# 创建一个菜单
filemenu_setting = tk.Menu(menubar, tearoff=0)
# 将菜单添加到菜单栏
#menubar.add_cascade(label="外观", menu=filemenu_setting)

#创建三个菜单：字体，字号，颜色
menu_setting_font = tk.Menu(filemenu_setting, tearoff=0)
menu_setting_size = tk.Menu(filemenu_setting, tearoff=0)
menu_setting_color = tk.Menu(filemenu_setting, tearoff=0)
#将三个菜单添加到setting
filemenu_setting.add_cascade(label="字体", menu=menu_setting_font)
filemenu_setting.add_cascade(label="字号", menu=menu_setting_size)
filemenu_setting.add_cascade(label="颜色", menu=menu_setting_color)

# ------------------------------字体-------------------------------------------------#
#在字体菜单中添加子菜单:对话框，输入框，消息框
menu_setting_font_Dialog_box = tk.Menu(menu_setting_font, tearoff=0)
menu_setting_font_Input_box = tk.Menu(menu_setting_font, tearoff=0)
menu_setting_font_message_box = tk.Menu(menu_setting_font, tearoff=0)
#将字体列表添加
menu_setting_font.add_cascade(label="对话框", menu=menu_setting_font_Dialog_box)
for i in font_list:
    menu_setting_font_Dialog_box.add_radiobutton(label=i, variable=selected_setting_font_Dialog_box, command=set_font)
menu_setting_font.add_cascade(label="消息框", menu=menu_setting_font_message_box)
for i in font_list:
    menu_setting_font_message_box.add_radiobutton(label=i, variable=selected_setting_font_message_box, command=set_font)
menu_setting_font.add_cascade(label="输入框", menu=menu_setting_font_Input_box)
for i in font_list:
    menu_setting_font_Input_box.add_radiobutton(label=i, variable=selected_setting_font_Input_box, command=set_font)

# --------------------------------字号---------------------------------------------------#
#在字号菜单中添加子菜单:对话框，输入框，消息框
menu_setting_size_Dialog_box = tk.Menu(menu_setting_size, tearoff=0)
menu_setting_size_Input_box = tk.Menu(menu_setting_size, tearoff=0)
menu_setting_size_message_box = tk.Menu(menu_setting_size, tearoff=0)

menu_setting_size.add_cascade(label="对话框", menu=menu_setting_size_Dialog_box)
for i in range(font_size_range[0], font_size_range[1]):
    menu_setting_size_Dialog_box.add_radiobutton(label=i, variable=selected_setting_fontsize_Dialog_box,command=set_font)

menu_setting_size.add_cascade(label="消息框", menu=menu_setting_size_message_box)
for i in range(font_size_range[0], font_size_range[1]):
    menu_setting_size_message_box.add_radiobutton(label=i, variable=selected_setting_fontsize_message_box,command=set_font)

menu_setting_size.add_cascade(label="输入框", menu=menu_setting_size_Input_box)
for i in range(font_size_range[0], font_size_range[1]):
    menu_setting_size_Input_box.add_radiobutton(label=i, variable=selected_setting_fontsize_Input_box,command=set_font)



# -----------------------------------------------------------------------------------#
#在颜色菜单中添加子菜单:字体颜色，背景颜色
menu_setting_font_color = tk.Menu(menu_setting_color, tearoff=0)
menu_setting_background_color = tk.Menu(menu_setting_color, tearoff=0)
#加入到颜色菜单
menu_setting_color.add_cascade(label="字体颜色", menu=menu_setting_font_color)
menu_setting_color.add_cascade(label="背景颜色", menu=menu_setting_background_color)

# --------------------------------字体颜色--------------------------------------------#
#在字体颜色菜单中添加子菜单:对话框，输入框，消息框
menu_setting_font_color_Dialog_box = tk.Menu(menu_setting_font_color, tearoff=0)
menu_setting_font_color_Input_box = tk.Menu(menu_setting_font_color, tearoff=0)
menu_setting_font_color_message_box = tk.Menu(menu_setting_font_color, tearoff=0)

#加入到字体颜色菜单
menu_setting_font_color.add_cascade(label="对话框", menu=menu_setting_font_color_Dialog_box)
for i in color_list:
    menu_setting_font_color_Dialog_box.add_radiobutton(label=i, variable=selected_setting_color_fg_Dialog_box, command=set_color)

menu_setting_font_color.add_cascade(label="输入框", menu=menu_setting_font_color_Input_box)
for i in color_list:
    menu_setting_font_color_Input_box.add_radiobutton(label=i, variable=selected_setting_color_fg_Input_box, command=set_color)

menu_setting_font_color.add_cascade(label="消息框", menu=menu_setting_font_color_message_box)
for i in color_list:
    menu_setting_font_color_message_box.add_radiobutton(label=i, variable=selected_setting_color_fg_message_box, command=set_color)

# ---------------------------------背景颜色------------------------------------------#
#在背景颜色菜单中添加子菜单:对话框，输入框，消息框
menu_setting_background_color_Dialog_box = tk.Menu(menu_setting_background_color, tearoff=0)
menu_setting_background_color_Input_box = tk.Menu(menu_setting_background_color, tearoff=0)
menu_setting_background_color_message_box = tk.Menu(menu_setting_background_color, tearoff=0)

menu_setting_background_color.add_cascade(label="对话框", menu=menu_setting_background_color_Dialog_box)
for i in color_list:
    menu_setting_background_color_Dialog_box.add_radiobutton(label=i, variable=selected_setting_color_bg_Dialog_box, command=set_color)

menu_setting_background_color.add_cascade(label="消息框", menu=menu_setting_background_color_message_box)
for i in color_list:
    menu_setting_background_color_message_box.add_radiobutton(label=i, variable=selected_setting_color_bg_message_box, command=set_color)

menu_setting_background_color.add_cascade(label="输入框", menu=menu_setting_background_color_Input_box)
for i in color_list:
    menu_setting_background_color_Input_box.add_radiobutton(label=i, variable=selected_setting_color_bg_Input_box, command=set_color)



# -----------------------------------------------------------------------------------#


