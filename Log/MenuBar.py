"""
设计：
    菜单栏：
        文件：
            -打开
            -保存
            -退出
        模式：
            -Prompt-based
            -Fine-tuning
        登录：(已删除)
            -API_KEY
        清空：
            -清空历史记录
    设计每一个菜单项的功能函数：
        -打开：open_file()
        -保存：save_file()
        -退出：window.quit()
        -Prompt-based：chat_UI()
        -Fine-tuning：load_UI()
        -API_KEY：login()
输出：
    1.selected_mode：模式选择（外部获取：selected_mode.get()）
    
"""
