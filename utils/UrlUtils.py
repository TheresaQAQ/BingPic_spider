import requests
import json

from core.Fish import Fish

cookies_raw = "_EDGE_V=1; MUID=2679AAA4B5B363CA1167B895B4F06295; MUIDB=2679AAA4B5B363CA1167B895B4F06295; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=F178597CDE6846BCAF036D718089C7BF&dmnchg=1; USRLOC=HS=1&CLOC=LAT=23.0218|LON=113.1219|A=18791|TS=230203123216|SRC=I; _UR=QS=0&TQS=0; MMCASM=ID=AA7BD591919D4ECF8AB1615D779FEF61; _EDGE_E=O=fw-efly3; _ITAB=STAB=TR; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; PPLState=1; ANON=A=2D5AC8F73D59D89C1FAD6567FFFFFFFF&E=1bd5&W=1; NAP=V=1.9&E=1b7b&C=5Y6uE6NSk6e1ZJZRFJhRYzW1iQVW7yMl7sNwle6qvakb_aqMl1T9hw&W=1; ANIMIA=FRE=1; WLS=C=45c93e5630e1980d&N=%e5%90%af%e4%bf%8a; SRCHS=PC=CNNDDB; _SS=SID=38E42BB4C47D6ED200113919C5AF6FEE&PC=CNNDDB&R=200&RB=0&GB=0&RG=200&RP=200; SUID=A; SRCHUSR=DOB=20230115&T=1675500287000; ZHCHATSTRONGATTRACT=TRUE; ipv6=hit=1675503891018&t=4; ZHCHATWEAKATTRACT=TRUE; _HPVN=CS=eyJQbiI6eyJDbiI6MTEsIlN0IjoyLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjExLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMSwiU3QiOjEsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMi0wNFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6ODd9; MicrosoftApplicationsTelemetryDeviceId=93f48d9a-bda7-4566-83c1-11fecdd02415; fbar=imgfbar=1; _EDGE_S=SID=38E42BB4C47D6ED200113919C5AF6FEE&ui=zh-cn; SNRHOP=I=&TS=; _U=1yWOohZdhsg_xW5IIMLy6PB_NUpd_13L_GEpRFA_yj0TbfnGRgwU65Xs9bWd2li2NrWOQwfNcrBI9ibwg2ZuhLiMgdvf3TBinYwtcRFR-xHGDW12ZrDxScLi5zcOirBbOCzBo78zttIDtrUGuWLwaZc4mb2HxYvVLimmIBbhdDjnYxRhqNN9z_kmGxEsP8BpQ9_v8sGhwC-2-bApseexd_A; ABDEF=V=13&ABDV=13&MRNB=1675503479126&MRB=0; _RwBf=ilt=158&ihpd=1&ispd=8&rc=200&rb=0&gb=0&rg=200&pc=200&mtu=0&rbb=0&g=0&cid=&clo=0&v=22&l=2023-02-04T08:00:00.0000000Z&lft=2023-01-17T00:00:00.0000000-08:00&aof=0&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2023-02-04T09:37:59.4050727+00:00&rwred=0&wls=&lka=0&lkt=0&TH=; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&BZA=0&BRW=M&BRH=M&CW=1321&CH=769&SCW=1304&SCH=3008&DPR=2.0&UTC=480&DM=0&EXLTT=32&HV=1675503480&PRVCW=1321&PRVCH=769&PR=2"

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70"
}


def extract_cookies(cookie):
    """从浏览器或者request headers中拿到cookie字符串，提取为字典格式的cookies"""
    cookies = dict([l.split("=", 1) for l in cookie.split("; ")])
    return cookies


def parse_url(key: str, count: int):
    split = key.split("_")
    key = ""
    for i in split:
        key = key + "+" + i
    key = key[1:]
    url = "https://cn.bing.com/images/api/custom/search?q={key}" \
          "&preserveIdOrder=2&count={count}&offset=0&" \
          "skey=XZsqCJEFoUIxADe3sw037WwG8t-3df5e40mjBGZYBBM&" \
          "safeSearch=Strict&mkt=zh-cn&setLang=zh-cn&" \
          "IG=A8932C399D66471F8788473B5657E052&IID=idpfs&SFX=1".format(key=key, count=count)
    print(url)
    return url


def get_fish(url: str):
    # url = "https://cn.bing.com/images/api/custom/search?q=Zebrias+zebra&id=7D3D35EF1F956FD4B666BDEBF3B32FD2A1989964&preserveIdOrder=1&count=25&offset=0&skey=XZsqCJEFoUIxADe3sw037WwG8t-3df5e40mjBGZYBBM&safeSearch=Strict&mkt=zh-cn&setLang=zh-cn&IG=A8932C399D66471F8788473B5657E052&IID=idpfs&SFX=1"

    cookies = extract_cookies(cookies_raw)
    html = requests.get(url, cookies=cookies, headers=header)

    jsons = json.loads(html.text)
    values = jsons["value"]

    fish_list = []
    for i in values:
        url = ""
        name = ""
        try:
            url = i["cDNContentUrl"]
            name = i["name"]

        except KeyError:
            url = i["contentUrl"]

        finally:
            fish_list.append(Fish(name, url))

    return fish_list


if __name__ == "__main__":
    parse_url("Zebrias zebra", 100)
