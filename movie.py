import moviepy.editor as mp
from os import remove


class movie:
    def mp4tomp3(self, mp4_filepath):
        # 选择MP4文件
        mp4_file = mp4_filepath
        # 通过替换文件名后缀，生成Mp3文件的新地址
        mp3_file = mp4_file.replace('.mp4', '.mp3')
        # 由于在读取无画面的Mp4文件的时候，系统会报错，从而中断程序运行，所以用try语句，先尝试按正常方式读取MP4
        try:
            # 正常情况下，应该使用VideoFileClip来读取Mp4文件，并重新生成Mp3文件，代码如下：
            mp.VideoFileClip(mp4_file).audio.write_audiofile(mp3_file)
            # 但是由于从Youtube下载的仅包含音频的文件，其实并不是MP4文件，会出现 self.fps = infos['video_fps'] 的关键错误，
            # 所以不能采用这种方式读取，应该考虑用音频的方式读取
        except:
            # 如果用正常的方式读取MP4出现错误，则采用读取音频的方式获取文件中的内容，再作输出。
            # 用音频的方式读取从Youtube下载的Mp4文件，并输出为mp3 音频文件。
            mp.AudioFileClip(mp4_file).write_audiofile(mp3_file)
        # 转换为MP3文件后，如果不再需要原Mp4文件可以直接删除该Mp4文件
        remove(mp4_file)
