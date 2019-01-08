import urllib.request
import


def download_files():
    url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/"
    content = urllib.request.urlopen(url).read()
    print(content)
    for  in content:
    pass

download_files()
