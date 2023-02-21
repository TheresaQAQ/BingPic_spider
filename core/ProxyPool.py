import random, requests, json

ipQuery = "https://httpbin.org/ip"


def get_ip(proxy: dict) -> str:
    value = ''
    for v in proxy.values():
        value = v
        find = str(v).find(":", 0, -1)

    return value[:find]


def is_ok(proxy: dict) -> bool:
    try:
        response = requests.get(ipQuery, proxies=proxy)
        if json.loads(response.text)["origin"] == get_ip(proxy):
            print("代理正常，ip为" + get_ip(proxy))
            return True
        else:
            return False
    except requests.exceptions.ProxyError:
        print("代理错误，ip为" + get_ip(proxy))
        return False


class ProxyPool:
    def __init__(self, http_type: str, ips: list):
        self.name = http_type
        self.http_type = http_type

        self.ips_str = ips

    def random_ip(self) -> dict:
        while 1:
            ip = random.choice(self.ips_str)
            proxy = {
                self.http_type: ip
            }
            if is_ok(proxy):
                return proxy


if __name__ == "__main__":
    iplist = ["1.1.1.1:22", '43555:22', "464758:44"]
    https_proxy = ProxyPool("https", iplist)
    print(get_ip(https_proxy.random_ip()))
