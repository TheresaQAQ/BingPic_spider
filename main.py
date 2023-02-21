from utils.UrlUtils import get_fish, parse_url
from core.ProxyPool import ProxyPool
from core.multiple_threading import thread_start

http = ProxyPool("http",
                 ["120.82.174.128:9091", "223.84.240.36:9091", "117.41.38.19:9000", "47.116.131.64:80",
                  "58.246.58.150:9002", "110.238.109.146:2080"])
https = ProxyPool("https",
                  ["111.225.152.53:8089", "118.31.2.38:8999", "183.221.242.102:9443", "36.138.56.214:3128",
                   "61.178.141.146", "123.182.58.115:8089", "123.182.58.170:8089",
                   ])


def run(fish):
    if fish.type == "http":
        fish.download(http.random_ip())

    else:
        fish.download(https.random_ip())


def main():
    fish = get_fish(parse_url("Mugil_cephalus", 1000),"Mugil_cephalus")
    start = 0

    args = []

    for i in range(start, len(fish)):
        args.append(fish[i])

    thread_start(run, args)


if __name__ == "__main__":
    main()
