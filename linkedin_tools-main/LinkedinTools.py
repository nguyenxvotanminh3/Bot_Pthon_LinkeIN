import tkinter as tk
from LinkedIn_group_Feature123 import Login_Linkedin, get_groups, auto_join_group, datetime, driver_Profile, auto_connect
from Auto_post_group import post_and_get_link_in_group
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.login = tk.Button(self, text="Login Linkedln", command=lambda: Login_Linkedin(driver))
        self.login.pack()

        self.auto_connect = tk.Button(self, text="Auto connect LinkedIn", command=lambda: auto_connect(driver))
        self.auto_connect.pack()

        self.join_group = tk.Button(self, text="Auto get groups LinkedIn", command=lambda: get_groups(driver))
        self.join_group.pack()

        self.join_group = tk.Button(self, text="Join groups LinkedIn", command=lambda: auto_join_group(driver))
        self.join_group.pack()

        self.post = tk.Button(self, text="Auto post LinkedIn", command=lambda: post_and_get_link_in_group(driver))
        self.post.pack()


        self.quit = tk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack()

start_time = datetime.now()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
root = tk.Tk()
app = Application(master=root)
app.master.title("LinkedIn auto tools")
app.master.minsize(300, 200)
app.mainloop()