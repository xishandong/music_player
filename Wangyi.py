from os import mkdir
from os import path
from execjs import compile
from requests import get
from requests import post
from movie import movie

xx = '010001'
yy = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
zz = '0CoJUm6Qyw8W8jud'
cookies = {
    'MUSIC_U': '在这里输入vip账户cookie',
}
headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}
params = {
    'csrf_token': '在这里输入vip账号的token',
}


def replace_lastChar(former_str, replacechar):
    return former_str[:-1] + replacechar


class Wangyi:

    def __init__(self):
        pass

    def search(self, name, offset):
        i3x = '{"hlpretag":"<span class=\\"s-fc7\\">","hlposttag":"</span>","id":"160947","s":"%s","type":"1","offset":"%s","total":"true","limit":"30","csrf_token":""}'
        i3x = format(i3x % (name, offset))
        param = compile(open('demo.js', 'r', encoding='utf-8').read()).call('d', i3x, xx, yy, zz)
        data = {
            'params': param['encText'],
            'encSecKey': param['encSecKey']
        }
        response = post(
            'https://music.163.com/weapi/cloudsearch/get/web',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        try:
            total = response.json()["result"]['songCount']
            songs = response.json()['result']['songs']
            Info = [total]
            for song in songs:
                songInfo = {
                    '歌曲id': song['id'],
                    '歌曲名称': song['name'],
                    '歌手姓名': song['ar'][0]['name'],
                    '专辑名称': song['al']['name'],
                    'mvid': song['mv']
                }
                Info.append(songInfo)
        except:
            Info = []
        return Info

    def get_lyric(self, id):
        i3x = '{"id":"%s","lv":-1,"tv":-1,"csrf_token":""}'
        i3x = format(i3x % id)
        param = compile(open('demo.js', 'r', encoding='utf-8').read()).call('d', i3x, xx, yy, zz)
        data = {
            'params': param['encText'],
            'encSecKey': param['encSecKey']
        }
        response = post('https://music.163.com/weapi/song/lyric', params=params, cookies=cookies,
                        headers=headers,
                        data=data)
        res = response.json()["lrc"]['lyric']
        try:
            resp = response.json()["tlyric"]['lyric']
        except:
            resp = ''
        res += resp
        return res

    def get_comment(self, id):
        id = str(id)
        i3x = {
            'csrf_token': "",
            'cursor': '-1',
            'offset': "0",
            'orderType': "1",
            'pageNo': "1",
            'pageSize': "20",
            'rid': f"R_SO_4_{id}",
            'threadId': f"R_SO_4_{id}",
        }
        param = compile(open('demo.js', 'r', encoding='utf-8').read()).call('md', i3x, xx, yy, zz)
        data = {
            'params': param['encText'],
            'encSecKey': param['encSecKey']
        }
        datas = post('https://music.163.com/weapi/comment/resource/comments/get', params=params,
                     headers=headers, data=data, cookies=cookies).json()
        userInfos = datas["data"]["comments"]
        infos = []
        for info in userInfos:
            info1 = info["user"]
            userInfo = {
                '评论人网名': info1['nickname'],
                '评论时间': info['timeStr'],
                '点赞量': info['likedCount'],
                '评论内容': info['content'],
            }
            infos.append(userInfo)
        return infos

    def download(self, id):
        mv = movie()
        url = self.get_musicUrl(id)
        if url != 'error':
            response = get(
                url=url,
                headers=headers,
            )
            if str(response) == '<Response [403]>':
                new_url = replace_lastChar(url, 'r')
                response = get(
                    url=new_url,
                    headers=headers,
                )
            if not path.exists('./WangyiMusic'):
                mkdir("./WangyiMusic")
            with open(f'./WangyiMusic/{id}.mp4', 'wb') as fp:
                fp.write(response.content)
            mv.mp4tomp3(f'./WangyiMusic/{id}.mp4')
            return 1
        else:
            return 0

    def get_musicUrl(self, mid):
        i3x = '{"ids":"[%s]","level":"standard","encodeType":"aac","csrf_token":""}'
        i3x = format(i3x % mid)
        param = compile(open('demo.js', 'r', encoding='utf-8').read()).call('d', i3x, xx, yy, zz)
        data = {
            'params': param['encText'],
            'encSecKey': param['encSecKey']
        }
        response = post(
            'https://music.163.com/weapi/song/enhance/player/url/v1',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        Url = response.json()["data"][0]['url']
        if Url is None:
            return 'error'
        return Url

    def downloadMV(self, id, mid):
        mv = movie()
        id = int(id)
        i3x = '{"id":"%d","r":"1080","csrf_token":""}'
        i3x = format(i3x % id)
        url = 'https://music.163.com/weapi/song/enhance/play/mv/url'
        param = compile(open('demo.js', 'r', encoding='utf-8').read()).call('d', i3x, xx, yy, zz)
        data = {
            'params': param['encText'],
            'encSecKey': param['encSecKey']
        }
        response = post(url,params=params,cookies=cookies,headers=headers,data=data)
        try:
            url = response.json()['data']['url']
        except:
            url = response.json()['urls'][0]['url']
        if url is not None:
            res = get(url, stream=True)
            if not path.exists('./WangyiMusic'):
                mkdir("./WangyiMusic")
            with open(f'./WangyiMusic/{mid}.mp4', 'wb') as fp:
                fp.write(res.content)
            mv.mp4tomp3(f'./WangyiMusic/{mid}.mp4')
            return 1
        else:
            return 0


if __name__ == '__main__':
    wy = Wangyi()
    # Info = wy.search('iu', 0)
    # print(Info)
    # wy.download(1835283134)
    wy.downloadMV(534350, 400581054)
