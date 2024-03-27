import mysql.connector
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
from io import BytesIO
import random

conn = mysql.connector.connect(host='localhost', user='root', password='@N101l09123', database='mydatabase')
my_cursor = conn.cursor()


bg_color = '#F2F2F2' 
button_color = '#4CAF50'  
highlight_color = '#E6E6FA'  
class LoginOrSignup:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('1200x650')
        self.root.resizable(0, 0)
        self.root.title('Student Teacher Dashboard')
        self.root.configure(bg=bg_color)
        self.login_frame = Frame(self.root, bd=4, borderwidth=4, relief='ridge', bg=highlight_color)
        self.login_frame.pack(fill='both', expand=True)
        label1 = Label(self.login_frame, text="Have an account? Login ", font=('Verdana', 13), bg=bg_color, fg='black',padx=10, pady=10)
        label1.grid(row=0,column=0,columnspan=10,padx=10,pady=10)
        label1.grid_anchor(CENTER)
        stulabel = Label(self.login_frame, text="Student", font=('Arial', 16, 'bold'), padx=10, pady=10, bg=highlight_color, fg='black')
        stulabel.grid(row=1, column=1, columnspan=2, sticky="ew")
        registernum_label = Label(self.login_frame, text="Register Number : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        registernum_label.grid(row=2, column=0)
        self.registernum_entry = Entry(self.login_frame, width=30)
        self.registernum_entry.grid(row=2, column=1)

        password_label = Label(self.login_frame, text="Password : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        password_label.grid(row=3, column=0)
        self.password_entry = Entry(self.login_frame, width=30, show="*")
        self.password_entry.grid(row=3, column=1)

        register_button = Button(self.login_frame, text="Login", font=('Arial', 15), command=self.checkValues, padx=10, pady=10, bd=2, borderwidth=2, bg=button_color, fg='white')
        register_button.grid(row=4, column=0, columnspan=2)

        faclabel = Label(self.login_frame, text="Faculty", font=('Arial', 16, 'bold'), padx=10, pady=10, bg=highlight_color, fg='black')
        faclabel.grid(row=1, column=5, columnspan=2, sticky="ew")
        
        email_label = Label(self.login_frame, text="Email : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        email_label.grid(row=2, column=4)
        self.email_entry = Entry(self.login_frame, width=30)
        self.email_entry.grid(row=2, column=5)

        password_label = Label(self.login_frame, text="Password : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        password_label.grid(row=3, column=4)
        self.password_entry_fac = Entry(self.login_frame, width=30, show="*")
        self.password_entry_fac.grid(row=3, column=5)

        login_button = Button(self.login_frame, text="Login", font=('Arial', 15), command=self.checkfacValues, padx=10, pady=10, bd=2, borderwidth=2, bg=button_color, fg='white')
        login_button.grid(row=4, column=4, columnspan=2)
        label2 = Label(self.login_frame, text="Don't you have an account?", font=('Verdana', 13), bg=bg_color, fg='black')
        label2.grid(row=5, column=0,columnspan=10 ,padx=10,pady=10)
        label2.grid_anchor(CENTER)
        register_button = Button(self.login_frame, text="Register", command=self.show_register, width=10, height=2, bg=button_color, fg='white', font=('Helvetica', 15, 'bold'))
        register_button.grid(row=6,column=0,columnspan=10, padx=10, pady=10)
        register_button.grid_anchor(CENTER)
        self.root.mainloop()

    def checkValues(self):
        regnumber = self.registernum_entry.get().strip()
        password = self.password_entry.get().strip()

        if not regnumber or not password:
            messagebox.showwarning("Incomplete Information", "Please enter both registration number and password.")
            return

        try:
            query = "SELECT * FROM userdata WHERE regno=%s"
            values = (regnumber,)
            my_cursor.execute(query, values)
            data = my_cursor.fetchall()
            print(data)
            if data:
                if password == data[0][2]:
                    messagebox.showinfo("Login successful", "Welcome Back!")
                    self.root.destroy()
                    Home('student', data)
                else:
                    messagebox.showwarning("Password incorrect", "Incorrect Password")
            else:
                messagebox.showerror("Unregistered user", "Registration number not found")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error accessing database: {e}")

    def checkfacValues(self):
        email = self.email_entry.get().strip()
        password = self.password_entry_fac.get().strip()

        if not email or not password:
            messagebox.showwarning("Incomplete Information", "Please enter both email and password.")
            return

        try:
            query = "SELECT * FROM teacher_data WHERE email=%s"
            values = (email,)
            my_cursor.execute(query, values)
            fdata = my_cursor.fetchall()

            if fdata:
                if password == fdata[0][2]:
                    messagebox.showinfo("Login successful", "Welcome Back!")
                    self.root.destroy()
                    Home('faculty', fdata)
                else:
                    messagebox.showwarning("Password incorrect", "Incorrect Password")
            else:
                messagebox.showerror("Unregistered user", "Email not found")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error accessing database: {e}")

    def show_register(self):
        self.root.destroy()
        Register()


class Register:
    def __init__(self) -> None:
        self.register = Tk()
        self.register.geometry('1200x650')
        self.register.resizable(0, 0)
        self.register.title('Student Teacher Dashboard Register')
        self.register.configure(bg=bg_color)

        register_frame = LabelFrame(self.register, bd=4, borderwidth=4, relief="ridge", bg=highlight_color)
        register_frame.pack(fill="both", expand=True)

        mylabel = Label(register_frame, text="Register Here", font=('Arial', 16, 'bold'), padx=10, pady=10, bg=highlight_color, fg='black')
        mylabel.grid(row=0, column=5, columnspan=2, sticky="ew")
        student_label = Label(register_frame, text="Student", font=('Arial', 16, 'bold'), padx=10, pady=10, bg=highlight_color, fg='black')
        student_label.grid(row=1, column=0, columnspan=2, sticky="ew")
        susername_label = Label(register_frame, text="Username : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        susername_label.grid(row=2, column=0)
        susername_entry = Entry(register_frame, width=30)
        susername_entry.grid(row=2, column=1)

        sregisternum_label = Label(register_frame, text="Register Number : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        sregisternum_label.grid(row=3, column=0)
        sregisternum_entry = Entry(register_frame, width=30)
        sregisternum_entry.grid(row=3, column=1)

        spassword_label = Label(register_frame, text="Password : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        spassword_label.grid(row=4, column=0)
        spassword_entry = Entry(register_frame, width=30,show='*')
        spassword_entry.grid(row=4, column=1)

        sregister_button = Button(register_frame, text="Register", font=('Arial', 15), command=lambda: self.checkStuValues(susername_entry.get(), sregisternum_entry.get(), spassword_entry.get()), padx=10, pady=10, bd=2, borderwidth=2, bg=button_color, fg='white')
        sregister_button.grid(row=5, column=0, columnspan=2)
        faculty_label = Label(register_frame, text="Faculty", font=('Arial', 16, 'bold'), padx=10, pady=10, bg=highlight_color, fg='black')
        faculty_label.grid(row=1, column=6, columnspan=2, sticky="ew")
        fusername_label = Label(register_frame, text="Username : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        fusername_label.grid(row=2, column=6)
        fusername_entry = Entry(register_frame, width=30)
        fusername_entry.grid(row=2, column=7)
        femail_label = Label(register_frame, text="Email : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        femail_label.grid(row=4, column=6)
        femail_entry = Entry(register_frame, width=30)
        femail_entry.grid(row=4, column=7)
        fpassword_label = Label(register_frame, text="Password : ", padx=10, pady=10, font=('Arial', 15), bg=highlight_color, fg='black')
        fpassword_label.grid(row=3, column=6)
        fpassword_entry = Entry(register_frame, width=30, show='*')
        fpassword_entry.grid(row=3, column=7)
        

        fregister_button = Button(register_frame, text="Register", font=('Arial', 15), command=lambda: self.checkFacValues(fusername_entry.get(), fpassword_entry.get(), femail_entry.get()), padx=10, pady=10, bd=2, borderwidth=2, bg=button_color, fg='white')
        fregister_button.grid(row=5, column=6, columnspan=2)

        self.register.mainloop()
    def checkFacValues(self, fname, password, email):
        try:
            my_cursor.execute("SELECT * FROM teacher_data WHERE email = %s", (email,))
            existing_teacher = my_cursor.fetchone()
            if existing_teacher:
                messagebox.showinfo("Warning!!", "You are already registered")
                self.register.destroy()
                LoginOrSignup()
            else:
                query = "INSERT INTO teacher_data (faculty_name, f_pass, email) VALUES (%s, %s, %s)"
                my_cursor.execute(query, (fname, password, email))
                conn.commit()
                messagebox.showinfo("Registration successful", "Welcome to Student-Teacher Dashboard")
                self.register.destroy()
                my_cursor.execute('SELECT * FROM teacher_data where email=%s',(email,))
                data=my_cursor.fetchall()
                Home('faculty',data) 
        except mysql.connector.Error as err:
            print("Error:", err)
            messagebox.showwarning("Warning", "Registration failed. Please try again.")

    def checkStuValues(self, username, regno, password):
        my_cursor.execute("SELECT * FROM userdata")
        data = my_cursor.fetchall()
        values = (username, regno, password)
        if values in data:
            messagebox.showinfo("Warning!!", "You are already registered")
            self.register.destroy()
            LoginOrSignup()
        else:
            try:
                query = "INSERT INTO userdata VALUES(%s,%s,%s)"
                my_cursor.execute(query, values)
                conn.commit()
                messagebox.showinfo("Registration successful", "Welcome to Student-Teacher Dashboard")
                self.register.destroy()
                Home('student',[[username, regno, password]])

            except:
                messagebox.showwarning("Warning", "Incorrect information")

class Home:
    def __init__(self, stuORfac, data) -> None:
        self.home = Tk()
        self.home.geometry('1200x650')
        self.home.resizable(0, 0)
        self.home.title('Student-Teacher Dashboard')
        self.home.configure(bg=bg_color)

        home_frame = LabelFrame(self.home, bd=4, borderwidth=4, relief="ridge", bg=bg_color)
        home_frame.pack(fill="both", expand=True)
        top_frame = Frame(home_frame, bg=bg_color)
        top_frame.pack(side=TOP, fill='x')
        Home_button = Button(top_frame, text="Home", padx=10, pady=10, bg=button_color, relief='raised', bd=1, borderwidth=1, border=5, fg='white', font=('Helvetica', 12))
        Home_button.pack(side=LEFT, padx=80, pady=5)
        profile_button = Button(top_frame, text="Profile", padx=10, pady=10, bg=button_color, command=lambda: self.callProfile(stuORfac,data), relief='raised', bd=1, borderwidth=1, border=5, fg='white', font=('Helvetica', 12))
        profile_button.pack(side=LEFT, padx=70, pady=5)

        group_button = Button(top_frame, text="Groups", command=lambda :self.callGroups(stuORfac,data[0][0], data),padx=10, pady=10, bg=button_color, relief='raised', bd=1, borderwidth=1, border=5, fg='white', font=('Helvetica', 12))
        group_button.pack(side=LEFT, padx=60, pady=5)

        chat_button = Button(top_frame, text="Chat Here!",command=lambda:self.chathere(stuORfac,data), padx=10, pady=10, bg=button_color, relief='raised', bd=1, borderwidth=1, border=5, fg='white', font=('Helvetica', 12))
        chat_button.pack(side=LEFT, padx=60, pady=5)
        search_button=Button(top_frame,text='LogOut',command=self.logout, padx=10, pady=10, bg=button_color, relief='raised', bd=1, borderwidth=1, border=5, fg='white', font=('Helvetica', 12))
        search_button.pack(side=LEFT, padx=60, pady=5)
        canvas = Canvas(home_frame, bg=bg_color, width=1000, height=500)
        canvas.pack(side=LEFT, fill="both", expand=True, padx=10, pady=10)

        scrollbar = Scrollbar(home_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=LEFT, fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = Frame(canvas)
        frame.pack(fill='both', expand=True)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        try:
         
            student_query = "SELECT imagedata.regno, imagedata.img, imagedata.descript, userdata.uname FROM imagedata INNER JOIN userdata ON imagedata.regno = userdata.regno"
            my_cursor.execute(student_query)
            student_images = my_cursor.fetchall()

            teacher_query = "SELECT imagedata.faculty_id, imagedata.img, imagedata.descript, teacher_data.faculty_name FROM imagedata INNER JOIN teacher_data ON imagedata.faculty_id = teacher_data.faculty_id"
            my_cursor.execute(teacher_query)
            teacher_images = my_cursor.fetchall()
            
            images = student_images + teacher_images
            random.shuffle(images)
            for regno, image_data, description, username in images:
                def show_user_details(regno=regno):
                    
                    my_cursor.execute('select * from teacher_data where faculty_id=%s',(regno,))
                    f_data=my_cursor.fetchall()
                    if f_data:
                            messagebox.showwarning('Accessing faculty details', 'You can not access the faculty details')
                    else:
                        self.showUserDetails(regno)
                
                my_frame=Frame(frame,padx=10,pady=10)
                my_frame.pack(side=TOP)
                img = Image.open(BytesIO(image_data))
                img.thumbnail((1000, 500))

                img_tk = ImageTk.PhotoImage(img)
                img_label = Label(frame, image=img_tk, bg=bg_color)
                img_label.image = img_tk
                img_label.pack(side=TOP,anchor=CENTER)
                username_button = Button(my_frame, text=username, bg=button_color,command=show_user_details,fg='white', font=('Helvetica', 12))
                username_button.pack(side=LEFT,padx=20, pady=5)
                description_label = Label(my_frame, text=description,font=('Arial',12), bg=bg_color)
                description_label.pack( side=LEFT,padx=10, pady=5)
        except Exception as e:
            print("Error during image processing:", e) 
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        self.home.mainloop()

    def callGroups(self, stuORfac,username, data):
        self.home.destroy()
        GroupManagement(stuORfac,username, data)
    def chathere(self,usertype,data):
        self.home.destroy()
        ChatHere(usertype,data)
    def callProfile(self, stuORfac,data):
        self.home.destroy()
        Profile(stuORfac,data)
    def logout(self):
        self.home.destroy()
        LoginOrSignup()
    def showUserDetails(self, regno):


        user_details_window = Toplevel(self.home)
        user_details_window.title("User Details")
        user_details_window.geometry('1150x650')
        user_details_frame = Frame(user_details_window)
        user_details_frame.pack(fill='both', expand=True)

        query_user = "SELECT * FROM userdata WHERE regno = %s"
        my_cursor.execute(query_user, (regno,))
        user_details = my_cursor.fetchone()

        username_label = Label(user_details_frame, text="Username:", font=('Arial', 12))
        username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        username_value = Label(user_details_frame, text=user_details[0], font=('Arial', 12))
        username_value.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        regno_label = Label(user_details_frame, text="Register Number:", font=('Arial', 12))
        regno_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        regno_value = Label(user_details_frame, text=user_details[1], font=('Arial', 12))
        regno_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        user_posts_frame = Frame(user_details_window)
        user_posts_frame.pack(fill='both', expand=True)

        canvas = Canvas(user_posts_frame, bg=highlight_color)
        canvas.pack(side=LEFT, fill='both', expand=True)

        scrollbar = Scrollbar(user_posts_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)

        posts_frame = Frame(canvas, bg=highlight_color)
        canvas.create_window((0, 0), window=posts_frame, anchor="nw")

        query_posts = "SELECT img, descript FROM imagedata WHERE regno = %s"
        my_cursor.execute(query_posts, (regno,))
        user_posts = my_cursor.fetchall()

        for i, (image_data, description) in enumerate(user_posts):
            img = Image.open(BytesIO(image_data))
            img.thumbnail((200, 200))
            img_tk = ImageTk.PhotoImage(img)
            img_label = Label(posts_frame, image=img_tk, text=description,font=('Arial',12), compound="top")
            img_label.image = img_tk
            img_label.grid(row=i, column=0, padx=10, pady=10)

        posts_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        back_button = Button(user_details_window, text="Back", command=user_details_window.destroy)
        back_button.pack(pady=10)
class ChatHere:
    def __init__(self,usertype,data_values) -> None:
        query = "SELECT * FROM userdata"
        my_cursor.execute(query)
        user_data = my_cursor.fetchall()
        user_name=data_values[0][0]
        self.chat_window = Tk()
        self.chat_window.geometry('1250x650')
        self.chat_window.resizable(0, 0)
        self.chat_window.title('Student-Teacher Dashboard Chat')
        self.chat_window.configure(bg=bg_color)
        
        chat_frame = Frame(self.chat_window)
        chat_frame.pack(fill='both', expand=True)
        
        canvas = Canvas(chat_frame, bg=highlight_color)
        canvas.pack(side='left', fill='both', expand=True)

        scrollbar = Scrollbar(chat_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.configure(yscrollcommand=scrollbar.set)

        chat_canvas_frame = Frame(canvas, bg=highlight_color)
        canvas.create_window((0, 0), window=chat_canvas_frame, anchor="nw")
        
        label = Label(chat_canvas_frame, text="Chat Here and Enhance your connections", padx=10, pady=10, font=('Arial', 20))
        label.grid(row=0, column=5)

        for i, data in enumerate(user_data):
            
            username_label = Label(chat_canvas_frame, text=data[0], padx=10, pady=10, font=('Arial', 15), bd=10)
            username_label.grid(row=i+1, column=0, columnspan=2, padx=10, pady=10)
            
            button = Button(chat_canvas_frame, text='Chat', bg=button_color,command=lambda : self.chat(user_name,data[0]), padx=10, pady=10, relief='raised', bd=1, borderwidth=1, border=5, fg='white', font=('Helvetica', 12))
            button.grid(row=i+1, column=3, columnspan=2, padx=10, pady=10)
           
        back_button=Button(chat_canvas_frame, text="< Back" , command=lambda:self.back(usertype,data_values), padx=10, pady=10,font=('vardana', 12), bd=2, borderwidth=2, bg=button_color)
        back_button.grid(row=0, column=9, columnspan=3)

        self.chat_window.mainloop()
    def back(self,usertype,data):
        self.chat_window.destroy()
        Home(usertype,data)
    def chat(self, currentuser,username):
        chat_window = Tk()
        self.uname=username
        chat_window.geometry('400x400')
        chat_window.title(f'Chat with {self.uname}')
        
        self.conversation_display = Text(chat_window, bg='white',width=400,height=3, font=('Arial', 12), wrap='word')
        self.conversation_display.pack(side=TOP,fill='both', expand=True)
        
        message_entry = Text(chat_window, bg='lightgray', font=('Arial', 12), wrap='word', width=400, height=5)
        message_entry.pack(side=TOP,fill='x', padx=5, pady=5)
        
        send_button = Button(chat_window, text='Send', bg='blue', fg='white', command=lambda: self.send_message(currentuser,chat_window, message_entry, self.conversation_display))
        send_button.pack(side=TOP,pady=5, fill='x', padx=5)
        
        chat_window.mainloop()
    
    def send_message(self,cuser, chat_window, message_entry, conversation_display):
        message = message_entry.get('1.0', END).strip()
        if message:
            sender_username = cuser 
            receiver_username = self.uname
            try:
                query = "INSERT INTO chat_messages (sender_username, receiver_username, message) VALUES (%s, %s, %s)"
                values = (sender_username, receiver_username, message)
                my_cursor.execute(query, values)
                conn.commit()
                query = "INSERT INTO chat_messages (sender_username, receiver_username, message) VALUES (%s, %s, %s)"
                values = (receiver_username, sender_username, message)
                my_cursor.execute(query, values)
                conn.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to send message: {str(e)}")
                return
            
            conversation_display.config(state='normal')
            conversation_display.insert(END, f"You: {message}\n")
            conversation_display.config(state='disabled')
            message_entry.delete('1.0', END)
class Groups:
    def __init__(self):
        pass
    
    def create_group(self, group_name, creator_username):

        try:
            query = "INSERT INTO groups_data (group_name, creator_username, members) VALUES (%s, %s, %s)"
            values = (group_name, creator_username, creator_username)  
            my_cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Group Created", "Group created successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create group: {str(e)}")
    
    def add_member(self, group_id, member_username):

        try:
            query = "SELECT members FROM groups_data WHERE group_id = %s"
            my_cursor.execute(query, (group_id,))
            result = my_cursor.fetchone()
            if result:
                members = result[0] + "," + member_username
                update_query = "UPDATE groups_data SET members = %s WHERE group_id = %s"
                my_cursor.execute(update_query, (members, group_id))
                conn.commit()
                messagebox.showinfo("Member Added", "Member added successfully.")
            else:
                messagebox.showerror("Error", "Group not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add member: {str(e)}")
    
    def get_user_groups(self, username):
        try:
            query = "SELECT * FROM groups_data WHERE creator_username = %s OR members LIKE %s"
            my_cursor.execute(query, (username, f"%{username}%"))
            return my_cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve user groups: {str(e)}")

class GroupManagement:
    def __init__(self, usertype,username,data):
        self.root = Tk()
        self.root.geometry('1200x650')
        self.root.resizable(0, 0)
        self.root.title('Student-Teacher Dashboard Group Management')
        self.root.configure(bg=bg_color)
        
        self.username = username

        create_group_frame = Frame(self.root, bg=highlight_color)
        create_group_frame.pack(fill='both', expand=True, pady=10)

        Label(create_group_frame, text="Create New Group", font=('Arial', 14), bg=highlight_color).grid(row=0, column=0, columnspan=2, pady=5)
        back_button=Button(create_group_frame, text="< Back" , command=lambda:self.back(usertype,data),padx=10, pady=10,font=('vardana', 10), bd=2, borderwidth=2, bg=button_color)
        back_button.grid(row=0, column=5, padx=10, pady=10)
        Label(create_group_frame, text="Group Name:", bg=highlight_color).grid(row=1, column=0, pady=5)
        self.group_name_entry = Entry(create_group_frame)
        self.group_name_entry.grid(row=1, column=1, pady=5)

        Button(create_group_frame, text="Create Group", command=self.create_group, bg=button_color, fg='white').grid(row=2, column=0, columnspan=2, pady=10)

        add_member_frame = Frame(self.root, bg=highlight_color)
        add_member_frame.pack(fill='both', expand=True, pady=10)

        Label(add_member_frame, text="Add Member to Group", font=('Arial', 14), bg=highlight_color).grid(row=0, column=0, columnspan=2, pady=5)

        Label(add_member_frame, text="Group ID:", bg=highlight_color).grid(row=1, column=0, pady=5)
        self.group_id_entry = Entry(add_member_frame)
        self.group_id_entry.grid(row=1, column=1, pady=5)

        Label(add_member_frame, text="Member Username:", bg=highlight_color).grid(row=2, column=0, pady=5)
        self.member_username_entry = Entry(add_member_frame)
        self.member_username_entry.grid(row=2, column=1, pady=5)
        
        Button(add_member_frame, text="Add Member", command=self.add_member, bg=button_color, fg='white').grid(row=3, column=0, columnspan=2, pady=10)
        self.display_groups_frame = Frame(self.root, bg=highlight_color)
        self.display_groups_frame.pack(fill='both', expand=True, pady=10)

        self.display_user_groups()
    def back(self,usertype,data):
        self.root.destroy()
        Home(usertype,data)
    def create_group(self):
        group_name = self.group_name_entry.get()

        if group_name:
            groups_manager = Groups()
            groups_manager.create_group(group_name, self.username)
            self.display_user_groups()
        else:
            messagebox.showerror("Error", "Please enter group name.")

    def add_member(self):
        group_id = self.group_id_entry.get()
        member_username = self.member_username_entry.get()

        if group_id and member_username:
            groups_manager = Groups()
            groups_manager.add_member(group_id, member_username)
        else:
            messagebox.showerror("Error", "Please enter group ID and member username.")

    def display_user_groups(self):
        for widget in self.display_groups_frame.winfo_children():
            widget.destroy()

        groups_manager = Groups()
        user_groups = groups_manager.get_user_groups(self.username)

        if user_groups:
            Label(self.display_groups_frame, text="Your Groups:", font=('Arial', 14), bg=highlight_color).pack(pady=5)

            for group in user_groups:
                if self.username == group[2] or self.username in group[3].split(','):
                    group_info = f"Group ID: {group[0]}, Group Name: {group[1]}, Creator: {group[2]}, Members: {group[3]}"
                    Label(self.display_groups_frame, text=group_info, bg=highlight_color).pack(pady=2)
        else:
            Label(self.display_groups_frame, text="You have no groups yet.", font=('Arial', 12), bg=highlight_color).pack(pady=5)

class Profile:
    def __init__(self, stuORfac,data) -> None:

        self.profile = Tk()
        self.profile.geometry('1250x650')
        self.profile.resizable(0,0)
        self.profile.title('Student-Teacher Dashboard Profile')
        if stuORfac=='student':
            self.profile_frame = LabelFrame(self.profile, bd=4, borderwidth=4, relief="ridge", bg=highlight_color)
            self.profile_frame.pack(fill="both", expand=True)
            username = data[0][0]
            regnum = data[0][1]
            profile_label = Label(self.profile_frame, text="Profile", font=('Arial', 15), padx=10, pady=10,bg=highlight_color)
            profile_label.place(x=150,y=50)
            username_label = Label(self.profile_frame, text="Username : ", font=('Arial', 12), padx=10, pady=10, bd=2,
                               borderwidth=2,bg=highlight_color)
            username_label.place(x=50, y=150)
            username_data = Label(self.profile_frame, text=username, padx=10, pady=10, font=('Arial', 12),bg=highlight_color)
            username_data.place(x=200, y=150)
            regnum_label = Label(self.profile_frame, text="Register Number : ", font=('Arial', 12), padx=10, pady=10, bd=2,
                             borderwidth=2,bg=highlight_color)
            regnum_label.place(x=50,y=200)
            regnum_data = Label(self.profile_frame, text=regnum, padx=10, pady=10, font=('Arial', 12),bg=highlight_color)
            regnum_data.place(x=200,y=200)
            post_pic = Button(self.profile_frame, text="Post Your certificate", command=lambda:self.SelectPic(self.profile,data,'student'), padx=10, pady=10,
                           font=('vardana', 12), bd=2, borderwidth=2, bg=button_color)
            post_pic.place(x=150,y=300)
            self.show_post=Button(self.profile_frame,text="Show Posts", font=('vardana', 12), command=lambda:self.show(regnum,data,'student'), bd=2, borderwidth=2, bg=button_color,padx=10,pady=10)
            self.show_post.place(x=500, y=300)
            self.pic_label = Label(self.profile_frame,bg=highlight_color)
            self.pic_label.place(x=200, y=400)
            back_button=Button(self.profile_frame, text="< Back" , command=lambda:self.back('student',data), padx=10, pady=10,font=('vardana', 12), bd=2, borderwidth=2, bg=button_color)
            back_button.place(x=1150,y=50)
            self.profile.mainloop()
        else:
            self.profile_frame = LabelFrame(self.profile, bd=4, borderwidth=4, relief="ridge", bg=highlight_color)
            self.profile_frame.pack(fill="both", expand=True)
            print(data)
            username = data[0][0]
            email = data[0][3]
            profile_label = Label(self.profile_frame, text="Profile", font=('Arial', 15), padx=10, pady=10,bg=highlight_color)
            profile_label.place(x=150,y=50)
            username_label = Label(self.profile_frame, text="Username : ", font=('Arial', 12), padx=10, pady=10, bd=2,
                               borderwidth=2,bg=highlight_color)
            username_label.place(x=50, y=150)
            username_data = Label(self.profile_frame, text=username, padx=10, pady=10, font=('Arial', 12),bg=highlight_color)
            username_data.place(x=200, y=150)
            email_label = Label(self.profile_frame, text="Email : ", font=('Arial', 12), padx=10, pady=10, bd=2,
                             borderwidth=2,bg=highlight_color)
            email_label.place(x=50,y=200)
            email_data = Label(self.profile_frame, text=email, padx=10, pady=10, font=('Arial', 12),bg=highlight_color)
            email_data.place(x=200,y=200)
            post_pic = Button(self.profile_frame, text="Post Your certificate", command=lambda:self.SelectPic(self.profile,data,'faculty'), padx=10, pady=10,
                           font=('vardana', 12), bd=2, borderwidth=2, bg=button_color)
            post_pic.place(x=150,y=300)
            self.show_post=Button(self.profile_frame,text="Show Posts", font=('vardana', 12), command=lambda:self.show(email,data,'faculty'), bd=2, borderwidth=2, bg=button_color,padx=10,pady=10)
            self.show_post.place(x=500, y=300)
            self.pic_label = Label(self.profile_frame,bg=highlight_color)
            self.pic_label.place(x=200, y=400)
            back_button=Button(self.profile_frame, text="< Back" , command=lambda:self.back('student',data), padx=10, pady=10,font=('vardana', 12), bd=2, borderwidth=2, bg=button_color)
            back_button.place(x=1150,y=50)
            self.profile.mainloop()
            
    def back(self,stuORfac,data):
            self.profile.destroy()
            Home(stuORfac,data)
    def show(self,val,data,stuORfac):
            self.profile.destroy()
            ShowPosts(val,data,stuORfac)
    def SelectPic(self, profile, data, stuORfac):
        global img
        filename = filedialog.askopenfilename(initialdir='/images', title='Select Image',
                                          filetypes=(('jpg images', '*.jpg'), ('png images', '*.png')))
        if filename: 
            try:
                img = Image.open(filename)
                img.thumbnail((200, 100))
                img = img.convert("RGB")
                img = ImageTk.PhotoImage(img)
                self.pic_label['image'] = img
                self.pic_label.image = img 

                self.description = Entry(self.profile_frame, width=50)
                self.description.place(x=150, y=525)

                self.add_image = Button(self.profile_frame, text="Post", command=lambda: self.post(profile, filename, self.description.get(), data, stuORfac), padx=10, pady=10)
                self.add_image.place(x=250, y=550)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open image: {str(e)}")
        else:
            messagebox.showerror("Error", "No file selected.")

    def post(self,profile,path,description,data,stuORfac):
            if stuORfac=='student':
                postPic(path,profile,description,data[0][1],data,stuORfac)
            else:
                print("Data:", data)
                my_cursor.execute("select * from teacher_data where email=%s",(data[0][3],))
                f_id=my_cursor.fetchall()
                id=f_id[0][1]
                postPic(path,profile,description,id,data,stuORfac)
class postPic:
        
    def __init__(self,path, profile,description,num,data,stuORfac) -> None:
        with open(path, 'rb') as file:
            BinaryData=file.read()
        if stuORfac=='student':

            query="INSERT INTO imagedata(img, regno, descript) VALUES(%s,%s,%s)"
            values=(BinaryData ,num,description)
            my_cursor.execute(query,values)
            conn.commit()
            messagebox.showinfo("Successful post", "Posted successfully")
        else:
            query="INSERT INTO imagedata(img, faculty_id, descript) VALUES(%s,%s,%s)"
            values=(BinaryData ,num,description)
            my_cursor.execute(query,values)
            conn.commit()
            messagebox.showinfo("Successful post", "Posted successfully")
        file.close()
        profile.destroy()
        Profile(stuORfac,data)
class ShowPosts:
    def __init__(self, val, data, stuORfac) -> None:
        self.show_posts = Tk()
        self.show_posts.geometry('1250x650')
        self.show_posts.resizable(0, 0)
        self.show_posts.title('Student-Teacher Dashboard Posts')
        
        show_frame = LabelFrame(self.show_posts, bd=4, borderwidth=4, bg=highlight_color, relief="ridge")
        show_frame.pack(fill="both", expand=True)

        back_button = Button(show_frame, text="< Back", command=lambda: self.back(stuORfac, data), padx=10, pady=10, font=('vardana', 14), bd=2, borderwidth=2, bg=button_color)
        back_button.grid(row=0, column=0)
        canvas = Canvas(show_frame, bg=highlight_color, width=1100, height=500)
        canvas.grid(row=1, column=0, padx=10, pady=10)

        scrollbar = Scrollbar(show_frame, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = Frame(canvas, bg=highlight_color)
        frame.grid(row=0, column=0, sticky="nsew")

        canvas.create_window((0, 0), window=frame, anchor="nw")

        images = None  

        if stuORfac == 'student':
            query = "SELECT img, descript FROM imagedata WHERE regno=%s"
            my_cursor.execute(query, (val,))
            images = my_cursor.fetchall()
        else:
            print('val',val)
            my_cursor.execute("SELECT * FROM teacher_data WHERE email=%s", (val,))
            f_data = my_cursor.fetchall()

            print('f_data', f_data)
            f_id = f_data[0][1]
            query = "SELECT img, descript FROM imagedata WHERE faculty_id=%s"
            my_cursor.execute(query, (f_id,))
            images = my_cursor.fetchall()

        if images:
            for image_data, description in images:
                img = Image.open(BytesIO(image_data))
                img.thumbnail((1000, 500))
                img_tk = ImageTk.PhotoImage(img)
                label = Label(frame, image=img_tk, text=description, font=('Arial', 12), compound="top")
                label.image = img_tk
                label.pack(anchor=CENTER, padx=10, pady=10)
        else:
            Label(frame, text="No posts available", font=('Arial', 12), bg=highlight_color).pack(padx=10, pady=10)

        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        self.show_posts.mainloop()

    def back(self, stuORfac, data):
        self.show_posts.destroy()
        Profile(stuORfac, data)

obj = LoginOrSignup()
