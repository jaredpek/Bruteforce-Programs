import requests
from termcolor import colored

target_url = input('[*] Enter Target URL: ')
print('[*] File With Common Directories: /usr/share/dirb/wordlists/common.txt')
directory_file = input('[*] Enter File Containing Directories (Optional To Copy Path To Common Directories): ')
print(colored('\n[*] Initiating Bruteforce Attack...\n', 'yellow'))
if target_url[-1] != '/':
    target_url = target_url + '/'
else:
    pass


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


discdir = []
directories = open(directory_file, 'r')
for directory in directories:
    full_url = target_url + directory.strip()
    response = request(full_url)
    if response:
        discdir.append(full_url)
        print(colored(f'[+] Discovered Directory At This Path: {full_url}', 'green'))
    else:
        print(colored(f'[-] No Directory Discovered At This Path: {full_url}', 'red'))
directories.close()

print(colored('\n[*] Bruteforce Attack Completed\n', 'yellow'))
if not discdir:
    print(colored('[*] No Directories Discovered.', 'red'))
else:
    print(colored('[*] Directories Discovered:', 'green'))
    for directory in discdir:
        print(colored(f'[*] Directory Path: {directory}', 'green'))
