'''
PySort
Author - yatinkalra.github.io
github: www.github.com/yatinkalra

'''

import os
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tkinter import filedialog
from tkinter import *
from os import listdir
from os.path import isfile, join

win = Tk()
win.title("PySort")
win.geometry("600x600")
win.configure(bg="White")
current_path=os.getcwd()

Label(win,text="PySort",font=("Times",30),height=4,bg="White",fg="Red")\
    .grid(row=0,column=0,padx=0,pady=0,sticky=N)
Label(win,text="Folder Address",font=("Times",12),width=20,height=1,bg="White",fg="Red")\
    .grid(row=1,column=0,padx=15,pady=10,sticky=W)
label1=Label(win,text=current_path,font=("Times",10),width=65,height=1,bg="Black",fg="White")
label1.grid(row=2,column=0,padx=0,pady=10)

def openDir():
    global current_path
    current_path=filedialog.askdirectory()
    label1.config(text=current_path)

Button(win,text='Browse',font=("Times",10),command=openDir,width=8,height=1,bg="Black",fg="White")\
    .grid(row=2,column=2,padx=0,pady=10,sticky=E)

extension = ''

executable = ['.apk', '.bat', '.bin', '.exe', '.jar', '.py']
images = ['.ico', '.png', '.jpeg', '.gif', '.tiff', '.psd', '.raw', '.jpg']
Entertainment = ['.mp3','.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.mpeg', '.mpg', '.3gp']
document = ['.doc', '.pdf', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt']
compressed = ['.7z', '.zip', '.rar', '.z', '.zip', '.iso']
database = ['.csv', '.dat', '.db', '.dbf', '.sql', 'xml']
program = ['.c', '.class', '.cpp', '.cs', '.h', '.java', '.swift', '.vb', '.sh']
system = ['.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.ini', '.msi', '.sys', '.tmp', '.ini']

def staticOne():
    track = open(current_path + "/listFiles.txt", "w+")
    reader = track.readlines(1)

    if not reader:
        track.write("Sorted files are placed under the following folder:\n\n")
        track.write("\tImage Files:\n\n")
        track.write("\tEntertainment Files:\n\n")
        track.write("\tDocument Files:\n\n")
        track.write("\tCompressed Files:\n\n")
        track.write("\tDatabase Files:\n\n")
        track.write("\tExecutable Files:\n\n")
        track.write("\tProgramming Files:\n\n")
        track.write("\tSystem Files:\n\n")
        track.write("\tOther Files:\n\n")
    track.close()
    print(current_path)
    file = [f for f in listdir(current_path) if isfile(join(current_path, f))]
    print(file)
    for f in file:
        currentDT = datetime.datetime.now()
        i=0
        name, ext = os.path.splitext(f)

        track = open(current_path + "/listFiles.txt", 'r')
        contents = track.readlines()
        track.close()

        if ext in images:
            for x in contents:
                i+=1
                if x =='\tImage Files:\n':
                    contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
                extension = '/Image Files'

        elif ext in Entertainment:
            for x in contents:
                i+=1
                if x=='\tEntertainment Files:\n':
                    contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
                extension = '/Entertainment Files'

        elif ext in document:
            if name=='listFiles':
                pass
            else:
                for x in contents:
                    i+=1
                    if x=='\tDocument Files:\n':
                        contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
                extension = '/Document Files'

        elif ext in compressed:
            for x in contents:
                i+=1
                if x == '\tCompressed Files:\n':
                    contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
            extension = '/Compressed Files'

        elif ext in database:
            for x in contents:
                i+=1
                if x=='\tDatabase Files:\n':
                    contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
            extension = '/Database Files'

        elif ext in executable:
            if name=='winFileSorter':
                pass
            else:
                for x in contents:
                    i+=1
                    if x == '\tExecutable Files:\n':
                        contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
                extension = '/Executable Files'

        elif ext in program:
            for x in contents:
                i+=1
                if x=='\tProgramming Files:\n':
                   contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
            extension = '/Programming Files'

        elif ext in system:
            for x in contents:
                i+=1
                if x=='\tSystem Files:\n':
                    contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
            extension = '/System Files'

        else:
            for x in contents:
                i+=1
                if x=='\tOther Files:\n':
                    contents.insert(i,'\t\t'+f+'\t\t'+"Sorted on - "+str(currentDT.strftime("%Y-%m-%d %H:%M:%S"))+'\n')
            extension = '/Other Files'

        if i>0:
            track = open(current_path + "/listFiles.txt", "r+")
            track.seek(0)
            contents = "".join(contents)
            track.write(contents)
            track.truncate()

            if not os.path.exists(current_path + extension):
                os.mkdir(current_path + extension)

            os.rename(current_path+'\\'+f, current_path+extension+'\\'+f)

def dynamicOne():
    class Myhandler(FileSystemEventHandler):
        def on_modified(self, event):
            staticOne()

    event = Myhandler()
    observe = Observer()
    observe.schedule(event, current_path, recursive=True)
    observe.start()

Label(win,text="Type of Sort",font=("Times",12),width=20,height=1,bg="Black",fg="Red")\
    .grid(row=3,column=0,padx=0,pady=10,sticky=W)
Button(win,text='Sort current files only',font=("Times",11),command=staticOne,width=35,height=2,bg="Black",fg="White")\
    .grid(row=4,column=0,padx=0,pady=10)
Button(win,text="All Files",font=("Times",11),command=dynamicOne,width=35,height=2,bg="Black",fg="White")\
    .grid(row=5,column=0,padx=0,pady=10)
Label(win,text="NOTE - ALL FILES requires program to keep running always.",font=("Times",12),fg="Red",bg="White")\
    .grid(row=6,column=0,padx=5,pady=3,sticky=N)
Button(win,text="Exit",font=("Times",10),command=sys.exit,width=10,bg="Black",fg="White")\
    .grid(row=7,column=0,padx=3,pady=3)

win.mainloop()
