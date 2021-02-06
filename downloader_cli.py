import dl_core.downloader as dl

print("Welcome to use ux.getuploader downloader!")
username = input("Please input the target 'username':")
b = input("Please input the 'begin index number':")
e = input("Please input the 'end index number':")
hasp = input("Password or not? (y/n)")
passwd = None
if hasp == 'y' or hasp == 'Y':
    passwd = input("Please input the 'password':")
if passwd is None:
    dl.dl_submit(username, int(b), int(e))
else:
    dl.dl_submit(username, int(b), int(e), passwd)