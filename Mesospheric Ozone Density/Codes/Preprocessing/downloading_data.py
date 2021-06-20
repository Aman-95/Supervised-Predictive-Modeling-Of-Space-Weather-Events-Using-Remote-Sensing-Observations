import os
from ftplib import FTP
from tqdm import tqdm

#create the file reciever server
ftp = FTP("saber.gats-inc.com")

#login to the server
ftp.login()

#create a data folder structure
home_dir = os.getcwd()

#data directory
home_dir = home_dir + '\\data'

try:
    os.mkdir(home_dir)
except:
    print('directory already exists')
#For the month of november
for i in tqdm(range(305+9, 335)):
    #create a folder for the day
    os.mkdir(home_dir + '\\' + str(i - 304))
    #change working directory
    os.chdir(home_dir + '\\' + str(i - 304))
    ftp.cwd('/Version2_0/Level2A/2004/' + str(i) + '/')
    print('------------------------------------------------------')
    print('/Version2_0/Level2A/2004/' + str(i) + '/')
    for j in tqdm(ftp.nlst()):
        with open(j, "wb") as file:
            ftp.retrbinary(f"RETR {j}", file.write)

    os.chdir(home_dir)


ftp.quit()