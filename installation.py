from tkinter import Tk, mainloop, TOP
from tkinter.ttk import Label, Button
from tkinter import messagebox
from tkinter import filedialog as OpenFile
from pathlib import Path

root = Tk()
root.title('NEURALINE')
root.geometry('600x385+200+200')
root.resizable(False, False)

step1, step2, step3 = False, False, False
label00 = Label(root, text='', font='Arial 15 bold')

def check_python_version():
	import sys
	if sys.version_info[0] >= 3 and sys.version_info[1] >= 10: return True
	else: return False
def install_dependencies():
	if not step3:
		from Neuraline.Utilities.dependencies_installer import DependenciesInstaller
		dependencies_installer = DependenciesInstaller()
		dependencies_installer.install()
		dependencies_installer.describe()
		global step1
		step1 = True
	else: messagebox.showwarning('WARNING', 'ALL STEPS have already been performed!')
def sign_neuraline():
	if step1:
		from Neuraline.Utilities.subscribe import Subscribe
		subscribe = Subscribe()
		subscribe.subscribe()
		global step2
		step2 = True
	else: messagebox.showwarning('WARNING', 'Do STEP 1 first!')
def open_key_explorer():
	if step1 and step2:
		try: initial_dir = str(Path.home() / "Downloads")
		except: initial_dir = './'
		file_path = OpenFile.askopenfilename(title='Open Subscription KEY', initialdir=initial_dir, filetypes=(('Subscription KEY', '*.key'),))
		global label00
		from Neuraline.Utilities.subscribe import Subscribe
		if Subscribe().validateSignature(url_path=file_path):
			label00.config(text='Subscription SUCCESSFULLY VALIDATED!', foreground='green')
			global step3
			step3 = True
		else: label00.config(text='ERROR validating the signing key.', foreground='red')
	else: messagebox.showwarning('WARNING', 'Do STEP 2 first!')
label01 = Label(root, text='Neuraline - Installer', font='Arial 20').pack(side=TOP, pady=10)

button01 = Button(root, text='Step 1: Install Dependencies', width=50, command=install_dependencies).pack(side=TOP, pady=10)
button02 = Button(root, text='Step 2: Subscribe to Neuraline', width=50, command=sign_neuraline).pack(side=TOP, pady=10)
button03 = Button(root, text='Step 3: Validate the Subscription Key', width=50, command=open_key_explorer).pack(side=TOP, pady=10)

python310 = check_python_version()
if python310: text_label, color_label = '*Python 3.10 or higher installed', 'green'
else: text_label, color_label = '*Your Python version is not supported, please upgrade to version 3.10 or higher', 'red'
label02 = Label(root, text=text_label, font='Arial 8 bold', foreground=color_label).pack(side=TOP, pady=10)
label03 = Label(root, text='Note: You will need Chrome or Chromium to be installed on your machine.\nInstall one of the two if you haven`t already done so.', font='Arial 8 bold').pack(side=TOP, pady=10)
label00.pack(side=TOP, pady=10)

root.mainloop()
