import tkinter as tk
from tkinter import messagebox, ttk

from jsonFile import handel_file_json



class profile:
        def __init__(self, root):
            self.root = root
            self.root.title("User Management System")
            self.root.geometry("500x500")
            self.root.configure(bg='#f0f0f0')

        def show_profile_page(self, user):
            profile_window = tk.Toplevel(self.root)
            profile_window.title("User Profile")
            profile_window.geometry("500x500")
            profile_window.configure(bg='#ffffff')

            # Title
            title_label = tk.Label(profile_window, text="User Profile", font=("Arial", 18, "bold"), bg="#ffffff")
            title_label.pack(pady=20)

            # User Info Display
            info_frame = tk.Frame(profile_window, bg='#ffffff')
            info_frame.pack(pady=10)

            # Adding FontAwesome user icon
            user_icon = tk.PhotoImage(file="C:\\Users\\Abdallah\\Desktop\\868320_people_512x512.png")  # Load your image
            profile_img_label = tk.Label(info_frame, image=user_icon, bg="#ffffff")
            profile_img_label.image = user_icon  # Keep reference to avoid garbage collection
            profile_img_label.grid(row=0, column=0, padx=20, pady=5)

            # User Details
            details_frame = tk.Frame(info_frame, bg='#ffffff')
            details_frame.grid(row=0, column=1, padx=20, pady=10)

            tk.Label(details_frame, text=f"Name: {user['name']}", bg='#ffffff', font=("Arial", 12)).pack(anchor='w',
                                                                                                         pady=5)
            tk.Label(details_frame, text=f"Email: {user['email']}", bg='#ffffff', font=("Arial", 12)).pack(anchor='w',
                                                                                                           pady=5)
            tk.Label(details_frame, text=f"Phone: {user['phone']}", bg='#ffffff', font=("Arial", 12)).pack(anchor='w',
                                                                                                           pady=5)
            tk.Label(details_frame, text=f"Gender: {user['gender']}", bg='#ffffff', font=("Arial", 12)).pack(anchor='w',
                                                                                                             pady=5)
            tk.Label(details_frame, text=f"Age: {user['age']}", bg='#ffffff', font=("Arial", 12)).pack(anchor='w',
                                                                                                       pady=5)

            # Action Buttons
            btn_frame = tk.Frame(profile_window, bg='#ffffff')
            btn_frame.pack(pady=20)

            update_btn = tk.Button(btn_frame, text="Update Profile", command=lambda: self.update(user, profile_window),
                                   width=20, bg="#007BFF", fg="white", font=("Arial", 10, "bold"))
            update_btn.grid(row=0, column=0, padx=10, pady=5)

            delete_btn = tk.Button(btn_frame, text="Delete User", command=lambda: self.destroy(user, profile_window),
                                   width=20, bg="#FF0000", fg="white", font=("Arial", 10, "bold"))
            delete_btn.grid(row=0, column=1, padx=10, pady=5)

            timeline_btn = tk.Button(btn_frame, text="Timeline", command=lambda: self.Time(user), width=20,
                                     bg="#28A745", fg="white", font=("Arial", 10, "bold"))
            timeline_btn.grid(row=1, column=0, padx=10, pady=5)

            messages_btn = tk.Button(btn_frame, text="Messages", command=lambda: self.go_to_messages(user), width=20,
                                     bg="#FFC107", fg="black", font=("Arial", 10, "bold"))
            messages_btn.grid(row=1, column=1, padx=10, pady=5)

            notifications_btn = tk.Button(btn_frame, text="Notifications", command=lambda: self.go_to_not(user),
                                          width=20, bg="#17A2B8", fg="white", font=("Arial", 10, "bold"))
            notifications_btn.grid(row=2, column=0,  pady=5)

            send = tk.Button(btn_frame, text="Send freind request", command=lambda: self.request(user),
                                          width=20, bg="#17A2B8", fg="white", font=("Arial", 10, "bold"))
            send.grid(row=2, column=1,  pady=5)



        def update(self, user, window):
            window.destroy()  # Close previous window


            update_window = tk.Toplevel(self.root)
            update_window.title("Update Profile")
            update_window.geometry("400x400")
            update_window.configure(bg='#ffffff')

            tk.Label(update_window, text="Update Profile", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=20)

            def add_labeled_entry(label_text, user_key):
                tk.Label(update_window, text=label_text, bg='#ffffff', font=("Arial", 12)).pack(pady=5)
                entry = tk.Entry(update_window)
                entry.insert(0, user[user_key])
                entry.pack(pady=5)
                return entry

            name_entry = add_labeled_entry("Name", "name")
            email_entry = add_labeled_entry("Email", "email")
            phone_entry = add_labeled_entry("Phone", "phone")
            password_entry = add_labeled_entry("Password", "password")
            age_entry = add_labeled_entry("Age", "age")
            gender_entry = add_labeled_entry("Gender", "gender")

            def save_updated_data():
                user["name"] = name_entry.get()
                user["email"] = email_entry.get()
                user["phone"] = phone_entry.get()
                user["password"] = password_entry.get()
                user["age"] = age_entry.get()
                user["gender"] = gender_entry.get()

                js = handel_file_json()
                js.update_data("User", user)
                messagebox.showinfo("Success", "Profile updated successfully!")
                self.show_profile_page(user)
                update_window.destroy()

            save_btn = tk.Button(update_window, text="Save Changes", command=save_updated_data, width=20, bg="#4CAF50",
                                 fg="white", font=("Arial", 10, "bold"))
            save_btn.pack(pady=20)

        def destroy(self, user, window):
            js = handel_file_json()
            js.delete_data("User", user)
            messagebox.showinfo("Success", "User deleted successfully!")
            window.destroy()

        def go_to_messages(self, user):
            from todo import UserList
            obj = UserList(user)
            obj.root.mainloop()

        def go_to_not(self, user):
            from main import notGUI
            app = notGUI(user)
            app.root.mainloop()

        def Time(self, user):
            from anotherv import TimeLine
            obj = TimeLine(user)
            obj.loadPosts()


        def request(self,user):
            from sendfreindrequest import FriendRequestSystem
            objjj=FriendRequestSystem(user)






