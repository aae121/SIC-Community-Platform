import tkinter as tk
from tkinter import messagebox
import json
class FriendRequestSystem:
    def __init__(self,ID):
        self.user_data = ID
        self.user_id = ID["id"]
        self.root = tk.Tk()
        self.root.title("Samsung Friend Request System")
        self.root.geometry("500x400")
        self.root.config(bg="#e6f2ff")
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()

        # Sample user data
        self.users = all

        # Create a frame for the search section
        self.frame_search = tk.Frame(self.root, bg="#e6f2ff")
        self.frame_search.pack(pady=10)

        self.label_search = tk.Label(self.frame_search, text="Search User:", font=("Helvetica", 14, "bold"), bg="#e6f2ff", fg="#005bb5")
        self.label_search.pack(side="left", padx=5)

        self.entry_search = tk.Entry(self.frame_search, font=("Helvetica", 14), width=20, bd=2, relief="solid")
        self.entry_search.pack(side="left", padx=5)

        # Search button
        self.button_search = tk.Button(self.frame_search, text="Search", font=("Helvetica", 12, "bold"), fg="white", bg="#005bb5",
                                       activebackground="#004080", cursor="hand2", command=self.search_users)
        self.button_search.pack(side="left", padx=5)

        # Create a canvas for displaying user search results
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg="#0073e6", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Scrollbar for canvas
        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a scrollable frame inside the canvas
        self.scrollable_frame = tk.Frame(self.canvas, bg="#e6f2ff")
        self.scrollable_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Bind the scrollable frame to update the scroll region
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    # Function to simulate sending a friend request
    def send_friend_request(self, id):
        #messagebox.showinfo("Friend Request", f"Friend request sent to {user_name}!")
        from main import Notifications
        objj = Notifications()
        objj.add_notification(id, "freind", f"You have a new freind request from {self.users[self.user_id]['name']}",
                              self.user_id)


    def search_users(self):
        query = self.entry_search.get().lower()
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        matching_users = []

        for user in self.users:
            if user["id"]==self.user_id:
                continue

            if user["name"].lower().startswith(query):
                matching_users.append(user)

        if not matching_users:
            no_results_label = tk.Label(self.scrollable_frame, text="No users found.", font=("Helvetica", 12), fg="red")
            no_results_label.pack(pady=10)
            return

        for user in matching_users:
            user_info = f"{user['name']}, Age: {user['age']}, Location: {user['patch']}"
            label = tk.Label(self.scrollable_frame, text=user_info, font=("Helvetica", 12, "bold"), anchor="w", bg="#e6f2ff", fg="#005bb5")
            label.pack(fill="x", pady=5, padx=10)

            button = tk.Button(self.scrollable_frame, text="Send Friend Request", font=("Helvetica", 10, "bold"), fg="white", bg="#0073e6",
                               activebackground="#005bb5", cursor="hand2", command=lambda u=user["id"]: self.send_friend_request(u))
            button.pack(pady=5)

        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))





