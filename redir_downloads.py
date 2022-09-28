import os
import re

BASE_DIR = "C:/Users/talea" # easier for other users to switch out

pattern_picture = re.compile(".*[.]jpg|.*[.]jpeg|.*[.]png|.*[.]gif")
pattern_docx = re.compile(".*[.]docx|.*[.]doc")
pattern_pdf = re.compile(".*[.]pdf")
pattern_exec = re.compile(".*[.]exe")
download_path = f"{BASE_DIR}/Downloads/"
pic_path = f"{BASE_DIR}/Pictures/"
docs_path = f"{BASE_DIR}/Documents/"
pdf_path = f"{BASE_DIR}/Pdfs/"
exec_path = f"{BASE_DIR}/Executables/"

def exec_move(name, path):
    cmd = f'move {download_path}"{name}" {path}'
    cmd = cmd.replace("/", "\\")
    print(cmd)
    os.system(cmd)

def redir_downloads(event):
    with os.scandir(download_path) as entries:
        for entry in entries:
            if re.match(pattern_picture, entry.name):
                exec_move(entry.name, pic_path)
            elif re.match(pattern_docx, entry.name):
                exec_move(entry.name, docs_path)
            elif re.match(pattern_pdf, entry.name):
                exec_move(entry.name, pdf_path)
            elif re.match(pattern_exec, entry.name):
                exec_move(entry.name, exec_path)


if __name__== "__main__":
    redir_downloads("some file")