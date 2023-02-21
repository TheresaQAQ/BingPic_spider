from utils.UrlUtils import get_fish, parse_url


def main():
    fish = get_fish(parse_url("Thryssa_dussumieri", 1000))
    start = 0

    for i in range(start, len(fish)):
        fish[i].download()


if __name__ == "__main__":
    main()
