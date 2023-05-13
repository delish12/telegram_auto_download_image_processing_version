# telegram_auto_download_image_processing_version

#### this is the upgraded version of my project telegram_anime_downloader_automate
in that project i used static movements and static clicking which can have some issues 
with downloading

to overcome this i thought of using image processing using python

## intension of the project:-
to download any long series in telegram without aid of a user

## LIBS used:-
pyautogui,numpy,time,cv2

## working:-
keep all the files i.e., images like cancel,download,open and main.py in the same folder

run the main file and input the no.of episodes to download as asked and open telegram app 
and open the channel which provides download for the perticular anime or your choice of entertainment

and watch the download automatically happening


## 2 modes:-

### wfd in line 10 if True:-

wfd stands for wait for download this mode is used when low internet speed 
which basically download each episode only after completion of the previous one

### wfd in line 10 if False:-

this can be used if internet speed is high enough that all the episodes can be
downloaded parallely then the program will download all the episodes at the same time

#### enjoy your free time