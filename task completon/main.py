# making a simple list for  task -- which we complete in full day.
#it just a reminder and not really work as check box....



import time
from plyer import notification 


while True:
    print("The task list of MONU VERMA [every day]")# for just testing
    task = ("workout\ndiet\nstudies\nreading\coding\nprojects on  coding\njournaling")
    notification.notify(title = "task list remainder",
                         message = task)
    # for  notifications..
    
    time.sleep(24*60*60)# i am writing this for it will remind me in one day....