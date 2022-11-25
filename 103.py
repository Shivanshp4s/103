import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/DELL/Downloads"
to_dir = "C:/Users/DELL/Downloads/document"

list_of_files = os.listdir(from_dir)


class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print({event.src_path},"Hey,this file has been created!")

    def on_deleted(self,event):
        print({event.src_path},"Oops!this file has been deleted")


event_handler = FileMovementHandler()


observer = Observer()


observer.schedule(event_handler,from_dir,recursive=True)


observer.start()
            
try:   
    while True :
        time.sleep(2)
        print("running....")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()




