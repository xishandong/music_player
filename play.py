from pygame import mixer
from eyed3 import load


class play:

    def __init__(self):
        mixer.init()
        self.music = mixer.music
        self.file = None
        self.length = None

    # 播放
    def play(self, filename):
        self.file = filename
        mp3Info = load(filename)
        self.length = mp3Info.info.time_secs
        self.music.load(filename)
        self.music.play(loops=-1)  # 播放

    # 重置
    def reset(self):
        self.music.stop()
        self.play(self.file)

    # 暂停
    def pause(self):
        self.music.pause()

    # 取消暂停
    def unpause(self):
        self.music.unpause()

    # 停止
    def stop(self):
        self.music.stop()

    # 获取音频长度
    def get_length(self):
        return self.length

    # 定位当前播放时间
    def get_pos(self):
        return self.music.get_pos()

    # 设置当前播放时间
    def set_pos(self, value=0):
        self.music.rewind()
        self.music.set_pos(value)


pl = play()
pl.file = './MV/14572401.mp3'
# pl.play('./KuwoMusic/440616.mp3')
