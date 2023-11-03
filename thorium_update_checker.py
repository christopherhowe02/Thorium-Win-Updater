from requests import get
from win32com.client import *
from tkinter import messagebox
from os import getenv
from subprocess import Popen

response=get("https://api.github.com/repos/Alex313031/Thorium-Win/releases/latest")

installed_version=Dispatch("Scripting.FileSystemObject").GetFileVersion(getenv("LOCALAPPDATA")+"/Thorium/Application/thorium.exe")

newest_version=response.json()["tag_name"][1:]

#print(installed_version)
#print(newest_version)

def update():
    if messagebox.askyesno("Thorium Update", "Thorium "+newest_version+" is available\nDo you want to update?")==True:
        for asset in response.json()["assets"]:
            if ".exe" in asset["browser_download_url"]:
                #print("download:", asset["browser_download_url"])
                file=get(asset["browser_download_url"], allow_redirects=True)
                with open(getenv("LOCALAPPDATA")+"/temp/thorium_update.exe", "wb") as f: f.write(file.content)
                Popen([getenv("LOCALAPPDATA")+"/temp/thorium_update.exe"])
                break

if installed_version.split(".")[0]<newest_version.split(".")[0]: update()
elif installed_version.split(".")[1]<newest_version.split(".")[1]: update()
elif installed_version.split(".")[2]<newest_version.split(".")[2]: update()
elif installed_version.split(".")[3]<newest_version.split(".")[3]: update()



