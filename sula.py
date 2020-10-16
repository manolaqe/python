from pytube import YouTube
from subprocess import call
import shutil, os, sys
   
def swla():
    os.startfile('C:\\SLAM_v1.5.4\\SLAM.exe')
    url = input("Link youtube: ")
    nume = input("Nume (nume efectiv + .wav): ")
    ytd = YouTube(url)
    stream = ytd.streams.first()
    stream.download()
    cale = "C:\\SLAM_v1.5.4\\csgo\\" + nume
    newPath = shutil.copy('YouTube.mp4', cale)
    os.system("taskkill /f /im SLAM.exe")

i = 1
while i < 100:
    swla()
    i += 1