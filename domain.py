# domain name
import pyfiglet 
import socket
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan

banner=pyfiglet.figlet_format("Domain Ip")
print(bgreen+banner)
print(bred+" "*30,"๐๐ฟ๐ฒ๐ฎ๐๐ฒ๐ฑ ๐ฏ๐ ๐ฅ๐ผ๐ผ๐>๐๐ผ๐ฑ๐ฒ โ\n\n")
print(bblue+"Tools User_Name [root] Password [code]\n ")
while True:
	user="root"
	pwd="code"
	user_name=(input(byellow+"[>] Enter The user name:"))
	password=(input(bpurple+"\n[>] Enter The password:"))
	if user==user_name and pwd==password:
		print(bgreen+"\nLogin Successfulโ")
		break
	else:
		print(bred+"\nLogin Failed?")
domain_name=(input(bcyan+"\nEnter Your Target Domain Url:"))
ip_address=socket.gethostbyname(domain_name)
print(bred+"\nThis is Your Host Ip [>] ",bgreen+ip_address)
a=input()