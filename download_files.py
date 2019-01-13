import lxml.html
import zipfile
import requests
from io import BytesIO


def create_directories_links_list(url, dom):
    directories_links_list = []
    for link in dom.xpath('//tr[td/img[@alt="[DIR]"]]/td//a/@href'):
        directories_links_list.append(url + link)
    return directories_links_list


def create_files_links_list(directories_links_list):
    files_links_list = {}
    for link in directories_links_list:
        request = requests.get(link)
        dom = lxml.html.fromstring(request.content)
        for file_link in dom.xpath('//tr[td/img[@alt="[   ]"]]/td//a/@href'):
            files_links_list[file_link] = link + file_link
    return files_links_list


def download_zip_files(files_links_list):
    request = None
    for file_name in files_links_list:
        status_code = 404
        while status_code != 200:
            request = requests.get(files_links_list[file_name])
            status_code = request.status_code
        zip_file = zipfile.ZipFile(BytesIO(request.content))
        zip_file.extractall('data/' + file_name)


def download_files():
    url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/"
    request = requests.get(url)
    dom = lxml.html.fromstring(request.content)

    directories_links_list = create_directories_links_list(url, dom)
    files_links_list = create_files_links_list(directories_links_list)
    download_zip_files(files_links_list)


download_files()
