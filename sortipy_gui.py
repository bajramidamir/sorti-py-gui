import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog


def sort(current_dir):
	output_dir = os.path.join(current_dir, '')
	Path(output_dir).mkdir(exist_ok=True)

	for f in os.listdir(current_dir):	
		if not os.path.isfile(os.path.join(current_dir, f)):
			continue
			
		name, ext = os.path.splitext(f)
		ext = ext[1:]
		fpath = os.path.join(current_dir, f)
		ext_output_dir = os.path.join(output_dir, ext, '')
		if not ext:
			ext_output_dir = os.path.join(output_dir, 'noextension', '')
		Path(ext_output_dir).mkdir(exist_ok=True)
		
		# try to move 
		try:
			shutil.move(fpath, ext_output_dir)
		# catch exception when we have two files with the same name, rename the second one and move
		except shutil.Error:
			shutil.move(fpath, os.path.join(ext_output_dir, name + "_new" + "." + ext))
		


def dir_prompt():
	path_entry = filedialog.askdirectory()
	sort(path_entry)


# /////////////// Tkinter defs
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
