import json
from datetime import datetime
from tkinter import Canvas,messagebox,PhotoImage
import tkinter as tk
from anotherv import TimeLine

class Notifications:
    def __init__(self):
        self.notifications =[]
        self.load_notifications()

    def load_notifications(self):
        file = open("notifc.json", 'r')
        data = json.load(file)
        file.close()
        self.notifications=data


    def add_notification(self, user_id, notification_type, message,togo):
        self.load_notifications()
        notification = {
            "type": notification_type,
            "message": message,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "toGO":togo
        }

        # ne7ot path el sora
        if notification["type"] =="like" :
            notification["image"]= "C:\\Users\\Abdallah\\Desktop\\pngimg.com - like_PNG11.png"
        elif notification["type"] =="comment" :
            notification["image"] = "C:\\Users\\Abdallah\\Desktop\\pngtree-blue-rounded-comment-button-on-white-background-png-image_4891076.png"
        elif notification["type"] == "message" :
            notification["image"] ="C:\\Users\\Abdallah\\Desktop\\png-transparent-white-and-blue-message-icon-illustration-email-computer-icons-symbol-message-inbox-by-gmail-envelope-miscellaneous-blue-angle-thumbnail.png"
        elif notification["type"] == "freind" :
            notification["image"] ="C:\\Users\\Abdallah\\Desktop\\freindreq.png"





        self.notifications[user_id].append(notification)
        self.save_notifications()

    def show_notifications(self, user_id):
           self.load_notifications()
           if user_id < len(self.notifications):
                 for notification in reversed(self.notifications[user_id]):
                      print(f"{notification['date']} - {notification['type']}: {notification['message']}")
           else:
              print("No notifications found for this user.")

    def save_notifications(self):
        file = open("notifc.json", 'w')
        json.dump(self.notifications, file, indent=4)
        file.close()

    def get_notifications(self,user_id):
        self.load_notifications()
        new= self.notifications[user_id]    # haib3t el list ely fe index el user ely gowaha el messages
        return new

    def remove_notifications(self,id,notifc):
        self.load_notifications()
        self.notifications[id].remove(notifc)
        self.save_notifications()




class notGUI:
    def __init__(self,ID):
        self.user_data = ID
        self.user_id = ID["id"]
        self.root = tk.Toplevel()
        self.root.title("notifications")
        self.root.geometry("800x750")

        self.canvas = Canvas(self.root, bg="#E3F2FD")
        self.canvas.pack(fill=tk.BOTH, expand=True)


        self.background_image_path = r"C:\Users\Abdallah\Downloads\Samsung-Innovation-Campus-1000x576.png"
        self.background_image = PhotoImage(file=self.background_image_path)

        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        self.notifications=Notifications()
        self.images={}







        self.display_users(self.user_id)

    def display_users(self,ID):
        y_offset = 15


        for user in self.notifications.get_notifications(ID):  #ha3mlha be stack

            rectangle = self.canvas.create_rectangle(15, y_offset, 450, y_offset + 80, fill="#ffffff", outline="")


            self.canvas.tag_bind(rectangle, "<Button-1>",
                                 lambda event, idx=user: self.on_rectangle_click(idx, event))

            image_path = user.get("image")
            img = PhotoImage(file=image_path)

            self.images[y_offset] = img


            #self.canvas.create_oval(25, y_offset + 10, 85, y_offset + 70, fill="#2196F3", outline="#BBDEFB")
            self.canvas.create_image(55, y_offset + 40, image=self.images[y_offset])



            self.canvas.create_text(95, y_offset + 20, anchor="w", text=user["type"], font=("Helvetica", 13, "bold"),
                                    fill="#1E88E5")
            self.canvas.create_text(95, y_offset + 45, anchor="w", text=user["message"], font=("Helvetica", 11),
                                    fill="#607D8B")
            self.canvas.create_text(400, y_offset + 20, anchor="e", text=user["date"], font=("Helvetica", 11),
                                    fill="#78909C")


            y_offset += 90
        self.root.mainloop()

    def on_rectangle_click(self, idx, event):   #lessa a5er haga

        if idx["type"] =="comment" or idx["type"] =="like" :
            if messagebox.askyesno("go to post ", f"do u want to open your post ?"):
                self.root.destroy()
                objjj=TimeLine(self.user_data)
                objjj.onePost(idx["toGO"])
                self.notifications.remove_notifications(self.user_id, idx)
                self.root.destroy()


            else:
                return
        elif idx["type"] == "message" :
            file = open('user.json', 'r')
            all = json.load(file)
            file.close()
            if messagebox.askyesno("go to message ", f"do u want to open the chat with {all[idx['toGO']]['name']} ") :

                from todo import ChatWindow, MessagingSystem
                obj2=MessagingSystem()
                chat_window = ChatWindow(self.root, idx["toGO"], obj2, self.user_id)
                self.notifications.remove_notifications(self.user_id, idx)
                #self.root.destroy()


        elif idx["type"]=="freind" :
            file = open('user.json', 'r')
            all = json.load(file)
            file.close()

            if messagebox.askyesno("freind ", f"do u want to accept  {all[idx['toGO']]['name']} freind request? "):
                all[self.user_id]["freinds"].append(idx["toGO"])
                all[idx["toGO"]]["freinds"].append(self.user_id)
                file = open("user.json", 'w')
                json.dump(all, file, indent=4)
                file.close()
                self.notifications.remove_notifications(self.user_id,idx)
                self.root.destroy()

            else :
                return


        else:
           return



        #print(f" {idx} type ")


#notifications = Notifications()




