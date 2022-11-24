import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Downloads/document"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print({event.src_path},"Hey,this file has been created!")

    def on_deleted(self,event):
        print({event.src_path},"Oops!this file has been deleted")

#initalising event handler class
event_handler = FileMovementHandler()

#initialising observer
observer = Observer()

#Schedule the observer
observer.schedule(event_handler,from_dir,recursive=True)

#start the observer
observer.start()
            
while True :
    time.sleep(2)
    print("running....")




