pip install watchdog

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# object that will be notified when something happen on the filesystem you are monitoring.
if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

# Handling all events
def on_created(event):
    print(f"hey, {event.src_path} has been created!")
def on_deleted(event):
    print(f"oh no, Someone deleted {event.src_path}!")
def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")
def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

# here is the observer
path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

# start the observer
my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
