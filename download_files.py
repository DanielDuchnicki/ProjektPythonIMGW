import lxml.html
import zipfile
import requests
from io import BytesIO


def create_directories_links_list(url, dom):
    """ Funkcja zwracajaca liste wszystkich folderow na stronie IMGW z danymi
        :param dom: DOM object of the IMGW data page
        :param url: URL of the IMG data page
        :return directories_links_list: list of directories' links
    """
    directories_links_list = []
    for link in dom.xpath('//tr[td/img[@alt="[DIR]"]]/td//a/@href'):
        directories_links_list.append(url + link)
    return directories_links_list


def create_files_links_dictionary(directories_links_list):
    """ Funkcja zwracajaca slownik linkow do wszystkich plikow z danymi znajdujacych sie na stronie IMGW
        :param directories_links_list: list of directories' links
        :return files_links_dictionary: dictionary of all files links
    """
    files_links_dictionary = {}
    for link in directories_links_list:
        request = requests.get(link)
        dom = lxml.html.fromstring(request.content)
        for file_link in dom.xpath('//tr[td/img[@alt="[   ]"]]/td//a/@href'):
            files_links_dictionary[file_link] = link + file_link
    return files_links_dictionary


def select_files_by_station_id(files_links_dictionary, station_id):
    """ Funkcja zwracajaca slownik linkow do plikow z danymi dla wybranej stacji pogodowej
        :param files_links_dictionary: dictionary of all files links
        :param station_id: the station's id
        :return selected_files_links_dictionary: dictionary of selected files' links
    """
    selected_files_links_dictionary = {}
    dictionary_keys = files_links_dictionary.keys()
    for key in dictionary_keys:
        if str(station_id) == key[-9:-6]:
            selected_files_links_dictionary[key] = files_links_dictionary[key]
    return selected_files_links_dictionary


def download_zip_files(selected_files_links_dictionary):
    """ Funkcja sciagajaca pliki z linkow ze slownika z linkami
        :param selected_files_links_dictionary: dictionary of selected files' links
    """
    request = None
    for file_name in selected_files_links_dictionary:
        status_code = 404
        while status_code != 200:
            request = requests.get(selected_files_links_dictionary[file_name])
            status_code = request.status_code
        zip_file = zipfile.ZipFile(BytesIO(request.content))
        zip_file.extractall('data/')


def download_files(station_id):
    """ Funkcja sciagajaca pliki ze strony IMGW z danymi dla danej stacji pogodowej
        :param station_id: the station's id
    """
    url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/"
    request = requests.get(url)
    dom = lxml.html.fromstring(request.content)

    directories_links_list = create_directories_links_list(url, dom)
    files_links_dictionary = create_files_links_dictionary(directories_links_list)
    selected_files_links_dictionary = select_files_by_station_id(files_links_dictionary, station_id)
    download_zip_files(selected_files_links_dictionary)
