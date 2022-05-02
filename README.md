Project Description:
- Bruteforce programs for Login Pages or Directories coded in Python.
- To be run on Kali Linux VM only.

Installation:
1. Download Project:
	- git clone https://github.com/jaredpek/Bruteforce-Programs
2. Install Requirements:
    - pip install -r requirements.txt

For Login Bruteforcer:
1. Setup:
	- Create a file containing possible usernames and take note of the path to this file
	- Create another file containing possible passwords and take note of the path to this file
	- Obtain URL of the page you want to attack
	- Attempt a login with random credentials to obtain the message received when login fails
	- View page source to obtain values of the username field, the password field and the login button
	- Obtain form method
		- If method = 'GET': Obtain Cookie value using Burpsuite
		- If method = 'POST': Go to Step 2
2. Attacking the website:
	- Inside the terminal, run the command: python3 LoginBruteforcer.py
	- Fill in the prompts accordingly

For Directory Bruteforcer:
1. Setup:
	- Obtain URL of the page you want to attack
    - Obtain the path to a file containing possible directories
    - Either create your own file<br>
    - Or use the one provided in Kali Linux VM: /usr/share/dirb/wordlists/common.txt
2. Attacking the website:
    - Inside the terminal, run the command: python3 DirectoryBruteforcer.py
    - Fill in the prompts accordingly
