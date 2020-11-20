import urllib.request


def img_dl_func(url, file_path, file_name):
    full_name = file_path + file_name + '.jpg'

    urllib.request.urlretrieve(url, full_name)


url = input('Type the url you want to download: ')

file_name = input('What would you like to save the image with?: ')

img_dl_func(url, './images/', file_name)
