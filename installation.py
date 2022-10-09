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
	else: messagebox.showwarning('AVISO', 'TODAS as ETAPAS já foram executadas!')
def sign_neuraline():
	if step1:
		from Neuraline.Utilities.subscribe import Subscribe
		subscribe = Subscribe()
		subscribe.subscribe()
		global step2
		step2 = True
	else: messagebox.showwarning('AVISO', 'Execute primeiro a ETAPA 1!')
def open_key_explorer():
	if step1 and step2:
		try: initial_dir = str(Path.home() / "Downloads")
		except: initial_dir = './'
		file_path = OpenFile.askopenfilename(title='Open Subscription KEY', initialdir=initial_dir, filetypes=(('Subscription KEY', '*.key'),))
		global label00
		from Neuraline.Utilities.subscribe import Subscribe
		if Subscribe().validateSignature(url_path=file_path):
			label00.config(text='Assinatura VALIDADA COM SUCESSO!', foreground='green')
			global step3
			step3 = True
		else: label00.config(text='ERRO na validação da chave de assinatura.', foreground='red')
	else: messagebox.showwarning('AVISO', 'Execute primeiro a ETAPA 2!')
label01 = Label(root, text='Neuraline - Instalador', font='Arial 20').pack(side=TOP, pady=10)

button01 = Button(root, text='Etapa 1: Instalar Dependências', width=50, command=install_dependencies).pack(side=TOP, pady=10)
button02 = Button(root, text='Etapa 2: Assinar o Neuraline', width=50, command=sign_neuraline).pack(side=TOP, pady=10)
button03 = Button(root, text='Etapa 3: Validar a Chave de Assinatura', width=50, command=open_key_explorer).pack(side=TOP, pady=10)

python310 = check_python_version()
if python310: text_label, color_label = '*Python 3.10 ou superior instalado', 'green'
else: text_label, color_label = '*Sua versão do Python não é compatível, atualize para a versão 3.10 ou superior', 'red'
label02 = Label(root, text=text_label, font='Arial 8 bold', foreground=color_label).pack(side=TOP, pady=10)
label03 = Label(root, text='Obs: Você precisará que o Chrome ou o Chromium estejam instalados na sua máquina.\nInstale um dos dois caso ainda não o tenha feito.', font='Arial 8 bold').pack(side=TOP, pady=10)
label00.pack(side=TOP, pady=10)

root.mainloop()
