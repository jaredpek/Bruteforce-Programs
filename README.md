# BruteforcePrograms
Bruteforce programs for Login Pages or Directories coded in Python and to be run on Kali Linux VM only.

Download the program:
1. Inside terminal, run the command: git clone https://github.com/jaredpek/Bruteforce-Programs<br>

For Login Bruteforcer:
1. Setup:
  - Create a file containing possible usernames and take note of the path to this file<br>
  - Create another file containing possible passwords and take note of the path to this file<br>
  - Obtain URL of the page you want to attack<br>
  - Attempt a login with random credentials to obtain the message received when login fails<br>
  - View page source to obtain values of the username field, the password field and the login button<br>
  - Obtain form method<br>
    - If method = 'GET': Obtain Cookie value using Burpsuite<br>
    - If method = 'POST': Go to Step 2<br>
2. Attacking the website:<br>
  - Inside the terminal, run the command: python3 LoginBruteforcer.py<br>
  - Fill in the prompts accordingly<br>

For Directory Bruteforcer:
1. Setup:
  - Obtain URL of the page you want to attack<br>
  - Obtain the path to a file containing possible directories<br>
    - Either create your own file<br>
    - Or use the one provided in Kali Linux VM: /usr/share/dirb/wordlists/common.txt<br>
2. Attacking the website:<br>
  - Inside the terminal, run the command: python3 DirectoryBruteforcer.py<br>
  - Fill in the prompts accordingly<br>
