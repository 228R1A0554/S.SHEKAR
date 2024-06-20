import winapps
import os
import logging
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as messagebox
class AppNotFoundException(Exception):
    pass

    class ApplicationManager:
        def __init__(self):

             self.history = []
                   self.config = {}

    def search_app_details(self, app_name):
        if not app_name:
            raise ValueError("Application name cannot be empty")

    for item in winapps.search_installed(app_name):
        details = {
            'name': item.name,
            'version': item.version,
            'install_date': item.install_date,
            'publisher': item.publisher,
            'uninstall_string': item.uninstall_string
        }
        self.history.append(details)
        return details
raise AppNotFoundException(f"No application found with the name: {app_name}")


        def uninstall_application(self, uninstall_string):
    if not uninstall_string:
raise ValueError("Uninstall string cannot be empty")


                   os.system(uninstall_string)


        def list_all_installed_apps(self):
            return [item.name for item in winapps.list_installed()]


        def search_by_publisher(self, publisher_name):
            if not publisher_name:
                raise ValueError("Publisher name cannot be empty")


        apps = [item for item in winapps.list_installed() if item.publisher == publisher_name]
        if not apps:
            raise AppNotFoundException(f"No applications found for publisher: {publisher_name}")
                   return apps


        def save_search_history(self, file_path):
            with open(file_path, 'w') as file:
                for entry in self.history:
                file.write(f"{entry}\n")
def load_search_history(self, file_path):
                self.history = []
with open(file_path, 'r') as file:
                for line in file:
self.history.append(eval(line.strip()))
def set_config(self, key, value):
  self.config[key] = value
def get_config(self, key):
  return self.config.get(key, None)
def setup_logging(log_file):
 logging.basicConfig(filename=log_file, level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s')
logging.info("Application Manager initialized")
def show_app_details():
app_name = app_name_entry.get()
clear_fields()
if app_name:
try:
details = app_manager.search_app_details(app_name)
name.set(details['name'])
version.set(details['version'])
install_date.set(details['install_date'])
publisher.set(details['publisher'])
uninstall_string.set(details['uninstall_string'])
not_found_label.place_forget()
        except AppNotFoundException as e:
not_found_label.place(relx=0.5, rely=0.9, anchor=CENTER)
        except ValueError as e:
messagebox.showerror("Error", str(e))
else:
messagebox.showerror("Error", "Please enter an application name.")
def clear_fields():
name.set("")
version.set("")
install_date.set("")
publisher.set("")
uninstall_string.set("")
app_name_entry.delete(0, END)
not_found_label.place_forget()
def uninstall_app():
try:
uninstall_str = uninstall_string.get()
if uninstall_str:
app_manager.uninstall_application(uninstall_str)
messagebox.showinfo("Success", "Application uninstalled successfully.")
else:
messagebox.showerror("Error", "No uninstall string available.")
   except Exception as e:
messagebox.showerror("Error", str(e))
def list_all_apps():
try:
apps = app_manager.list_all_installed_apps()
messagebox.showinfo("Installed Applications", "\n".join(apps))
except Exception as e:
messagebox.showerror("Error", str(e))
root = Tk()
root.title("Application Search Tool")
# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
# Setup logging
setup_logging('app_manager.log')
# Background image setup
background_image_path = "Best-Background-Images-for-Marketing-Needs-Vector-1.jpg"
background_image = Image.open(background_image_path)
background_image = background_image.resize((screen_width, screen_height),
Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = ttk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()
root.configure(bg='light blue')
font_size = 14
app_manager = ApplicationManager()
name = StringVar()
version = StringVar()
install_date = StringVar()
publisher = StringVar()
uninstall_string = StringVar()
labels = ["Name:", "Version:", "Install Date:", "Publisher:", "Uninstall String:"]
for i, label_text in enumerate(labels, start=2):
label = ttk.Label(root, text=label_text, style="Label.TLabel", font=('Helvetica', font_size))
label.place(relx=0.32, rely=0.1*i, anchor=W)
entry_fields = [name, version, install_date, publisher, uninstall_string]
for i, entry_var in enumerate(entry_fields, start=2):
entry = ttk.Entry(root, textvariable=entry_var, width=38, font=('Helvetica', font_size))
entry.place(relx=0.7, rely=0.1*i, anchor=E)
app_name_entry = ttk.Entry(root, width=50, font=('Helvetica', font_size),
style='App.TEntry')
app_name_entry.place(relx=0.5, rely=0.8, anchor=CENTER)
style = ttk.Style()
style.configure('App.TEntry', background='light yellow')
style.configure('TButton', font=('Helvetica', font_size))
show_button = ttk.Button(root, text="Search", command=show_app_details,
style='TButton')
show_button.place(relx=0.5, rely=0.85, anchor=W)
clear_button = ttk.Button(root, text="Clear", command=clear_fields, style='TButton')
clear_button.place(relx=0.6, rely=0.85, anchor=W)
uninstall_button = ttk.Button(root, text="Uninstall", command=uninstall_app,
style='TButton')
uninstall_button.place(relx=0.7, rely=0.85, anchor=W)
list_button = ttk.Button(root, text="List All", command=list_all_apps, style='TButton')
list_button.place(relx=0.8, rely=0.85, anchor=W)
style.configure("Label.TLabel", background="light grey")
heading_label = ttk.Label(root, text="Application Search Tool", font=('Helvetica', 20, 'bold'),
background='light yellow')
heading_label.place(relx=0.5, rely=0.04, anchor=N)
not_found_label = ttk.Label(root, text="Application not found.", font=('Helvetica', 14),
foreground='red', background='light blue')
root.mainloop()

