import tkinter as tk
from tkinter import *
import json
import comments
from datetime import datetime
import addComment

timeLineStack = []


class TimeLine:
    def __init__(self,ID):
        self.user_data = ID
        self.user_id = ID["id"]
        self.root = tk.Tk()
        self.root.title("SIC Application")
        self.root.geometry("600x700")
        self.root.configure(bg="#E3F2FD")

        # self.root.configure(bg="#E3F2FD")
        self.title_label = tk.Label(self.root, text="SIC", font=("Pacifico", 24), fg="#0D47A1",
                                    bg="#E3F2FD")
        self.title_label.pack(pady=10)
        self.canvas = tk.Canvas(self.root, bg="#E3F2FD")
        self.canvas.pack(side=LEFT, expand=True, fill="both")
        self.scroll_bar = Scrollbar(self.root, command=self.canvas.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)
# ___________________________________________________________________________________________________________-

        self.canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.timeline_frame = tk.Frame(self.canvas,bg="#FFFFFF",)
        self.canvas.create_window((300, 0), window=self.timeline_frame, anchor="n")
        self.timeline_frame.bind("<Configure>", self.on_frame_configure)
#                          byzbt el scroll bar bs lsa msh 3arf azbtoh awy w dh mn google
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#____________________________________________________________________________________________________________--------
    def loadPosts(self):
        global timeLineStack
        with open("posts.json", "r",encoding="utf-8") as file:
            data = json.load(file)
        timeLineStack = data

        file = open('user.json', 'r')
        all = json.load(file)
        file.close()

        for post in timeLineStack:#btlf 3la el stack elly feha el posts w hya global 5lo balko
            if post["by"] == int(self.user_id) :  # ma yetba3sh postaty
                continue
            post["timestamp"] = self.format_timestamp(post["timestamp"])

            post_frame = tk.Frame(self.timeline_frame, bg="#FFFFFF", bd=2, relief="groove",
                                  highlightbackground="#BBDEFB")
            post_frame.pack(fill="x", pady=15, padx=10)
            timestamp_label = tk.Label(post_frame, text=post["timestamp"], font=("Helvetica Neue Bold", 12),
                                       fg="#0D47A1",bg="white")
            timestamp_label.pack(anchor="e", padx=10, pady=5)


            user_label = tk.Label(post_frame, text=all[post["by"]]["name"], font=("foldit", 18),
                                       fg="#0D47A1",bg="white")
            user_label.pack(anchor="w", padx=10, pady=5)



            content_label = tk.Label(post_frame, text=post["content"], font=("Helvetica", 14), fg="#1E88E5",)
            content_label.pack(anchor="w", padx=10, pady=5)

            like_button = tk.Button(post_frame, text=f"Like ({post['likes']})", bg="#1976D2", fg="#FFFFFF")
            like_button.pack(side="left", padx=10, pady=5)
            like_button.config(command=lambda p=post,btn=like_button:self.likePost(p,btn))

            # Hover effect for buttons
            like_button.bind("<Enter>", lambda e: like_button.config(bg="#1565C0"))
            like_button.bind("<Leave>", lambda e: like_button.config(bg="#1976D2"))

            comment_button = tk.Button(post_frame, text="Comment", bg="#1976D2", fg="#FFFFFF",
                                       command=lambda p=post: self.showComment(p["id"]))
            comment_button.pack(side="left", padx=5, pady=5)
            comment_button.bind("<Enter>", lambda e: comment_button.config(bg="#1565C0"))
            comment_button.bind("<Leave>", lambda e: comment_button.config(bg="#1976D2"))

            # Adding a separator line
            separator = tk.Frame(self.timeline_frame, height=1, bg="#BBDEFB")
            separator.pack(fill="x", padx=10)

        add_frame = tk.Frame(self.root, bg="#E3F2FD", bd=2, relief="groove")
        add_frame.pack( side="bottom", pady=10)
        add_frame.grid_columnconfigure(0, weight=1)
        self.button = tk.Button(add_frame, text="Add Post", font=('Helvetica', 12), bg="#1976D2", fg="#FFFFFF",
                                width=10,
                                command=self.add_post)
        # self.button.pack( padx=10)
        self.button.grid(row=0, column=0, pady=5)

        self.root.mainloop()

    def format_timestamp(self, timestamp):
        """Format timestamp from ISO format to a more readable format."""
        return datetime.fromisoformat(timestamp).strftime("%Y-%m-%d %H:%M")

    def likePost(self, post,button):
        # print(post["likes"])
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()

        post["likes"] += 1
        from main import Notifications
        objj = Notifications()
        objj.add_notification(post["by"], "like", f"You have a new like from {all[self.user_id]['name']}",
                              post['id'])
        # print(post["likes"])
        button.config(text=f"Like ({post['likes']})")
        with open("posts.json", "w", encoding="utf-8") as file:
            json.dump(timeLineStack, file, indent=2)

        # neb3at lel notifications

    def showComment(self,post_id):
        self.root.destroy()
        comments.CommentPage(post_id,self.user_data).show_comments()

    def onePost(self,post_id) :
            file = open('user.json', 'r')
            all = json.load(file)
            file.close()

            with open("posts.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            data[post_id]["timestamp"] = self.format_timestamp(data[post_id]["timestamp"])

            post_frame = tk.Frame(self.timeline_frame, bg="#FFFFFF", bd=2, relief="groove",
                                  highlightbackground="#BBDEFB")
            post_frame.pack(fill="x", pady=15, padx=10)
            timestamp_label = tk.Label(post_frame, text=data[post_id]["timestamp"], font=("Helvetica Neue Bold", 12),
                                       fg="#0D47A1", bg="white")
            timestamp_label.pack(anchor="e", padx=10, pady=5)

            user_label = tk.Label(post_frame, text=all[data[post_id]["by"]]["name"], font=("foldit", 18),
                                  fg="#0D47A1", bg="white")
            user_label.pack(anchor="w", padx=10, pady=5)

            content_label = tk.Label(post_frame, text=data[post_id]["content"], font=("Helvetica", 14), fg="#1E88E5", )
            content_label.pack(anchor="w", padx=10, pady=5)

            like_button = tk.Button(post_frame, text=f"Like ({data[post_id]['likes']})", bg="#1976D2", fg="#FFFFFF")
            like_button.pack(side="left", padx=10, pady=5)
            like_button.config(command=lambda p=data[post_id], btn=like_button: self.likePost(p, btn))

            # Hover effect for buttons
            like_button.bind("<Enter>", lambda e: like_button.config(bg="#1565C0"))
            like_button.bind("<Leave>", lambda e: like_button.config(bg="#1976D2"))

            comment_button = tk.Button(post_frame, text="Comment", bg="#1976D2", fg="#FFFFFF",
                                       command=lambda p=data[post_id]: self.showComment(p["id"]))
            comment_button.pack(side="left", padx=5, pady=5)
            comment_button.bind("<Enter>", lambda e: comment_button.config(bg="#1565C0"))
            comment_button.bind("<Leave>", lambda e: comment_button.config(bg="#1976D2"))

            # Adding a separator line
            separator = tk.Frame(self.timeline_frame, height=1, bg="#BBDEFB")
            separator.pack(fill="x", padx=10)

            self.root.mainloop()
    def add_post(self):
        self.root.destroy()
        addComment.AddComment(self.user_data)
        # timeLineStack.append()
        # with open("posts.json", "w", encoding="utf-8") as file:
        #     json.dump(timeLineStack, file, indent=2)



# TimeLine(self.user_id).loadPosts()
