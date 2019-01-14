import lxml.html
import zipfile
import requests
from io import BytesIO


def create_directories_links_list(url, dom):
    directories_links_list = []
    for link in dom.xpath('//tr[td/img[@alt="[DIR]"]]/td//a/@href'):
        directories_links_list.append(url + link)
    return directories_links_list


def create_files_links_dictionary(directories_links_list):
    files_links_dictionary = {}
    for link in directories_links_list:
        request = requests.get(link)
        dom = lxml.html.fromstring(request.content)
        for file_link in dom.xpath('//tr[td/img[@alt="[   ]"]]/td//a/@href'):
            files_links_dictionary[file_link] = link + file_link
    return files_links_dictionary


def select_files_by_station_id(files_links_dictionary, station_id):
    selected_files_links_dictionary = {}
    dictionary_keys = files_links_dictionary.keys()
    for key in dictionary_keys:
        if str(station_id) == key[-9:-6]:
            selected_files_links_dictionary[key] = files_links_dictionary[key]
    return selected_files_links_dictionary


def download_zip_files(selected_files_links_dictionary):
    request = None
    for file_name in selected_files_links_dictionary:
        status_code = 404
        while status_code != 200:
            request = requests.get(selected_files_links_dictionary[file_name])
            status_code = request.status_code
        zip_file = zipfile.ZipFile(BytesIO(request.content))
        zip_file.extractall('data/')


def download_files(station_id):
    url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/"
    request = requests.get(url)
    dom = lxml.html.fromstring(request.content)

    directories_links_list = create_directories_links_list(url, dom)
    files_links_dictionary = create_files_links_dictionary(directories_links_list)
    selected_files_links_dictionary = select_files_by_station_id(files_links_dictionary, station_id)
    download_zip_files(selected_files_links_dictionary)
