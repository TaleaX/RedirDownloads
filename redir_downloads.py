import os
import re


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

def redir_downloads(event):
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
    redir_downloads("some file")