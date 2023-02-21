import json, requests, uuid, os


class Fish:
    def __init__(self, name: str, url: str, fish_name: str):
        self.name = name
        self.url = url
        if name == "":
            self.name = str(uuid.uuid1())
        self.type = self.__get_http_type()
        self.fish_name = fish_name

    def __get_http_type(self) -> str:
        # 获取http请求的类型，用与代理进行区分
        find = self.url.find(":", 0, -1)
        return self.url[:find]

    def download(self, proxy: dict = {}):

        if os.path.exists("D:\\fish_download\\{0}".format(self.fish_name)):
            print(True)
        else:
            os.mkdir("D:\\fish_download\\{0}".format(self.fish_name))

        time = 0
        while 1:
            if time >= 3:
                print("{0}下载失败".format(self.url))
                break
            else:
                try:
                    requests.adapters.DEFAULT_RETRIES = 5
                    response = requests.get(self.url, timeout=3, proxies=proxy)
                    with open("D:\\fish_download\\{0}\\{1}.jpg".format(self.fish_name, self.name), "wb") as f:
                        f.write(response.content)
                        break

                except Exception as e:
                    time += 1

                # print("图片'{0}'下载成功".format(self.name))
