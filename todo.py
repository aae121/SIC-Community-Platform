import tkinter as tk
from tkinter import messagebox, scrolledtext,PhotoImage
import json
from datetime import datetime
from tkinter import Canvas
from main import Notifications


class MessagingSystem:
    def __init__(self):

        self.data = []
        self.load_messages()

    def load_messages(self):
        file = open('data.json', 'r')
        data = json.load(file)
        file.close()
        self.data = data

    # def get_data(self, user_id):
    #     to_show = []
    #     for i in range(len(self.data)):
    #         if i != user_id:
    #             to_show.append(i)
    #     return to_show

    def save_messages(self):
        file = open('data.json', 'w')
        json.dump(self.data, file, indent=4)
        file.close()

    def send_message(self, from_id, to_id, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #te7wl el boj le string
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()
        obj=Notifications()

        obj.add_notification(to_id,"message",f"You have a new message from{all[from_id]['name']}",from_id)
        self.load_messages()

        self.data[from_id].append({
            "type": "s",
            "with": int(to_id),
            "message": message,
            "date": timestamp
        })

        self.data[to_id].append({
            "type": "r",
            "with": int(from_id),
            "message": message,
            "date": timestamp
        })

        self.save_messages()

    def show_messages_sorted(self, user_id):
        self.load_messages()
        user_id = int(user_id)
        user_messages = self.data[user_id]
        self.bubble_sort(user_messages)

        new = {}
        for i in user_messages:
            if i["with"] in new.keys():
                new[i["with"]].append(i)
            else:
                new.update({i["with"]: []})
                new[i["with"]].append(i)

        return new

    def convert_to_datetime(self, date_str):                 #te7wal el string le date obj ner3f ne3ml comp
        return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

    def bubble_sort(self, messages):   # ya rab al7a2 a3mlha quick sort
        n = len(messages)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.convert_to_datetime(messages[j]["date"]) < self.convert_to_datetime(messages[j + 1]["date"]):
                    messages[j], messages[j + 1] = messages[j + 1], messages[j]


class UserList:
    def __init__(self,ID):
        self.user_data=ID
        self.user_id=ID["id"]
        self.root = tk.Toplevel()
        self.root.title("Samsung Chat List")
        self.root.geometry("800x750")


        self.canvas = Canvas(self.root, bg="#E3F2FD")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.background_image_path = r"C:\Users\Abdallah\Downloads\Samsung-Innovation-Campus-1000x576.png"
        self.background_image = PhotoImage(file=self.background_image_path)


        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")

        self.messaging_system = MessagingSystem()
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.root, textvariable=self.search_var)
        self.canvas.create_window(165, 20, window=self.search_entry, width=300,height=22)

        self.sign_up = tk.Label(self.root, text="SEARCH", font=('Georgia', 12, 'bold'), bg='#ffffff',
                                fg='#2196F3', cursor='hand2')
        self.canvas.create_window(370,20,window= self.sign_up, width=80,height=22)
        #self.sign_up.pack(pady=10)
        self.sign_up.bind("<Button-1>", self.show_one)

       # self.side_image_path = r"C:\Users\Abdallah\Desktop\featured-image-2-modified.png"
       # self.side_image = PhotoImage(file=self.side_image_path)


        #self.canvas.create_image(1200, 775, image=self.side_image)



        self.display_users(self.user_id)
    def display_users(self,id):

        y_offset = 35
        data=self.messaging_system.show_messages_sorted(id)

        file = open('user.json', 'r')
        all = json.load(file)
        file.close()
        self.default_image_path = "C:\\Users\\Abdallah\Desktop\\62f4bc4dc414b.png"
        self.default_image = PhotoImage(file=self.default_image_path)


# "C:\Users\Abdallah\Desktop\62f4bc4dc414b.png"
        for user in data.items():   # ( id , list of messages(dict) with this id )

            if user [0] not in  all[self.user_id]["freinds"] :
                continue

            rectangle = self.canvas.create_rectangle(15, y_offset, 450, y_offset + 80, fill="#ffffff", outline="")



            self.canvas.tag_bind(rectangle, "<Button-1>", lambda event, idx=user[0]: self.on_rectangle_click(idx, event))
           # self.canvas.create_oval(25, y_offset + 10, 85, y_offset + 70, fill="#2196F3", outline="#BBDEFB")
            self.canvas.create_image(55, y_offset + 40, image=self.default_image)




            self.canvas.create_text(95, y_offset + 20, anchor="w", text=all[user[0]]["name"], font=("Helvetica", 13, "bold"),
                                    fill="#1E88E5")

            self.canvas.create_text(95, y_offset + 45, anchor="w", text=user[1][0][ "message"], font=("Helvetica", 11),
                                    fill="#607D8B")
            self.canvas.create_text(400, y_offset + 20, anchor="e", text=user[1][0][ "date"], font=("Helvetica", 11),
                                    fill="#78909C")

            y_offset += 90

    def on_rectangle_click(self, idx, event):
        chat_window = ChatWindow(self.root, idx, self.messaging_system,self.user_id)

    def show_one(self,event):
        name=self.search_entry.get()
        print(name)
        userschatedwith= self.messaging_system.show_messages_sorted(self.user_id).keys()
        print(self.root.focus_get())
        flag=0
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()
        idx=None
        for i in userschatedwith :         #linear search
            if name == all[int(i)]["name"] :
                flag=1
                idx=int(i)
                break

        if flag :
            #print(name)  #5atwa search na2sa
            if messagebox.askyesno("go to message ",f"do u want to open the chat with {name}") and idx in all[self.user_id]["freinds"] :
                chat_window = ChatWindow(self.root, int(idx), self.messaging_system, self.user_id)
            else:
                messagebox.showerror("return",f"{name} not in your freind list ")
                return

        else :
             messagebox.showwarning("error","please enter a valid name")







class ChatWindow:
    def __init__(self, root, user_id, messaging_system,ID1):
        self.root = root
        self.mainID=ID1
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()


        self.user_id = user_id
        self.messaging_system = messaging_system

        self.chat_window = tk.Toplevel(root)
        self.chat_window.title(f"Chat with User {user_id}")
        self.chat_window.geometry("400x500")
        self.chat_window.configure(bg="#E8E8E8")

        self.chat_display = scrolledtext.ScrolledText(self.chat_window, state='disabled', font=("Helvetica", 12))
        self.chat_display.pack(pady=10, fill=tk.BOTH, expand=True)



        self.message_entry = tk.Entry(self.chat_window, font=("Helvetica", 12), width=30)
        self.message_entry.pack(pady=10, padx=10, fill=tk.X)

        self.send_button = tk.Button(self.chat_window, text="Send", command=self.send_message, bg="#4CAF50", fg="white",
                                     font=("Helvetica", 12))
        self.send_button.pack(pady=10)

        self.load_chat()

    def load_chat(self):
        file = open('user.json', 'r')
        all = json.load(file)
        file.close()
        user_messages = self.messaging_system.show_messages_sorted(self.mainID)
        self.chat_display.configure(state='normal')
        if self.user_id in user_messages:
            for msg in user_messages[self.user_id]:
                if msg["type"] == "s":
                    sender = "You"
                else:
                    sender = all[self.user_id]["name"]
                self.chat_display.insert(tk.END, f"{sender}: {msg['message']} ({msg['date']})\n\n")
        self.chat_display.configure(state='disabled')

    def send_message(self):

        message = self.message_entry.get()
        if message.strip():
            self.messaging_system.send_message(self.mainID, self.user_id, message)
            self.chat_display.configure(state='normal')
            self.chat_display.insert(tk.END, f"You: {message} ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n\n")
            self.chat_display.configure(state='disabled')
            self.message_entry.delete(0, tk.END)
            self.chat_display.yview(tk.END)



#app = UserList(1)

