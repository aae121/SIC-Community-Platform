import tkinter as tk
from tkinter import *
import json
from datetime import datetime


class CommentPage:
    def __init__(self,post_id,ID):
        self.user_data = ID
        self.user_id = ID["id"]
        self.post_id = post_id
        self.root = tk.Tk()
        self.root.title("Islamic Application")
        self.root.geometry("600x700")
        self.root.configure(bg="#E3F2FD")
        self.title_label = tk.Label(self.root, text="Comments", font=("Helvetica Neue Bold", 24), fg="#0D47A1",
                                    bg="#E3F2FD")
        self.title_label.pack(pady=10)

    def show_comments(self):
        with open("posts.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()

        for post in data:
            if post["id"] == self.post_id:
                for comment in post["comments"]:
                    comment_frame = tk.Frame(self.root, bg="#FFFFFF", bd=2, relief="groove",
                                             highlightbackground="#BBDEFB")
                    comment_frame.pack(fill="x", pady=15, padx=10, anchor="center")

                    comment_user = tk.Label(comment_frame, text=all[comment['who']]['name'], font=("Helvetica", 12, "bold"),
                                            fg="#0D47A1")
                    comment_user.pack(anchor="w", padx=10, pady=2)

                    comment_label = tk.Label(comment_frame, text=comment['comment'], font=("Helvetica", 12),
                                             fg="#1E88E5")
                    comment_label.pack(anchor="w", padx=10, pady=2)

                    # Frame to add new comments
                add_frame = tk.Frame(self.root, bg="#E3F2FD", bd=2, relief="groove")
                add_frame.pack(fill="x", side="bottom", pady=10)

                self.comment = tk.Text(add_frame, width=60, height=2, font=('Helvetica', 12), bd=2)
                self.comment.pack(side="left", padx=10, pady=5)

                self.button = tk.Button(add_frame, text="Share", font=('Helvetica', 12), bg="#1976D2", fg="#FFFFFF",
                                        width=10,
                                        command=lambda p=post: self.add_comment(p, data))
                self.button.pack(side="right", padx=10)

                # Hover effect for the button
                self.button.bind("<Enter>", lambda e: self.button.config(bg="#1565C0"))
                self.button.bind("<Leave>", lambda e: self.button.config(bg="#1976D2"))
                #     comment_frame = tk.Frame(self.root, bg="black", bd=3, relief="groove")
                #     comment_frame.pack(fill="x", pady=10, padx=10, anchor="center")
                #     comment_user = tk.Label(comment_frame, text=comment['user'], font=("Helvetica", 10))
                #     comment_user.pack(anchor="w", padx=20, pady=2)
                #     comment_label = tk.Label(comment_frame, text=comment['comment'], font=("Helvetica", 10))
                #     comment_label.pack(anchor="w", padx=20, pady=2)
                #
                # add_frame = tk.Frame(self.root, bg="black", bd=3, relief="groove")
                # add_frame.pack(fill="x", side="bottom")
                # self.button = tk.Button(add_frame, text="share", font=('arial', 12),
                #                         command=lambda p=post: self.add_comment(p, data))
                # self.button.pack(side="right")
                #
                # self.comment = tk.Text(add_frame, width=61, height=1, font=('arial', 10))
                # self.comment.pack(side="left")

        self.root.mainloop()

    def add_comment(self, post, data):
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()

        new_comment = self.comment.get("1.0", "end-1c").strip()
        if new_comment:
            post["comments"].append({
                "user": "Anonymous",
                "comment": new_comment,
                "timestamp": datetime.now().isoformat(),
                "who" : self.user_id
            })
            from main import Notifications
            objj=Notifications()
            objj.add_notification(post["by"],"comment",f"You have a new comment from {all[self.user_id]['name']}",post['id'])
            with open("posts.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
            self.root.destroy()


    # def add_comment(self,post,data):
    #     # file = open("posts.json", "r",encoding="utf-8")
    #     # data = json.load(file)  # hena h impot json 34an a5od el data
    #     # file.close()
    #     new_comment = self.comment.get("1.0", "end-1c").strip()
    #     if new_comment:
    #         print("hi")
    #         post["comments"].append({
    #             "user": "Anonymous",
    #             "comment": new_comment,
    #             "timestamp": "2024-09-25T14:00:00"  # Example timestamp, replace with actual timestamp in a real app
    #             })
    #         with open("posts.json", "w", encoding="utf-8") as file:
    #             json.dump(data, file, indent=2)
            # button.config(text=f"Like ({comment['comment']})")
            # comment.append({"comment":"new_comment"})
            # file = open("posts.json", "w", encoding="utf-8")
            # json.dump(post, file, indent=2)  # write in json
            # file.close()

# CommentPage().show_comments()

