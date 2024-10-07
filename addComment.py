import tkinter as tk
from tkinter import *
import json
class AddComment:
    def __init__(self,ID):
        self.user_data = ID
        self.user_id = ID["id"]

        self.root = tk.Tk()
        self.root.title("SIC Application")
        self.root.geometry("600x700")
        self.root.configure(bg="#E3F2FD")
        add_frame = tk.Frame(self.root, bg="#E3F2FD", bd=2, relief="groove")
        add_frame.pack(fill="x", side="bottom", pady=10)

        self.post = tk.Text(add_frame, width=60, height=2, font=('Helvetica', 12), bd=2)
        self.post.pack(side="left", padx=10, pady=5)

        self.button = tk.Button(add_frame, text="Share", font=('Helvetica', 12), bg="#1976D2", fg="#FFFFFF",
                                width=10,
                                command=self.add_comment)
        self.button.pack(side="right", padx=10)

        # Hover effect for the button
        # self.button.bind("<Enter>", lambda e: self.button.config(bg="#1565C0"))
        # self.button.bind("<Leave>", lambda e: self.button.config(bg="#1976D2"))
    def add_comment(self):
        with open("User.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        text = self.post.get("1.0", "end-1c").strip()
        user=data[self.user_id]


        with open("posts.json", "r", encoding="utf-8") as file:
            timeline = json.load(file)
            new= {
                "id": len(timeline),
                "user": user["name"],
                "content": text,
                "timestamp": "2024-09-25 12:34",
                "likes": 0,
                "by": self.user_id,
                "comments": [ ]
              }
            timeline.append(new)
            with open("posts.json", "w", encoding="utf-8") as file:
                json.dump(timeline, file, indent=2)

        self.root.destroy()





