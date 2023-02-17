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
    'MUSIC_U': '5451bcd0097d856694d08b196528b8a90267b7bf2fe2b56867a2139741527167993166e004087dd327586c5555c1631aaac449237689908bb8a169e60ca9265e6b6f7b8785862331a0d2166338885bd7',
    # 'e302082b51e8da6685dbb3aaf926a6db0267b7bf2fe2b56841d31edd145a3021993166e004087dd3360b2c74791823624d9912ada5e0062f84ee70de9e8757ca6b324248e5c93b0ed4dbf082a8813684'
    # '5451bcd0097d856694d08b196528b8a90267b7bf2fe2b56867a2139741527167993166e004087dd327586c5555c1631aaac449237689908bb8a169e60ca9265e6b6f7b8785862331a0d2166338885bd7'
}
headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    # 'cookie': 'P_INFO=18608219667|1659842485|1|study|00&99|null&null&null#sic&510500#10#0|&0||18608219667; __bid_n=184855102dc3deb72f4207; FPTOKEN=72X4JbpCu5OusTIYuHrCSGgjkuVlm7w0d2wuZhf+LU7tCP8d2MdyrBKXbvhWmMBQ4PKKvkagbJ51CrfoDP1FK92ujmpUvUgInBgFojtQGyau97Tpz4WSuTnUiS6fizwTsHkskf4I2RdqrQCBQFHtYEtOnpD8RQadQBQbKXjwRw/nR1DO+23Y6vcDZbzGXAtLl6Xm4RhhE95S1srhGEVyjbIKGwnyHfiAJRmy6s7aRwJy06lrHyqXmRGsl75msfYuOSPVdoqKR50yZOaIXkE9+reLCp71sfWzH6IyIuEd0tOfp2DIGQOXRwPNsfJIVhnzOmQETOjXTciGSjjqjpcB1HvV6MJEPoJTz9jtA9xEAbpdqzfdbXWd1t66tiWvMdSwOdRJufrVWLb5Kp45jXCEMg==|4i8C4fx+LJpM3RJOqHD5D/gktdXKtOZsPzv+3ONA2vU=|10|4784ce007f1eaa4073c5660cfcf93bfa; vinfo_n_f_l_n3=0f5eba99d02a8a90.1.12.1673163354239.1673496764827.1673499976392; _iuqxldmzr_=32; _ntes_nnid=f37f7a44b589883a8947dd6fca21229a,1674451825593; _ntes_nuid=f37f7a44b589883a8947dd6fca21229a; NMTID=00OpWJ6K25R-OBw305HoKc7iw1Bum4AAAGF3Rs0ZA; WEVNSM=1.0.0; WNMCID=pozalx.1674451825917.01.0; WM_TID=%2BrY9QzhJ44xAQUUBAFKBIufmFp9POPoJ; WM_NI=FZifNkYxQ5%2BsOc7UcO0iL2%2BysJb4NBTGZYVM84rxk4hET0mDURlUNWjbwIRjhuX5QLHgQRO1zicH%2BhhGxyGw5XoZKrhco9d3otC6cYq4jWsQGVO9ozzTlzitaHjcs4mocU0%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb0cf6f898e0096fc4eada88fb2d54f838a9fadc147edb99d98bc46bab7a9abe52af0fea7c3b92a8686a787cd619ba89fd6aa798dbdf9b6e245f4b784d3aa73b196aed5cd4a989996bad547fcecbe99ea40ac9b9cd1f050978ea4b6cd5daabeb9aad162acab98d6d4488cb99fb3ce3bbab7ada9aa64ac99b89ac67df788a1bbca7aacbda1dae739adac8dd7e253b3eca6b8f25b858a81daee72ba8ca49bec80a398a684f240afb1adb6b337e2a3; playerid=49334466; JSESSIONID-WYYY=o%5CyijWemMcjioZJ1fsF%5C9sl57SgrkFa6o9yMUd4dnNshvo11uAMNJOV%5CbIJYe0VSo2xpDI0mc%2FUvQX2xQpe1U2JCJDfEwIvO%2FhMo%5CGHCcfZI3r%2BzseRcOnnrt8NsZwR53VNvUYHNp6sYzWTZEiYbYJ9D4%2Fv%2BIUCnGPv3mypr1JBIDaev%3A1674532481499',
    'origin': 'https://music.163.com',
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
    'csrf_token': 'd5e1f281f7b6f7ff2caf0af810f347d7',
}


def replace_lastChar(former_str, replacechar):
    return former_str[:-1] + replacechar


class Wangyi:

    def __init__(self):
        pass

    def search(self, name, offset):
        i3x = '{"hlpretag":"<span class=\\"s-fc7\\">","hlposttag":"</span>","id":"160947","s":"%s","type":"1","offset":"%s","total":"true","limit":"30","csrf_token":"ee74402ef50d2a957bccb7b540f4bc27"}'
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
        i3x = '{"id":"%s","lv":-1,"tv":-1,"csrf_token":"d5e1f281f7b6f7ff2caf0af810f347d7"}'
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
            'csrf_token': "d5e1f281f7b6f7ff2caf0af810f347d7",
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
        i3x = '{"ids":"[%s]","level":"standard","encodeType":"aac","csrf_token":"d5e1f281f7b6f7ff2caf0af810f347d7"}'
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
        i3x = '{"id":"%d","r":"1080","csrf_token":"ee74402ef50d2a957bccb7b540f4bc27"}'
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
