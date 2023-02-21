import json, requests, uuid


class Fish:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        if name == "":
            self.name = str(uuid.uuid1())

    def download(self):
        print("正在下载：{0}".format(self.url))
        try:
            response = requests.get(self.url, timeout=3)
            with open("pic\\" + self.name + ".jpg", "wb") as f:
                f.write(response.content)

            print("图片'{0}'下载成功".format(self.name))

        except requests.exceptions.SSLError:
            print("下载失败,网站资源已丢失")
        except requests.exceptions.ConnectTimeout:
            print("下载失败,网络连接超时")
        except requests.exceptions.ReadTimeout:
            print("下载失败,网络连接超时")

        except Exception:
            print("下载失败,未知错误")
