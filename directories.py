import requests

target_url = input('[*] Enter Target URL: ')
file_name = input('[*] Enter Name of The File Containing Directories: ')


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exeptions.ConnectionError:
        pass

file = open(file_name, 'r')
for line in file:
    directory = line.strip()
    full_url = target_url + '/' + directory
    response = requests(full_url)
    if response:
        print('[*] Discovered Directory At This Path: ' + full_url)