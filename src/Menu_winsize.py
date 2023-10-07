from UI import *
from Box_Dialog import *
from Box_Message import *
from Box_Input import *



# -----------------------------------------------------------------------------------#
# -----------------------------------------------------------------------------------#
def reset_winsize():
    scale=float(scale_var.get().split("%")[0])/100
    # 1
    Dialog_box.config(width=int(Dialog_box_size[0] * scale),
                      height=int(Dialog_box_size[1] * scale), highlightthickness=2 * scale)

    Dialog_box.config(font=(font_style, int(font_size * scale)))
    # 2
    Message_box.config(width=int(message_box_size[0] * scale),
                       height=int(message_box_size[1] * scale), highlightthickness=8 * scale)

    Message_box.config(font=(font_style, int(font_size * scale)))

    # 3
    temperature_label.config(width=int(temperature_label_size[0] * scale),
                             height=temperature_label_size[1])
    temperature_label.config(font=(entry_font[0],int(entry_font[1]*scale)))
    temperature_box.config(width=temperature_box_size[0])
    temperature_box.config(font=(entry_font[0],int(entry_font[1]*scale)))
    max_tokens_label.config(width=int(max_tokens_label_size[0] * scale),
                            height=max_tokens_label_size[1])
    max_tokens_label.config(font=(entry_font[0],int(entry_font[1]*scale)))
    max_tokens_box.config(width=int(max_tokens_box_size[0] * scale))
    max_tokens_box.config(font=(entry_font[0],int(entry_font[1]*scale)))
    # 4
    Label_model.config(width=int(Label_model_size[0] * scale), height=int(Label_model_size[1] * scale))
    Label_model.config(font=(cbox_font[0],int(cbox_font[1])))
    model_list.config(width=int(ComboBox_model_size[0] * scale))
    model_list.config(font=(cbox_font[0],int(cbox_font[1]* scale)))

    Label_func.config(width=int(Label_func_size[0] * scale), height=int(Label_func_size[1] * scale))
    Label_func.config(font=(cbox_font[0],int(cbox_font[1])))
    prompts_list.config(width=int(ComboBox_func_size[0] * scale))
    prompts_list.config(font=(cbox_font[0],int(cbox_font[1]* scale)))
    # 5
    Input_box.config(width=int(Input_box_size[0] * scale),
                     height=int(Input_box_size[1] * scale), highlightthickness=4 * scale)
    Input_box.config(font=(font_style, int(font_size * scale)))
    # 6
    # 更新窗口
    window.update()


filemenu_winsize = tk.Menu(menubar, tearoff=0)
max_scale=200
min_scale=20
step=10
scale_var=tk.StringVar()
for i in range(min_scale,max_scale,step):
    scale_var.set("100%")
    label_size= str(i)+"%"
    filemenu_winsize.add_radiobutton(label=label_size, variable=scale_var, command=lambda: reset_winsize())


