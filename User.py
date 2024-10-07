import tkinter as tk
from tkinter import font as tkfont
from jsonFile import handel_file_json
from tkinter import PhotoImage, messagebox
from profile import profile
import json

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("700x700")
        self.root.configure(bg='#f4f4f4')

        # Set the fonts
        title_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
        regular_font = tkfont.Font(family="Helvetica", size=12)

        # Title Label
        title_label = tk.Label(self.root, text="SIC COMMUNITY", font=title_font, bg='#f4f4f4', fg='#333333')
        title_label.pack(pady=(20, 10))

        # Welcome Message
        welcome_label = tk.Label(self.root, text="Welcome back to your social app!", font=regular_font,
                                 bg='#f4f4f4', fg='#333333')
        welcome_label.pack(pady=(0, 20))

        # Login Frame
        login_frame = tk.Frame(self.root, bg='#f4f4f4')
        login_frame.pack(padx=20, pady=10)

        # Username/Email Label and Entry
        email_label = tk.Label(login_frame, text="UserName / Email :", font=regular_font, bg='#f4f4f4', fg='#333333')
        email_label.grid(row=0, column=0, sticky='w', pady=10)

        email_entry = tk.Entry(login_frame, font=regular_font, width=30, bd=1, relief='solid')
        email_entry.grid(row=0, column=1, pady=10)

        # Password Label and Entry
        password_label = tk.Label(login_frame, text="Password :", font=regular_font, bg='#f4f4f4', fg='#333333')
        password_label.grid(row=1, column=0, sticky='w', pady=10)

        password_entry = tk.Entry(login_frame, font=regular_font, show='*', width=30, bd=1, relief='solid')
        password_entry.grid(row=1, column=1, pady=10)

        # Sign Up Text
        signup_frame = tk.Frame(self.root, bg='#f4f4f4')
        signup_frame.pack(pady=(10, 20))

        signup_label = tk.Label(signup_frame, text="Don't have an account?", font=regular_font, bg='#f4f4f4',
                                fg='#333333')
        signup_label.pack(side='left')

        signup_button = tk.Button(signup_frame, text="Sign UP", font=regular_font, bg='#f4f4f4', fg='blue', bd=0,
                                  cursor='hand2', command=self.open_register_page)
        signup_button.pack(side='left')

        def submit_login():
            get = handel_file_json()
            users = get.get_data("User")
            email = email_entry.get()
            password = password_entry.get()
            for user in users:

                if user["email"] == email and user["password"] == password:
                    messagebox.showinfo("Success", "User login successfully!")
                    self.user = user
                    self.open_profile_page()
                    return

            messagebox.showerror("Error", "User not found or password is incorrect")

        login_button = tk.Button(self.root, text="Login", font=regular_font, bg='#4CAF50', fg='#ffffff', width=20,
                                 height=2, cursor='hand2', command=submit_login)
        login_button.pack(pady=(20, 10))

    def open_register_page(self, from_back=False):
        # if not from_back:
        # self.page_stack.append("register")

        # self.clear_window()

        register_window = tk.Frame(self.root)
        register_window.pack()

        name_label = tk.Label(register_window, text="Name")
        name_label.pack()
        name_entry = tk.Entry(register_window)
        name_entry.pack()

        email_label = tk.Label(register_window, text="Email")
        email_label.pack()
        email_entry = tk.Entry(register_window)
        email_entry.pack()

        password_label = tk.Label(register_window, text="Password")
        password_label.pack()
        password_entry = tk.Entry(register_window, show="*")
        password_entry.pack()

        gender_label = tk.Label(register_window, text="Gender")
        gender_label.pack()
        gender_entry = tk.Entry(register_window)
        gender_entry.pack()

        governorate_label = tk.Label(register_window, text="Governorate")
        governorate_label.pack()
        governorate_entry = tk.Entry(register_window)
        governorate_entry.pack()

        age_label = tk.Label(register_window, text="Age")
        age_label.pack()
        age_entry = tk.Entry(register_window)
        age_entry.pack()

        national_id_label = tk.Label(register_window, text="National ID")
        national_id_label.pack()
        national_id_entry = tk.Entry(register_window)
        national_id_entry.pack()

        phone_label = tk.Label(register_window, text="Phone")
        phone_label.pack()
        phone_entry = tk.Entry(register_window)
        phone_entry.pack()

        def submit_register():
            js = handel_file_json()
            users = js.get_data("User")

            email = email_entry.get()
            if any(user["email"] == email for user in users):
                messagebox.showerror("Error", "Email is already in use.")
                return

            userdata = {
                "id": len(users),
                "name": name_entry.get(),
                "phone": phone_entry.get(),
                "email": email,
                "gender": gender_entry.get(),
                "password": password_entry.get(),
                "gavernorate": governorate_entry.get(),
                "age": age_entry.get(),
                "patch": national_id_entry.get(),
                "role": "user",
                "freinds" : []
            }
            if not all(userdata.values()):
                messagebox.showerror("Error", "Register failed, please enter all data")
            else:
                js.adde("User", userdata)
                messagebox.showinfo("Success", "User registered successfully!")
                self.prep_files()
                # self.create_main_page()

        register_btn = tk.Button(register_window, text="Submit", command=submit_register)
        register_btn.pack(pady=10)

        # if len(self.page_stack) > 1:
        #     back_button = tk.Button(self.root, text="Back", command=self.go_back)
        #     back_button.pack(pady=5)

    def open_profile_page(self):
        p = profile(self.root)
        p.show_profile_page(self.user)

    def prep_files(self):
        file = open('notifc.json', 'r')
        PREP = json.load(file)
        file.close()
        PREP.append([])
        file = open("notifc.json", 'w')
        json.dump(PREP, file, indent=4)
        file.close()
        file = open('data.json', 'r')
        PREP = json.load(file)
        file.close()
        PREP.append([])
        file = open("data.json", 'w')
        json.dump(PREP, file, indent=4)
        file.close()


# Main Application Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
