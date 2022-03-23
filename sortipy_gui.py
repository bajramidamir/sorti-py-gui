import tkinter as tk
from tkinter import filedialog
import os
import shutil

def sort(path):
	lista = os.listdir(path)
	for f in lista:
		name, ext = os.path.splitext(f)
		ext = ext[1:]

		if ext == "":
			continue

		if os.path.exists(path + "/" + ext):
			shutil.move(path + "/" + f, path + "/" + ext + "/")
	
		else:
			os.makedirs(path + "/" + ext)
			shutil.move(path + "/" + f, path + "/" + ext + "/")

	success = tk.Label(window, text = "Success!", font = "Consolas")
	success.pack()


def dir_prompt():
	path_entry = filedialog.askdirectory()
	sort(path_entry)


# / / / / / / / / / / /
# tkinter defs
window = tk.Tk()
window.geometry("500x200")
window.title("Sorti-Py")

greeter = tk.Label(window, text = "Welcome to Sorti-Py!", font = "Consolas")
greeter.pack()
prompt = tk.Label(window, text = "Select the directory you want sorted: ",
font = "Consolas")
prompt.pack()

path_button = tk.Button(window, font = "Consolas", text = "Choose Directory", width = "20",
command = dir_prompt)
path_button.pack()

window.mainloop()
