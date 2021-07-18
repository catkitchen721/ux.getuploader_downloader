from dl_core.downloader import dl_submit

print("Welcome to use ux.getuploader downloader!")
username = input("Please input the target 'username':")
r = input("Please input whether 'ranking' mode or not: (y/n)")
if r == 'y' or r == 'Y':
    r = True
else:
    r = False
if r:
    rb = input("Ranking by (week, day, or month)? (w/d/m)")
    b = input("Please input the 'begin ranking number':")
    e = input("Please input the 'end ranking number':")
else:
    rb = 'w'
    b = input("Please input the 'begin index number':")
    e = input("Please input the 'end index number':")
if rb == 'w' or rb == 'W':
    rb = 'weekly'
elif rb == 'd' or rb == 'D':
    rb = 'daily'
elif rb == 'm' or rb == 'M':
    rb = 'monthly'
else:
    rb = 'weekly'
hasp = input("Password or not? (y/n)")
passwd = None
if hasp == 'y' or hasp == 'Y':
    passwd = input("Please input the 'password':")
if passwd is None:
    dl_submit(username, int(b), int(e), isCLI=True, ranking=r, ranking_by=rb)
else:
    dl_submit(username, int(b), int(e), passwd, isCLI=True, ranking=r, ranking_by=rb)