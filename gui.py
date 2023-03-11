from threading import Thread
import tkinter as tk
from webbrowser import open
import tkinter.messagebox as mes_box
from os import getpid, system
from tkinter import ttk
from Kuwo import Kuwo
from Wangyi import Wangyi
from play import play


class SetUI(object):
    ischanging = False
    last_pos = 0

    def __init__(self):
        self.song_num = ''
        self.paused = True
        self.all = None
        self.offset = None
        self.show_result_lyric = None
        self.show_comment = None
        self.show_result = None
        self.title = " 音乐播放器"
        self.ui_root = tk.Tk(className=self.title)
        self.ui_root.geometry(
            '{}x{}+0+50'.format(self.ui_root.winfo_screenwidth(), self.ui_root.winfo_screenheight() - 200))
        self.ui_url = tk.StringVar()
        self.ui_var = tk.IntVar()
        self.var = tk.IntVar()
        self.length = 0
        self.ui_root.after(100, self.timer)
        self.ui_var.set(1)

    # 设置ui界面
    def set_ui(self):
        """
        设置简易UI界面
        :return:
        """
        # Frame空间
        frame_1 = tk.Frame(self.ui_root)
        frame_2 = tk.Frame(self.ui_root)
        frame_3 = tk.Frame(self.ui_root)
        frame_4 = tk.Frame(self.ui_root)
        frame_5 = tk.Frame(self.ui_root)
        frame_6 = tk.Frame(self.ui_root)

        # ui界面中菜单设计
        ui_menu = tk.Menu(self.ui_root)
        self.ui_root.config(menu=ui_menu)
        file_menu = tk.Menu(ui_menu, tearoff=0)
        ui_menu.add_cascade(label='菜单', menu=file_menu)
        file_menu.add_command(label='使用说明', command=lambda: open('https://space.bilibili.com/35242527'))
        file_menu.add_command(label='关于作者', command=lambda: open('https://space.bilibili.com/35242527'))
        file_menu.add_command(label='退出', command=self.quit)

        # 控件内容设置
        choice_passageway = tk.Label(frame_1, text='请选择音乐搜索通道：', padx=10, pady=10)
        passageway_button_1 = tk.Radiobutton(frame_1, text='酷我', variable=self.ui_var, value=1, width=10, height=3)
        passageway_button_2 = tk.Radiobutton(frame_1, text='网易云', variable=self.ui_var, value=2, width=10, height=3)
        input_link = tk.Label(frame_2, text="请输入歌曲名或歌手：")
        self.entry_style = tk.Entry(frame_2, textvariable=self.ui_url, highlightcolor='red', highlightthickness=1,
                                    width=35)
        label2 = tk.Label(frame_2, text=" ")
        play_button = tk.Button(frame_2, text="搜索", font=('宋体', 10), fg='black', width=2, height=1,
                                command=self.search)
        label3 = tk.Label(frame_2, text=" ")
        # 表格样式
        columns = ("序号", "歌曲", "歌手", "专辑", "mvid")
        columns_comment = ('评论人网名', '评论内容', '点赞量', '评论时间')
        self.show_result = ttk.Treeview(frame_3, height=20, show="headings", columns=columns)
        self.show_comment = ttk.Treeview(frame_3, height=20, show="headings", columns=columns_comment)
        self.show_result_lyric = tk.Text(frame_3, height=33, bg="white", width=45)
        # 下载
        download_button = tk.Button(frame_4, text="下载", font=('楷体', 11), fg='black', width=6, height=1, padx=5,
                                    pady=5, command=self.downloadThread)
        # 翻页
        self.offset = tk.IntVar()
        self.offset.set(1)
        a01 = tk.Radiobutton(frame_4, text="第一页", font=('楷体', 11), fg='black', width=5, height=1, value=1,
                             variable=self.offset)
        a02 = tk.Radiobutton(frame_4, text="第二页", font=('楷体', 11), fg='black', width=5, height=1, value=2,
                             variable=self.offset)
        a03 = tk.Radiobutton(frame_4, text="第三页", font=('楷体', 11), fg='black', width=5, height=1, value=3,
                             variable=self.offset)
        a04 = tk.Radiobutton(frame_4, text="第四页", font=('楷体', 11), fg='black', width=5, height=1, value=4,
                             variable=self.offset)
        a05 = tk.Radiobutton(frame_4, text="第五页", font=('楷体', 11), fg='black', width=5, height=1, value=5,
                             variable=self.offset)
        a06 = tk.Radiobutton(frame_4, text="第六页", font=('楷体', 11), fg='black', width=5, height=1, value=6,
                             variable=self.offset)
        a07 = tk.Radiobutton(frame_4, text="第七页", font=('楷体', 11), fg='black', width=5, height=1, value=7,
                             variable=self.offset)
        a08 = tk.Radiobutton(frame_4, text="第八页", font=('楷体', 11), fg='black', width=5, height=1, value=8,
                             variable=self.offset)
        a09 = tk.Radiobutton(frame_4, text="第九页", font=('楷体', 11), fg='black', width=5, height=1, value=9,
                             variable=self.offset)
        a10 = tk.Radiobutton(frame_4, text="第十页", font=('楷体', 11), fg='black', width=5, height=1, value=10,
                             variable=self.offset)
        # 播放
        play = tk.Button(frame_6, text="播放", command=self.playThread, bg='white')
        play.pack(side='left', fill='x', padx=10, expand=True)
        pause = tk.Button(frame_6, text="暂停", command=pl.pause, bg='white')
        pause.pack(side='left', fill='x', padx=10, expand=True)
        unpause = tk.Button(frame_6, text="取消暂停", command=pl.unpause, bg='white')
        unpause.pack(side='left', fill='x', padx=10, expand=True)
        stop = tk.Button(frame_6, text="从头播放", command=self.reset, bg='white')
        stop.pack(side='left', fill='x', padx=10, expand=True)
        # 进度条
        self.elapse = ttk.Label(frame_5, text="")
        self.elapse.pack(side='left', padx=10)
        self.remain = ttk.Label(frame_5, text="")
        self.remain.pack(side='right', fill='x', padx=10)
        self.scale = ttk.Scale(frame_5, orient="horizontal", from_=0, to=0,
                               command=self.change_position, variable=self.var)
        # 控件布局
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        frame_5.pack(expand=True, fill='x')
        frame_6.pack(expand=True, fill='x')
        self.scale.pack(side='left', expand=True, fill='x')
        choice_passageway.grid(row=0, column=0)
        passageway_button_1.grid(row=0, column=1)
        passageway_button_2.grid(row=0, column=2)
        input_link.grid(row=0, column=0)
        self.entry_style.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        play_button.grid(row=0, column=3, ipadx=10, ipady=10)
        label3.grid(row=0, column=4)
        self.show_result.grid(row=0, column=4)
        self.show_comment.grid(row=0, column=8, padx=10)
        self.show_result_lyric.grid(row=0, column=0, padx=10, sticky='wn')
        download_button.grid(row=1, column=4)
        a01.grid(row=0, column=0)
        a02.grid(row=0, column=1)
        a03.grid(row=0, column=2)
        a04.grid(row=0, column=3)
        a05.grid(row=0, column=4)
        a06.grid(row=0, column=5)
        a07.grid(row=0, column=6)
        a08.grid(row=0, column=7)
        a09.grid(row=0, column=8)
        a10.grid(row=0, column=9)

        # 设置表头
        self.show_result.heading("序号", text="序号")
        self.show_result.heading("歌手", text="歌手")
        self.show_result.heading("歌曲", text="歌曲")
        self.show_result.heading("专辑", text="专辑")
        self.show_result.heading("mvid", text="mvid")
        self.show_comment.heading("评论人网名", text="评论人网名")
        self.show_comment.heading("评论内容", text="评论内容")
        self.show_comment.heading("点赞量", text="点赞量")
        self.show_comment.heading("评论时间", text="评论时间")
        # 设置列
        self.show_result.column("序号", width=150, anchor='w')
        self.show_result.column("歌手", width=150, anchor='w')
        self.show_result.column("歌曲", width=250, anchor='w')
        self.show_result.column("专辑", width=250, anchor='w')
        self.show_result.column("mvid", width=50, anchor='e')
        self.show_comment.column("评论人网名", width=100, anchor='w')
        self.show_comment.column("评论内容", width=150, anchor='w')
        self.show_comment.column("评论时间", width=100, anchor='w')
        self.show_comment.column("点赞量", width=50, anchor='w')

        # 事件绑定
        self.show_result.bind('<Button-1>', self.loadInfoThread)
        self.show_result.bind('<Double-Button-1>', self.downloadEvent)
        self.entry_style.bind('<Return>', self.searchEvent)

    def loop(self):
        self.set_ui()
        self.ui_root.resizable(False, False)  # 禁止修改窗口大小
        self.ui_root.mainloop()

    # 重写父类退出函数，退出前杀掉未结束的进程
    def quit(self):
        pid = getpid()
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        try:
            system(cmd)
        except Exception as e:
            print(e, 'abcde')
        self.ui_root.quit()

    # 判断进度条是否被改变
    def change_position(self, value):
        self.ischanging = True

    # 控制进度条
    def timer(self):
        if self.ischanging:
            self.ischanging = False
            self.last_pos = self.var.get() - pl.get_pos() / 1000
            pl.set_pos(self.var.get())
        else:
            self.var.set(pl.get_pos() / 1000 + self.last_pos)
            self.elapse.configure(text=int(pl.get_pos() / 1000 + self.last_pos))
        self.ui_root.after(200, self.timer)

    def reset(self):
        pl.reset()
        self.last_pos = 0

    def searchEvent(self, event):
        self.search()

    def search(self):
        # 清空treeview表格数据
        for item in self.show_result.get_children():
            self.show_result.delete(item)
        search_input = self.ui_url.get()
        if len(search_input) > 0:
            try:
                if self.ui_var.get() == 1:
                    self.all = kw.search(search_input, self.offset.get())
                elif self.ui_var.get() == 2:
                    self.all = wy.search(search_input, (self.offset.get() - 1) * 30)
                if len(self.all) <= 0:
                    mes_box.showerror(title='错误', message='搜索: {} 不存在或在该页不存在.'.format(search_input))
                else:
                    for i in range(len(self.all) - 1):
                        all0 = self.all[i + 1]
                        self.show_result.insert('', i, values=(all0['歌曲id'], all0['歌曲名称'],
                                                               all0['歌手姓名'], all0['专辑名称'], all0['mvid']))
            except TimeoutError:
                mes_box.showerror(title='错误', message='搜索超时，请重新输入后再搜索！')
        else:
            mes_box.showerror(title='错误', message='未输入需查询的歌曲或歌手，请输入后搜索！')

    # 给加载歌词和评论开辟一个进程
    def loadInfoThread(self, event):
        t = Thread(target=self.loadInfo)
        t.start()

    def loadInfo(self):
        # 清空treeview表格数据
        for item in self.show_comment.get_children():
            self.show_comment.delete(item)
        self.show_result_lyric.delete(0.0, 'end')
        # treeview中的左键单击
        for item in self.show_result.selection():
            item_text = self.show_result.item(item, "values")
            self.song_num = item_text[0]
        if self.ui_var.get() == 1:
            try:
                lyric = kw.get_lyric(self.song_num)
                comment = kw.get_comment(self.song_num, 1)
                self.show_result_lyric.insert(0.0, lyric)
                for i in range(len(comment) - 1):
                    self.show_comment.insert('', i,
                                             values=(comment[i + 1]['评论人网名'], comment[i + 1]['评论内容'],
                                                     comment[i + 1]['点赞量'], comment[i + 1]['评论时间']))
            except:
                mes_box.showerror("错误", "无法加载数据")
        elif self.ui_var.get() == 2:
            try:
                lyric = wy.get_lyric(self.song_num)
                comment = wy.get_comment(self.song_num)
                self.show_result_lyric.insert(0.0, lyric)
                for i in range(len(comment) - 1):
                    self.show_comment.insert('', i,
                                             values=(comment[i]['评论人网名'], comment[i]['评论内容'],
                                                     comment[i]['点赞量'], comment[i]['评论时间']))
            except:
                mes_box.showerror("错误", "无法加载数据")

    # 给下载功能开辟一个进程
    def downloadEvent(self, event):
        self.downloadThread()

    def downloadThread(self):
        t = Thread(target=self.download)
        t.start()

    def download(self):
        for item in self.show_result.selection():
            item_text = self.show_result.item(item, "values")
            self.song_num = item_text[0]
            self.song_name = item_text[1]
            self.mv_num = item_text[4]
        if self.ui_var.get() == 1:
            try:
                kw.download(self.song_num)
                mes_box.showinfo("成功", f'{self.song_name}下载成功')
                self.status = 1
            except:
                mes_box.showerror("错误", "无法下载歌曲")
        elif self.ui_var.get() == 2:
            try:
                flag = wy.download(self.song_num)
                if flag != 0:
                    mes_box.showinfo("成功", f'{self.song_name}下载成功')
                if flag == 0:
                    if self.mv_num != '0':
                        self.status = wy.downloadMV(self.mv_num, self.song_num)
                        if self.status != 0:
                            mes_box.showinfo("成功", f'{self.song_name}下载成功')
                        else:
                            mes_box.showinfo("失败", f'{self.song_name}无法下载')
                    else:
                        mes_box.showerror("错误", "暂时无法获取该音频资源，请过段时间搜索或者购买专辑")
            except:
                mes_box.showerror("错误", "无法下载歌曲")

    # 播放音乐需要多开一个进程
    def playThread(self):
        t = Thread(target=self.play)
        t.start()

    def play(self):
        for item in self.show_result.selection():
            item_text = self.show_result.item(item, "values")
            self.song_num = item_text[0]
        if self.ui_var.get() == 1:
            filename = f'./KuwoMusic/{self.song_num}.mp3'
            self.play_chose(filename)
        elif self.ui_var.get() == 2:
            filename = f'./WangyiMusic/{self.song_num}.mp3'
            self.play_chose(filename)

    def play_chose(self, filename):
        if len(self.song_num) > 0:
            try:
                pl.play(filename)
                self.length = pl.get_length()
                if self.ui_var.get() == 2:
                    self.length /= 2
            except:
                self.download()
                if self.status == 1:
                    pl.play(filename)
                    self.length = pl.get_length() / 2
                else:
                    mes_box.showerror("错误", "无法播放当前选择的歌曲，请选择其他个歌曲")
                    self.length = 0
            self.scale.configure(from_=0, to=self.length)
            self.remain.configure(text=self.length)
            self.last_pos = 0
        else:
            mes_box.showerror("错误", "请选择想要播放的歌曲")


kw = Kuwo()
wy = Wangyi()
pl = play()

