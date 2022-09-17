import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from redir_downloads import redir_downloads
from redir_downloads import download_path

if __name__=="__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = redir_downloads
    my_observer = Observer()
    my_observer.schedule(my_event_handler, download_path, recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()