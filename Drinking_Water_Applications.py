import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title= "**Time to drink Water!!!",
            message = "Water requirement and factors affecting it. ... However, it is generally accepted that a normal healthy person needs to drink about 8 glasses (2 litre) of water per day.",
            app_icon = "C:\\Users\\user\\Desktop\\Application\\icon.ico",
            timeout=10
        )
        time.sleep(60*60)
    