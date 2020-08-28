from tkinter import *
from tkinter import filedialog
from tkinter import filedialog
from tkinter import Menu
from tkinter.scrolledtext import *
from tkinter.filedialog import asksaveasfile 
from tkinter.filedialog import askopenfile 
from tkinter import messagebox
import os
from tkinter.colorchooser import askcolor
from tkinter.font import Font,families

root = Tk()
root.geometry("500x400")
filename = None
def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)
	
def saveFile():
	global filename
	t = text.get(0.0, END)
	f.open(filename, "w")
	f.write(t)
	f.close()
	
def saveAs():
	f = asksaveasfile(mode="w", defaultextension=".txt")
	t = text.get(0.0, END)
	try:
		f.write(t.rstrip())
	except:
		showerror(message="Oops Unable to Open file.....")
		
def openFile():
	f = askopenfile(mode="r")
	t = f.read()
	text.delete(0.0, END)
	text.insert(0.0, t)



def copy():
       text.event_generate('<<Copy>>')

def cut():
          text.event_generate('<<Cut>>')

def paste():
       text.event_generate('<<Paste>>')

def undo():
	   text.event_generate('<<Undo>>')
	
def redo():
	   text.event_generate('<<Redo>>')
	
def select_all(event=None):
    text.tag_add('sel', '1.0', 'end')
    return "break"
    

def changeBg():
	(tripple, hexstr) = askcolor()
	if hexstr:
		text.config(bg=hexstr)
		
def changeFg():
        (triple, hexstr) = askcolor()
        if hexstr:
            text.config(fg=hexstr)
            
def bold():
	F_font = ('bold', 30)
	text.font=F_font
	
def about():
	messagebox.showinfo(title="about", message="Notepad v1, made by Sparks It education Comapny, Created to help people to help, vist website at www.spark4plusweb.wordpress.com or email at praisemcconnel@gmail.com")
	
def suggest():
	messagebox.askyesno(title="Suggest", message="Do u Want a Change")
	result = 0
	if result == 0:
		messagebox.showinfo(message="thanks for the feedback")
	
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New",accelerator="Ctrl+N", command=newFile)
filemenu.add_command(label="Open",accelerator="Ctrl+O", command=openFile)
filemenu.add_command(label="Save",   accelerator="Ctrl+S", command=saveFile)
filemenu.add_command(label="Save as",accelerator="Ctrl+Shift + S", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Copy",accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="Cut",accelerator="Ctrl+X", command=cut)
editmenu.add_command(label="Paste",accelerator="Ctrl+V", command=paste)
editmenu.add_command(label="Undo",accelerator="Ctrl+U", command=undo)
editmenu.add_command(label="Redo",accelerator="Ctrl+Y", command=redo)
editmenu.add_command(label="Select all",accelerator="Ctrl+A", command=select_all)
filemenu.add_separator()
menubar.add_cascade(label="edit", menu=editmenu)

formatmenu = Menu(menubar, tearoff=0)
formatmenu.add_command(label="Change Background", command=changeBg)
formatmenu.add_command(label="font Color", command=changeFg)
filemenu.add_separator()
menubar.add_cascade(label="Format", menu=formatmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="about", command=about)
helpmenu.add_command(label="suggest",command=suggest)
menubar.add_cascade(label="help", menu=helpmenu)

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)
root.bind('<Control-N>', newFile)
root.bind('<Control-n>', newFile)
root.bind('<Control-O>', openFile)
root.bind('<Control-o>', openFile)
root.bind('<Control-Shift-s>', saveAs)
root.bind('<Control-Shift-S>', saveAs)
root.bind('<Control-U>', undo)
root.bind('<Control-u>', undo)
root.bind('<Control-Y>', redo)
root.bind('<Control-y>', redo)
root.bind('<Control-X>', cut)
root.bind('<Control-x>', cut)





root.config(menu = menubar)
root.mainloop()
