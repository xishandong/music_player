# Title

***

基于tkinter的可视化界面，音乐内容为爬虫爬取，包含酷我音乐和网易云音乐的api

# Install

***

    需要nodejs环境，来调用js代码，网易云的资源需要逆向获取
    npm install crypto
    npm install jsdom
    pip install moviepy
    pip install eyed3
    pip indtsll tkinter
    pip indtsll pygame
    现在安装包已经安装好crypto和jsdom环境，只需要在电脑上安装有nodejs即可

# Useage

***

环境配置好后，运行main.py即可出现可视化界面

选择好接口之后点击搜索即可展示歌曲信息，单击歌曲会出现歌词以及评论信息，双击可以下载歌曲

下方播放按钮单击播放歌曲，会先下载到本地进行播放

进度条可以拖动选择播放事件

如果没有nodejs环境，只能运行酷我的接口，不能运行网易云的接口

# Run

***
![image](https://user-images.githubusercontent.com/100206449/219686284-d8dbe446-59f1-4cc8-bdca-d961c3c23f91.png)
![image](https://user-images.githubusercontent.com/100206449/219686324-61f80988-7175-48cd-ba56-6e03c781e342.png)
![image](https://user-images.githubusercontent.com/100206449/219686382-8061ec40-f4c3-4a7f-9f69-f91439c2b433.png)
</br>演示播放付费购买专辑歌曲</br>
![image](https://user-images.githubusercontent.com/100206449/219686598-fbeace3c-d7cc-4caa-aedf-2ca5c5c5bd95.png)

# 注意

***
网易云歌曲因为音频头增加了一段cover，所以无法通过pygame播放，处理方法使用moviepy，下载的时候下载成MP4格式
</br>然后转化为MP3播放。
</br>如果没有再Wangyi.py中增加vip账户cookie，但是这首歌有mv也可以得到MP3音频
</br>由于使用了爬虫，请大家遵守网络安全，合法使用
