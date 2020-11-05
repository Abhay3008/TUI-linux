import os,getpass
import subprocess
os.system("tput setaf 1")
print("\t\t\t Hi welcome to my TUI for some small tasks")
os.system("tput setaf 7")

print("\t\t\t-----------------------------------------")
passwd = getpass.getpass("Enter ur password: ")
apass = "abhay"
if passwd != apass:
    print("authorization incorrect")
    exit()
    
print("which machine you want to use local/remote: ",end="")
location = input()
print(location)
if location == "remote":
    remoteIp = input("Enter ur Ip: ")
while True:
    os.system("tput setaf 4")
    print("\t\t .--,\t    .--,\n\t\t( (  \.---./  ) )\n\t\t '.__/o   o\__.'\n\t\t    {=  ^  =}\n\t\t     >  -  <\n      ___________.\"\"`-------`\"\".____________\n     /                                      \ \n     \ o   Press 1: to see date           o / \n     /     Press 2: to check Calendar       \ \n     \     Press 3: to conf Webserver       /   \n     /     Press 4: to create user          \ \n     \     Press 5: to install a package    / \n     /     Press 6: to check about server?  \ \n     \     Press 7: to exit \t\t    / \n     /______________________________________\ \n\t\t   ___)( )(___ \n \t\t  (((__) (__)))")
    os.system("tput setaf 2")
    print("Enter your choice: " , end="")
    ch=input()
    print(ch)
    os.system("tput setaf 7")

    if location == "local":
        if int(ch) == 1:
            os.system("date")
        elif int(ch) == 2:
            os.system("cal")
        elif int(ch) == 3:
            os.system("sudo yum install httpd")
        elif int(ch) == 4:
            print("Please provide name of the user: ",end="")
            create_user = input()
            os.system("sudo useradd {0}".format(create_user))   ##this is called place holder  or interpolation
        elif int(ch) == 5:
             print("write a package name lets see if its available: ", end="")
             pack_name = input()
             os.system("sudo dnf install {0}".format(pack_name))
        elif int(ch) == 6:
             os.system("systemctl restart httpd")
        elif int(ch) == 7:
             exit()

            
        else:
            print("option not found")
        os.system(input("Press Enter to continue........"))
        os.system("clear")
    elif location == "remote":
        if int(ch) == 1:
            os.system("ssh {0} date".format(remoteIp))
        elif int(ch) == 2:
            os.system("ssh {0} cal".format(remoteIp))
        elif int(ch) == 3:
            os.system("ssh {0} sudo yum install httpd".format(remoteIp))
        elif int(ch) == 4:
            print("can you give me name for user: ",end="")
            create_user = input()
            os.system("ssh {0} sudo useradd {1}".format(remoteIp,create_user))   ##this is called place holder  or interpolation
        elif int(ch) == 5:
            os.system("write a package name lets see if its available: ", end="")
            pack_name = input()
            os.system("ssh {0} sudo dnf install {1}".format(remoteIp,pack_name))
        elif int(ch) == 6:
            os.system("ssh {0}systemctl restart httpd".format(remoteIp))
        elif int(ch) == 7:
            exit()
        else:
            print("option not found")
            
    else:
        print("sorry wrong input")
        
