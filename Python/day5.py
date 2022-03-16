#STORAGE DROPBOX#

#open dropbox using "https://www.dropbox.com/h"
# Login to dropbox
#pip install dropbox
#howdoi upload files using dropbox

import dropbox

class transferdata:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)

def main():
    #access_token is common for each dropbox
    access_token="sl.BCzS9LhYuSamk2zJW6DMMS3VSxkFwDSi40sZdd-NhJf8eFIqqxOtUNBvN1nS-wdOMD4Nk_fWvVhDw7fJd3YYGBjtdMPH3tAds-4OX2WxPsealEEwP-e9090zMxtKMAzPlA6DIfrVuz-H"
    transfer=transferdata(access_token)

    fromfile =input("enter the source : ")
    tofile =input("enter the destination : ")

    transfer.upload(fromfile,tofile)
    print("uploaded")

main()