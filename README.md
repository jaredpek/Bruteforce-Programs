# BruteforcePrograms
Bruteforce programs for Login Pages or Directories coded in Python and to be run on Kali Linux VM only.

Download the program:
git clone https://github.com/jaredpek/Bruteforce-Programs

For Login Bruteforcer:
1. Setup:
  a. Create a file containing possible usernames and take note of the path to this file
  b. Create another file containing possible passwords and take note of the path to this file
  c. Obtain URL of the page you want to attack
  d. Attempt a login with random credentials to obtain the message received when login fails
  e. View page source to obtain values of the username field, the password field and the login button
  f. Obtain form method
    i.  If method = 'GET': Obtain Cookie value using Burpsuite
    ii. If method = 'POST': Go to Step 2
2. Attacking the website:
  a. Inside the terminal, run the command: python3 LoginBruteforcer.py
  b. Fill in the prompts accordingly

For Directory Bruteforcer:
1. Setup:
  a. Obtain URL of the page you want to attack
  b. Obtain the path to a file containing possible directories
    i.  Either create your own file
    ii. Or use the one provided in Kali Linux VM: /usr/share/dirb/wordlists/common.txt
2. Attacking the website:
  a. Inside the terminal, run the command: python3 DirectoryBruteforcer.py
  b. Fill in the prompts accordingly
