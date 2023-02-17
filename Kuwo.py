from os import mkdir
from os import path
from requests import get as gets


class Kuwo:

    def __init__(self):
        self.response = None
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept - encoding': 'gzip, deflate',
            'accept - language': 'zh - CN, zh;q = 0.9',
            'cache - control': 'no - cache',
            'Connection': 'keep-alive',
            'csrf': 'HH3GHIQ0RYM',
            'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/99.0.4844.51 Safari/537.36',
            'Cookie': '_ga=GA1.2.218753071.1648798611; _gid=GA1.2.144187149.1648798611; _gat=1; '
                      'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1648798611; '
                      'Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1648798611; kw_token=HH3GHIQ0RYM'
        }

    def search(self, keyword, pageNum):
        params = {
            'key': keyword,
            'pn': str(pageNum),
            'rn': '30',
            'httpsStatus': '1',
            'reqId': 'd1e64d70-a2f2-11ed-8254-9b005a05c7eb',
        }

        self.response = gets(
            'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord',
            params=params,
            headers=self.headers,
            verify=False,
        )
        total = self.response.json()["data"]['total']
        songs = self.response.json()['data']['list']
        Info = [total]
        for song in songs:
            songInfo = {
                '歌曲id': song['rid'],
                '歌曲名称': song['name'],
                '歌手姓名': song['artist'],
                '专辑名称': song['album'],
                'mvid': song['mvpayinfo']['vid']
            }
            Info.append(songInfo)
        return Info

    def download(self, rid):
        songs_req_id = self.response.json()['reqId']
        song_rid = rid
        music_url = 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid={}&type=convert_url3' \
                    '&httpsStatus=1&reqId={}' \
            .format(song_rid, songs_req_id)
        response_data = gets(music_url).json()
        song_url = response_data['data'].get('url')
        if not path.exists('./KuwoMusic'):
            mkdir("./KuwoMusic")
        resp = gets(song_url)
        with open(f'./KuwoMusic/{song_rid}.mp3', 'wb') as fp:
            fp.write(resp.content)

    def get_lyric(self, rid):
        songs_req_id = self.response.json()['reqId']
        params = {
            'musicId': rid,
            'httpsStatus': '1',
            'reqId': songs_req_id,
        }
        response = gets('http://m.kuwo.cn/newh5/singles/songinfoandlrc', params=params, headers=self.headers,
                                verify=False).json()["data"]["lrclist"]
        lyrics = ''
        for lyric in response:
            lyrics += lyric['lineLyric']
            lyrics += '\n'

        return lyrics

    def get_comment(self, rid, page):
        songs_req_id = self.response.json()['reqId']
        params = {
            'type': 'get_comment',
            'f': 'web',
            'page': page,
            'rows': '20',
            'digest': '15',
            'sid': rid,
            'uid': '0',
            'prod': 'newWeb',
            'httpsStatus': '1',
            'reqId': songs_req_id,
        }
        resp = gets('http://www.kuwo.cn/comment', params=params, headers=self.headers,
                            verify=False).json()
        totalPage = resp['totalPage']
        comments = resp["rows"]
        infos = [totalPage]
        for row in comments:
            userInfo = {
                '评论人网名': row['u_name'],
                '评论时间': row['time'],
                '点赞量': row['like_num'],
                '评论内容': row['msg'],
            }
            infos.append(userInfo)
        return infos


if __name__ == '__main__':
    cw = Kuwo()
    Info = cw.search('iu', 1)
    cw.download('23683150')
    lyric = cw.get_lyric('198967906')
    comment = cw.get_comment('23683150', '3')
    print(Info)
    print(lyric)
    print(comment)
