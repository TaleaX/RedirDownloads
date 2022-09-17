import os
import re
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

pattern_picture = re.compile(".*[.]jpg|.*[.]jpeg|.*[.]png|.*[.]gif")
pattern_docx = re.compile(".*[.]docx|.*[.]doc")
pattern_pdf = re.compile(".*[.]pdf")
pattern_exec = re.compile(".*[.]exe")
download_path = "C:/Users/talea/Downloads/"
pic_path = "C:/Users/talea/Pictures/"
docs_path = "C:/Users/talea/Documents/"
pdf_path = "C:/Users/talea/Pdfs/"
exec_path = "C:/Users/talea/Executables/"

def exec_move(name, path):
    cmd = "move " + download_path + '"' + name + '"' + " " + path
    cmd = cmd.replace("/", "\\")
    print(cmd)
    os.system(cmd)

def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    with os.scandir(download_path) as entries:
        for entry in entries:
            if re.match(pattern_picture, entry.name):
                exec_move(entry.name, pic_path)
            if re.match(pattern_docx, entry.name):
                exec_move(entry.name, docs_path)
            if re.match(pattern_pdf, entry.name):
                exec_move(entry.name, pdf_path)
            if re.match(pattern_exec, entry.name):
                exec_move(entry.name, exec_path)


if __name__=="__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    my_event_handler.on_created = on_created
    my_observer = Observer()
    my_observer.schedule(my_event_handler, download_path, recursive=True)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()