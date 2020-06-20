import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="This is the titlefor this Basic Notification",#Titile of the Notification
            message="Enter Your Notification Message Here :D",#message for the Notification
            app_icon="D:\Github Projects\icon.ico",		   #Icon path to the File
            timeout=10									   #Time for the notification to be displayed on the Sceen
        )
        time.sleep(60*60)							#time interval after which this program will be invoked again
