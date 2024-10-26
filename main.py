import customtkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import utils as log
import time

class BankApp():
    def __init__(self,root):
        FONT = ("Arial", 12, "bold")
        PURPLE = '#E1B5EF'
        BLACK = 'black'
        self.root = root
        self.root.title("Bank Account App")
        self.root.geometry("1300x650+20+10")  # Increased height for clock
        self.root.configure(fg_color="#fff")
        self.root.resizable(0,0)
        self.current_user = None
        
        self.clock_frame = tk.CTkFrame(root, fg_color=PURPLE)
        self.clock_frame.pack(side='bottom', fill='x')
        
                # Create and display the clock
        self.clock_label = tk.CTkLabel(self.clock_frame, font=FONT, fg_color="transparent", text_color=BLACK)
        self.clock_label.pack(pady=10)
        self.update_clock()
        
        
        # Main Frame for content
        self.main_frame = tk.CTkFrame(root, fg_color=PURPLE,width=900,height=900)
        self.main_frame.pack(pady=(50,10), padx = 30)
        
        # Show the login form initially
        self.show_login_form()
        
    def update_clock(self):
        now = datetime.now()
        time_str = now.strftime('%Y-%m-%d %H:%M:%S')
        self.clock_label.configure(text=time_str)
        self.root.after(1000, self.update_clock)  # Update the clock every second

    def withdraw_page(self):
        return messagebox.showinfo("Sorry 🙁🙁","This feature is not yet available")

    def transfer_page(self):
        
        FONT = ("Arial", 21, "bold")
        FONT2 = ("Consolas", 18, "italic")
        MAIN_PURPLE = '#E1B5EF'
        PURPLE = 'purple'
        VIOLET = 'violet'
        BLACK = 'black'
        WHITE = '#faeff2'
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()
        # Initialize the main window
        
        self.root.title("Transfer Money")
    

        
        def confirm_user():
            num = self.trf_acc_number_entry.get()
            if usr.get_beneficiary(num) != "NOT FOUND":
                _,fullname = usr.get_beneficiary(num)
                self.trf_confirm_user_entry.configure(text=fullname)
                self.trf_transfer_button.configure(state='normal')
                return True
            else:
                messagebox.showinfo("Error","User not Found")
                return False
        
        # Configure the main grid layout with 3 rows and 2 columns
        self.main_frame.grid_columnconfigure((0, 1), weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)

        self.trf_header_frame = tk.CTkFrame(self.main_frame,fg_color='transparent')
        self.trf_header_frame.grid(row=0, column=0,columnspan=2,sticky='nsew')
        # Header at the top
        tk.CTkButton(self.trf_header_frame, text="←", font=("Arial", 24, "bold"), text_color="black",width=2,fg_color='transparent',hover_color=MAIN_PURPLE,command=self.home_page).grid(row=0,column=0,padx=0)
        self.trf_header_label = tk.CTkLabel(self.trf_header_frame, text=usr.get_first_name().upper()+ " READY TO TRANSFER 💸-=💸? ", font=("Arial", 24, "bold"), text_color="black")
        self.trf_header_label.grid(row=1, column=0, columnspan=2, padx=200, pady=10, sticky="nsew")

        # Frame for entry section on the left side
        self.trf_entry_frame = tk.CTkFrame(self.main_frame, corner_radius=10,fg_color='transparent')
        self.trf_entry_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Account Number Entry
        self.trf_acc_number_label = tk.CTkLabel(self.trf_entry_frame, text="Account Number:", font=("Arial", 14),fg_color="transparent",text_color=BLACK)
        self.trf_acc_number_label.grid(row=0,column=0,padx=10, pady=(10, 5))
        self.trf_acc_number_entry = tk.CTkEntry(self.trf_entry_frame, width=250,fg_color=WHITE,text_color=BLACK)
        self.trf_acc_number_entry.grid(row=0,column =1,padx=10, pady=5)

        # Amount Entry
        self.trf_amount_label = tk.CTkLabel(self.trf_entry_frame, text="Amount:", font=("Arial", 14),fg_color="transparent",text_color=BLACK)
        self.trf_amount_label.grid(row=1,column=0,padx=10, pady=(10, 5))
        self.trf_amount_entry = tk.CTkEntry(self.trf_entry_frame, width=250,fg_color=WHITE,text_color=BLACK)
        self.trf_amount_entry.grid(row=1,column =1,padx=10, pady=5)

        # PIN Entry
        self.trf_pin_label = tk.CTkLabel(self.trf_entry_frame, text="PIN:", font=("Arial", 14),fg_color="transparent",text_color=BLACK)
        self.trf_pin_label.grid(row=2,column =0,padx=10, pady=(10, 5))
        self.trf_pin_entry = tk.CTkEntry(self.trf_entry_frame, width=250, show="*",fg_color=WHITE,text_color=BLACK)
        self.trf_pin_entry.grid(row=2,column =1,padx=10, pady=5)

        # Confirm User Entry
        self.trf_confirm_user_button = tk.CTkButton(self.trf_entry_frame, text="Confirm User", font=("Arial", 14),fg_color=PURPLE,hover_color=VIOLET,command=confirm_user)
        self.trf_confirm_user_button.grid(row=3,column =0,padx=10, pady=(10, 5))
        self.trf_confirm_user_entry = tk.CTkLabel(self.trf_entry_frame, width=250,text="",fg_color='transparent',text_color=BLACK,font=FONT)
        self.trf_confirm_user_entry.grid(row=3,column =1,padx=10, pady=5)

        # Transfer Button
        self.trf_transfer_button = tk.CTkButton(self.trf_entry_frame, text="Transfer", width=200, height=40, corner_radius=8,fg_color=PURPLE,hover_color=VIOLET,command=self.transfr,state='disabled')
        self.trf_transfer_button.grid(row=4,column =0,padx=10, pady=(20, 10),columnspan=2)

        # Frame for keypad on the right side
        self.trf_keypad_frame = tk.CTkFrame(self.main_frame, corner_radius=10,fg_color='transparent')
        self.trf_keypad_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        self.trf_keypad_buttons = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('Clear', 3, 0), ('0', 3, 1), ('Enter', 3, 2)
        ]

        for (text, row, col) in self.trf_keypad_buttons:
            button = tk.CTkButton(self.trf_keypad_frame, text=text, width=80, height=60, corner_radius=8,fg_color=PURPLE,hover_color=VIOLET,state='disabled')
            button.grid(row=row, column=col, padx=5, pady=5)

        # Footer at the bottom
        trffooter_label = tk.CTkLabel(self.main_frame, text="TDD Bank © 2024", font=("Arial", 12), text_color="gray")
        trffooter_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="sew")
 
    def depo(self):
        global balance
        
        if self.depo_amount_entry.get().isdigit():
            if self.depo_pin_entry.get() != "":
                if self.depo_pin_entry.get().isdigit():
                    deposit = usr.deposit(float(self.depo_amount_entry.get()),int(self.depo_pin_entry.get()))
                    if deposit == True:
                        balance = usr.get_acc_bal()
                        self.acc_bal.configure(text=balance) 
                        self.home_page()
                    # transaction_history_deposit_lbl.configure(text=usr.get_deposit_count())
            else:
                messagebox.showinfo("Error","Enter your pin")
        else:
            messagebox.showinfo("Error","Enter a Valid Amount")
        
    def transfr(self):
        account_number = self.trf_acc_number_entry.get()
        send_amount = self.trf_amount_entry.get()
        user_pin = self.trf_pin_entry.get()

        transferred = usr.transfer(send_amount,user_pin,account_number)
        if transferred:
            self.home_page()
        else:
            messagebox.showinfo("Error",transferred)
    
    def deposit_page(self):
        FONT = ("Arial", 24, "bold")
        FONT2 = ("Consolas", 12)
        MAIN_PURPLE = '#E1B5EF'
        PURPLE = 'purple'
        VIOLET = 'violet'
        BLACK = 'black'
        WHITE = '#faeff2'
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()
        # Initialize the main window
        
        self.root.title("Transfer Money")
    

        # Configure the main grid layout with 3 rows and 2 columns
        self.main_frame.grid_columnconfigure((0, 1), weight=1)
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)

        self.depo__frame = tk.CTkFrame(self.main_frame,fg_color='transparent')
        self.depo__frame.grid(row=0, column=0,columnspan=2,sticky='nsew')
        # Header at the top
        tk.CTkButton(self.depo__frame, text="←", font=FONT, text_color="black",width=2,fg_color='transparent',hover_color=MAIN_PURPLE,command=self.home_page).grid(row=0,column=0,padx=0)
        self.depo_header_label = tk.CTkLabel(self.depo__frame, text=usr.get_first_name().upper() + " READY TO DEPOSIT 💸+=💸 ?", font=FONT, text_color="black")
        self.depo_header_label.grid(row=1, column=0, columnspan=2, padx=200, pady=10, sticky="nsew")

        # Frame for entry section on the left side
        self.depo_entry_frame = tk.CTkFrame(self.main_frame, corner_radius=10,fg_color='transparent')
        self.depo_entry_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Account Number Entry
        self.depo_amount_label = tk.CTkLabel(self.depo_entry_frame, text="Amount", font=("Arial", 14),fg_color="transparent",text_color=BLACK)
        self.depo_amount_label.grid(row=0,column=0,padx=10, pady=(10, 5))
        self.depo_amount_entry = tk.CTkEntry(self.depo_entry_frame, width=250,fg_color=WHITE,text_color=BLACK,font=FONT2)
        self.depo_amount_entry.grid(row=0,column =1,padx=10, pady=5)

        # PIN Entry
        self.depo_pin_label = tk.CTkLabel(self.depo_entry_frame, text="PIN:", font=("Arial", 14),fg_color="transparent",text_color=BLACK)
        self.depo_pin_label.grid(row=1,column =0,padx=10, pady=(10, 5))
        self.depo_pin_entry = tk.CTkEntry(self.depo_entry_frame, width=250, show="*",fg_color=WHITE,text_color=BLACK,font=FONT2)
        self.depo_pin_entry.grid(row=1,column =1,padx=10, pady=5)


        # Deposit Button
        self.deposit_button = tk.CTkButton(self.depo_entry_frame, text="Deposit", width=200, height=40, corner_radius=8,fg_color=PURPLE,hover_color=VIOLET,command=self.depo)
        self.deposit_button.grid(row=3,column =0,padx=10, pady=(20, 10),columnspan=2)

        # Frame for keypad on the right side
        self.depo_keypad_frame = tk.CTkFrame(self.main_frame, corner_radius=10,fg_color='transparent')
        self.depo_keypad_frame.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")

        # Keypad Layout (3x4 grid of buttons, including numbers 1-9, 0, Clear, and Enter)
        self.depo_keypad_buttons = [
            ('1', 0, 0), ('2', 0, 1), ('3', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('Clear', 3, 0), ('0', 3, 1), ('Enter', 3, 2)
        ]

        for (text, row, col) in self.depo_keypad_buttons:
            button = tk.CTkButton(self.depo_keypad_frame, text=text, width=80, height=60, corner_radius=8,fg_color=PURPLE,hover_color=VIOLET,state='disabled')
            button.grid(row=row, column=col, padx=5, pady=5)

        # Footer at the bottom
        self.depo_footer_label = tk.CTkLabel(self.main_frame, text="TDD Bank © 2024", font=("Arial", 12), text_color="gray")
        self.depo_footer_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="sew")

    def settings_page(self):
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()

        self.root.title("Settings")
        MAIN_PURPLE = '#E1B5EF'
        PURPLE = 'purple'
        VIOLET = 'violet'
        BLACK = 'black'
        WHITE = '#faeff2'
        
        self.main_frame.configure(corner_radius=20)
        
        # Configure the main grid layout
        
        self.main_frame.grid_columnconfigure(0, weight=1)  # Single column
        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)  # Six rows

        self.settings_header_frame = tk.CTkFrame(self.main_frame,fg_color='transparent')
        self.settings_header_frame.grid(row=0, column=0,columnspan=2,sticky='nsew')
        # Header at the top
        tk.CTkButton(self.settings_header_frame, text="←", font=("Arial", 24, "bold"), text_color="black",width=2,fg_color='transparent',hover_color=MAIN_PURPLE,command=self.home_page).grid(row=0,column=0,padx=0)

        # Header at the top
        settings_header_label = tk.CTkLabel(self.settings_header_frame, text="SETTINGS", font=("Arial", 24, "bold"), text_color=WHITE,fg_color=PURPLE,corner_radius=20,height=100,width=380,)
        settings_header_label.grid(row=1, column=1, padx=20, pady=20, sticky="nsew",columnspan=2)

        # Define placeholder functions for each action
        def close_account():
            if messagebox.askyesno("Warning","Are you sure you want to DELETE this account"):
                messagebox.showinfo("Bye Bye 👋🙋‍♂️👋",usr.del_account())
                self.show_login_form()
            else:
                pass    
            
        def set_pin():          
            pin = set_pin_entry.get()
            play = usr.set_withdraw_pin(pin)
            if play != "Successful":
                messagebox.showinfo("Error",play)
            elif play != "Already have a pin so you'll have to change instead":
                messagebox.showinfo("Error",play)
                set_pin_window.destroy()
            else:
                messagebox.showinfo("Info","You have successfully set a pin ")
                set_pin_window.destroy()
                set_pin_button.configure(state='disabled')
 
        def change_pin():
            pin = change_pin_entry.get()
            play = usr.change_pin(pin)
            if play != "Successful":
                messagebox.showinfo("Error",play)
            else:
                messagebox.showinfo("Success","You have successfully Changed your pin ") 
                change_pin_window.destroy()
               
        def close_set():
            set_pin_window.destroy()

        def close_change():
            change_pin_window.destroy()
            
        def set_pin_frame():
            global set_pin_entry
            global set_pin_window
            
            set_pin_window = tk.CTk()
            set_pin_window.attributes('-topmost', True)
            set_pin_window.overrideredirect(True)
            set_pin_window.geometry("180x100+800+300")  
            set_pin_window.configure(fg_color="#fff")
            set_pin_window.resizable(0,0)
            
            set_pin_lbl = tk.CTkLabel(master=set_pin_window,text_color=BLACK,font=('consolas',10),width=50,text="SET PIN",fg_color=MAIN_PURPLE,corner_radius=10,height=20)
            set_pin_entry = tk.CTkEntry(master=set_pin_window,font=('consolas',10),placeholder_text="Set your new pin",width=100,height=20,fg_color=MAIN_PURPLE,text_color=BLACK)
            set_pin_btn = tk.CTkButton(master=set_pin_window,text="Confirm",text_color=WHITE,font=("consolas",13),cursor='hand2',fg_color=PURPLE,width=75,corner_radius=10,hover_color=PURPLE,command=set_pin,height=20)
            cancel_btn = tk.CTkButton(master=set_pin_window,text="Cancel",text_color=BLACK,font=("consolas",13),cursor='hand2',fg_color=MAIN_PURPLE,width=75,corner_radius=10,hover_color=PURPLE,command=close_set,height=20)
            set_pin_lbl.grid(row=0,column=0,padx=5,pady=(10,0))
            set_pin_entry.grid(row=0,column=1,padx=5,pady=(10,0))
            cancel_btn.grid(row=1,column=0,padx=5,pady=(20,10))
            set_pin_btn.grid(row=1,column=1,padx=5,pady=(20,10))
            set_pin_window.mainloop()
            
        def change_pin_frame():
            global change_pin_entry
            global change_pin_window
            
            change_pin_window = tk.CTk()
            change_pin_window.attributes('-topmost', True)
            change_pin_window.overrideredirect(True)
            change_pin_window.geometry("180x100+800+300")  
            change_pin_window.configure(fg_color="#fff")
            change_pin_window.resizable(0,0)
            
            change_pin_lbl = tk.CTkLabel(master=change_pin_window,text_color=BLACK,font=('consolas',10),width=50,text="change PIN",fg_color=MAIN_PURPLE,corner_radius=10,height=20)
            change_pin_entry = tk.CTkEntry(master=change_pin_window,font=('consolas',10),placeholder_text="Change your existing pin",width=100,height=20,fg_color=MAIN_PURPLE,text_color=BLACK)
            change_pin_btn = tk.CTkButton(master=change_pin_window,text="Confirm",text_color=WHITE,font=("consolas",13),cursor='hand2',fg_color=PURPLE,width=75,corner_radius=10,hover_color=PURPLE,command=change_pin,height=20)
            cancel_btn = tk.CTkButton(master=change_pin_window,text="Cancel",text_color=BLACK,font=("consolas",13),cursor='hand2',fg_color=MAIN_PURPLE,width=75,corner_radius=10,hover_color=PURPLE,command=close_change,height=20)
            change_pin_lbl.grid(row=0,column=0,padx=5,pady=(10,0))
            change_pin_entry.grid(row=0,column=1,padx=5,pady=(10,0))
            cancel_btn.grid(row=1,column=0,padx=5,pady=(20,10))
            change_pin_btn.grid(row=1,column=1,padx=5,pady=(20,10))
            change_pin_window.mainloop()

        def color_settings():
            messagebox.showinfo("Sorry 💔💔!","This feature is not available yet")


        # Adding buttons to the grid
        close_button = tk.CTkButton(self.main_frame, text="Close Account", width=400, height=40, corner_radius=8, command=close_account ,fg_color=VIOLET,text_color=BLACK,hover_color=PURPLE)
        close_button.grid(row=1, column=0, padx=40, pady=10, sticky="nsew")
        logout_button = tk.CTkButton(self.main_frame, text="Logout", width=400, height=40, corner_radius=8, command=self.log_out ,fg_color=VIOLET,text_color=BLACK,hover_color=PURPLE)
        logout_button.grid(row=2, column=0, padx=40, pady=10, sticky="nsew")
        set_pin_button = tk.CTkButton(self.main_frame, text="Set PIN", width=400, height=40, corner_radius=8, command=set_pin_frame ,fg_color=VIOLET,text_color=BLACK,hover_color=PURPLE)
        set_pin_button.grid(row=3, column=0, padx=40, pady=10, sticky="nsew")
        change_pin_button = tk.CTkButton(self.main_frame, text="Change PIN", width=400, height=40, corner_radius=8, command=change_pin_frame ,fg_color=VIOLET,text_color=BLACK,hover_color=PURPLE)
        change_pin_button.grid(row=4, column=0, padx=40, pady=10, sticky="nsew")
        color_set_button = tk.CTkButton(self.main_frame, text="Color Settings", width=400, height=40, corner_radius=8, command=color_settings ,fg_color=VIOLET,text_color=BLACK,hover_color=PURPLE)
        color_set_button.grid(row=5, column=0, padx=40, pady=(10,40), sticky="nsew")

                

        # Run the main event loop
    
    def verify(self,fname,lname,email,password,confirm_password,agree,phone,dob):
        agree = self.agree.get()

        dob = self.dob_entry.get_date()
        today = datetime.now().strftime('%Y-%m-%d')
        
        dob_calc = str(dob)[0:4]
        today_calc = str(today)[0:4]
        
        age = int(today_calc) - int(dob_calc)
        if fname != "":
            if lname != "":
                if phone != '':
                    if phone[slice(0,4)] == '+234':
                        if len(phone) == 14:
                            if 18 <= age <= 100:
                                if 21 > len(password) > 7:
                                    if password == confirm_password:
                                        if agree == True:
                                            email_type = ["@gmail.com","@yahoo.com"]
                                            for tipe in email_type:
                                                if (email[slice(-10,len(email))] == tipe and len(email) > 11) or (email[slice(-11,len(email))] == "@outlook.com" and len(email) > 11):
                                                    return True
                                            else:
                                                messagebox.showinfo(title="Vital Info",message="Invalid email")
                                        else:
                                            messagebox.showinfo(title="Vital Info",message="You must Agree to The Terms First")
                                    else:
                                        messagebox.showinfo(title="Vital Info",message="Passwords must match")  
                                else:
                                    messagebox.showinfo(title="Vital Info",message="Passwords must within the range 8-20")
                            else:
                                messagebox.showinfo(title="Vital Info",message=f"Age is {age}. Not in valid age range")
                        else:
                            messagebox.showinfo(title="Vital Info",message="Invalid Phone Number!")
                    else:
                        messagebox.showinfo(title="Vital Info",message="Phone Number must have (+234)")
                else:
                    messagebox.showinfo(title="Vital Info",message="Phone Number must have numbers")
            else:
                messagebox.showinfo(title="Vital Info",message="Last name cannot be empty")
        else:
            messagebox.showinfo(title="Vital Info",message="First name cannot be empty")
            return False
  
    def get_acc_type(self):
        selection = self.acc_type_var.get()

        if selection == "Savings":
            return "Savings"
        elif selection == "Current":
            return "Current"  
        
    def get_gender(self):
        gender = self.gender_var.get()

        if gender == "Male":
            return "Male"
        elif gender == "Female":
            return "Female"  
        else:
            return gender

    def sign_up(self):
        type = self.get_acc_type()
        gende = self.get_gender()
        fnam = self.first_name_entry.get()
        lnam = self.last_name_entry.get()
        emai = self.email_entry.get()
        numb = self.mobile_no_entry.get()
        dob = self.dob_entry.get_date()
        dob = str(dob)
        passwor = self.password_entry.get()
        conf_passwor = self.confirm_password_entry.get()
        agree = self.agree.get()
        if self.verify(fname=fnam,lname=lnam,email=emai,password=passwor,confirm_password=conf_passwor,agree=agree,phone=numb,dob=dob):
            user = log.SignUp(type=type,fname=fnam,lname=lnam,email=emai,password=passwor,gender=gende,phone=numb,dob=dob)
            messagebox.showinfo(title="Vital Info",message= user.add_user())
            time.sleep(1)
            self.show_login_form()    

# did not use 
    def verify_login(self,email,password):
    #     if len(password) > 7:
    #         if email[slice(-10,len(email))] == "@gmail.com" or email[slice(-10,len(email))] == "@yahoo.com" or email[slice(-11,len(email))] == "@outlook.com":
    #             return email,password
    #         else:
    #             return messagebox.showerror("Error","Invaid email")
    #     else:
    #         return messagebox.showerror("Error","Invalid Password")
        pass

    def login(self):
        try:
            password_login = self.login_password_entry.get()
            email_login = self.login_email_entry.get()
            if email_login[slice(-10,len(email_login))] == "@gmail.com" or email_login[slice(-10,len(email_login))] == "@yahoo.com" or email_login[slice(-11,len(email_login))] == "@outlook.com":
                if len(password_login) > 7:
                    user = log.Login(email_login,password_login)
                    global usr
                    usr = user.get_user()
                    messagebox.showinfo("Welcome Back 🎊🎉✨",usr.log_in())
                    self.home_page()
                else:
                    messagebox.showerror("Error","Invalid Password")
            else:
                    messagebox.showerror("Error","Invalid email")
        except:
            messagebox.showinfo("Error","Unavailable user")

    def show_login_form(self):
        FONT = ("Arial", 12, "bold")
        PURPLE = '#E1B5EF'
        BLACK = 'black'
        WHITE = 'white'
        
        
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()

        self.root.title("Login") 
        # Login Form
        tk.CTkLabel(self.main_frame, text="Login", font=("Arial", 20, "bold"), fg_color='transparent', text_color=BLACK).grid(row=0, column=0, columnspan=2, pady=10)

        # Email
        tk.CTkLabel(self.main_frame, text="Email:", font=FONT, fg_color='transparent', text_color=BLACK).grid(row=1, column=0, pady=(30,5),padx=7, sticky='e')
        self.login_email_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200,placeholder_text="Jagaban101@gmail.com")
        self.login_email_entry.grid(row=1, column=1, pady=(30,5),padx=20)

        # Password
        tk.CTkLabel(self.main_frame, text="Password:", font=FONT, fg_color='transparent', text_color=BLACK).grid(row=2, column=0, pady=(10,0) , padx=7, sticky='e')
        self.login_password_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200, show="*",placeholder_text="**********")
        self.login_password_entry.grid(row=2, column=1, pady=(10,0),padx=20)


        # # Switch to Sign Up
        # tk.CTkButton(self.main_frame, text="Sign Up", font=FONT, fg_color='darkred', text_color=WHITE, width=40).grid(row=4, column=0, columnspan=2, pady=20)

        sign_up_fram = tk.CTkFrame(self.main_frame,fg_color="transparent")
        sign_up_password_lbl = tk.CTkLabel(master=sign_up_fram,text="Ready to join?",text_color=BLACK,font=FONT,width=50)
        sign_up_password_lbl.grid(row=0,column=0)
        sign_up_btn = tk.CTkButton(master=sign_up_fram,text="SignUp here",text_color="#032eac",font=("consolas",14,'bold'),fg_color="transparent",hover_color=PURPLE,cursor='hand2',command=self.create_form)
        sign_up_btn.grid(row=0,column=1)
        sign_up_fram.grid(row=3,column=0,columnspan=2,pady=(30,5))
        
                # Login Button
        tk.CTkButton(self.main_frame, text="Login",font=FONT, fg_color="purple",text_color=WHITE,hover_color='violet', width=60 , command=self.login).grid(row=4, column=0, columnspan=2, pady=(0,20))

    def create_form(self):

        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()
        
            
        FONT = ("Arial", 12, "bold")
        PURPLE = '#E1B5EF'
        BLACK = 'black'
        WHITE = 'white'           
        
        self.root.title("Sign up") 
        
        # Title
        tk.CTkLabel(self.main_frame, text="Bank Account Sign-Up", font=("Arial", 16, "bold"), fg_color='transparent', text_color=BLACK).grid(row=0, column=0, columnspan=2, pady=10)

        # First Name
        tk.CTkLabel(self.main_frame, text="First Name: ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=1, column=0, pady=(35,0) , padx=(15,2), sticky='e')
        self.first_name_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200,placeholder_text="Jagaban")
        self.first_name_entry.grid(row=1, column=1, pady=(35,0) ,padx=(2,25))

        # Last Name
        tk.CTkLabel(self.main_frame, text="Last Name: ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=2, column=0, pady=(10,0) , padx=(15,2), sticky='e')
        self.last_name_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200,placeholder_text="Thegoat")
        self.last_name_entry.grid(row=2, column=1, pady=(10,0) ,padx=(2,25))

        # Email
        tk.CTkLabel(self.main_frame, text="Email: ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=3, column=0, pady=(10,0) , padx=(15,2), sticky='e')
        self.email_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200,placeholder_text="Jagaban101@gmail.com")
        self.email_entry.grid(row=3, column=1, pady=(10,0) ,padx=(2,25))

        # Mobile No.
        tk.CTkLabel(self.main_frame, text="Mobile no : ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=4, column=0, pady=(10,0) , padx=(15,2), sticky='e')
        self.mobile_no_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200,placeholder_text="+2348084123812")
        self.mobile_no_entry.grid(row=4, column=1, pady=(10,0) ,padx=(2,25))

        # Date of Birth (with DateEntry)
        tk.CTkLabel(self.main_frame, text="Date of Birth:", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=5, column=0, pady=(10,0) ,padx=(2,25), sticky='e')
        self.dob_entry = DateEntry(self.main_frame, font=('consolas',8), width=10, fg_color='darkBLACK', text_color='white',borderwidth=2, date_pattern="d-mm-yyyy", headersbackground=PURPLE, headersforeground="BLACK", weekendbackground="purple", weekendforeground="white", othermonthbackground='violet', othermonthforeground=BLACK)        
        self.dob_entry.grid(row=5, column=1, pady=(10,0) ,padx=(2,25))

        # Gender
        tk.CTkLabel(self.main_frame, text="Gender: ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=6, column=0, pady=(10,0) , padx=(15,2), sticky='e')
        self.gender_var = tk.StringVar(self.main_frame)
        self.gender_var.set("Male")
        self.gender_dropdown = tk.CTkOptionMenu(self.main_frame,variable=self.gender_var, font=("Arial", 12), values=["Male", "Female","Others"], width=200,fg_color=WHITE,dropdown_fg_color=WHITE,dropdown_text_color=BLACK,button_color=PURPLE,button_hover_color=PURPLE,text_color=BLACK)
        self.gender_dropdown.grid(row=6, column=1, pady=(10,0) ,padx=(2,25))

        tk.CTkLabel(self.main_frame, text="Account type: ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=7, column=0, pady=(10,0) , padx=(15,2), sticky='e')
        self.acc_type_var = tk.StringVar(self.main_frame)
        self.acc_type_var.set("Savings")
        self.acc_type_dropdown = tk.CTkOptionMenu(self.main_frame,variable=self.acc_type_var, font=("Arial", 12), values=["Savings", "Current"], width=200,fg_color=WHITE,dropdown_fg_color=WHITE,dropdown_text_color=BLACK,button_color=PURPLE,button_hover_color=PURPLE,text_color=BLACK)
        self.acc_type_dropdown.grid(row=7, column=1, pady=(10,0) ,padx=(2,25))

        # Password
        tk.CTkLabel(self.main_frame, text="Password: ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=9, column=0, pady=(10,0) , padx=(15,2), sticky='e')
        self.password_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200,placeholder_text="***********",show="*")
        self.password_entry.grid(row=9, column=1, pady=(10,0) ,padx=(2,25))

        # Confirm Password
        tk.CTkLabel(self.main_frame, text="Confirm Password: ", font=FONT, fg_color=PURPLE, text_color=BLACK).grid(row=10, column=0, pady=(5,35) , padx=(15,2), sticky='e')
        self.confirm_password_entry = tk.CTkEntry(self.main_frame,font=FONT, fg_color=WHITE, text_color=BLACK, width=200,placeholder_text="***********", show="*")
        self.confirm_password_entry.grid(row=10, column=1, pady=(5,35) ,padx=(2,25))


        self.agree = tk.BooleanVar()
        tc = tk.CTkCheckBox(master=self.main_frame,text="Agree to terms and Conditions",hover_color=BLACK,fg_color=BLACK,text_color=BLACK,variable=self.agree,onvalue=True,offvalue=False)
        tc.grid(row=11,column=0,columnspan=2)
        
        # # Switch to Login
        
        login_frame = tk.CTkFrame(self.main_frame,fg_color="transparent")
        login_password_lbl = tk.CTkLabel(master=login_frame,text="Already a Member?",text_color=BLACK,font=FONT)
        login_password_lbl.grid(row=0,column=0)
        login_btn = tk.CTkButton(master=login_frame,text="Login here",text_color='blue',font=("consolas",14),fg_color="transparent",hover_color=PURPLE,cursor='hand2',command=self.show_login_form)
        login_btn.grid(row=0,column=1)
        login_frame.grid(row=12,column=0,columnspan=2)

        # # Submit Button
        sign_up_btn = tk.CTkButton(master=self.main_frame,text="Sign UP",font=FONT,cursor='hand2',fg_color="purple",text_color=WHITE,hover_color='violet',command=self.sign_up)
        sign_up_btn.grid(row=13,column=0,columnspan=2,pady=(2,10),padx=(10))
     
    def log_out(self):
        if messagebox.askyesno("Warning","Are you sure you want to log out"):
            messagebox.showinfo("Bye Bye 👋🙋‍♂️👋",usr.logout())
            self.show_login_form()
        else:
            pass
    
    def home_page(self):
            
        FONT = ("Arial", 21, "bold")
        FONT2 = ("Consolas", 18, "italic")
        MAIN_PURPLE = '#E1B5EF'
        PURPLE = 'purple'
        VIOLET = 'violet'
        BLACK = 'black'
        WHITE = '#faeff2'
        balance = usr.get_acc_bal()
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()
            
        self.root.title("Bank App Homepage")
        self.root.geometry("1300x700+20+10")
        

        # Configure the grid layout
        self.main_frame.grid_columnconfigure((0, 1), weight=1)
        self.main_frame.grid_rowconfigure((0,1), weight=1)

        greting = tk.CTkFrame(self.main_frame, corner_radius=10,fg_color="transparent")
        greting.grid(row=0, column=0, padx=20, pady=(5,20),sticky="nsew",columnspan=2)

        gret_lbl = tk.CTkLabel(
            greting, text=usr.greet().upper(),justify="left", text_color="#222", font=("Arial", 36,'bold')
        )
        gret_lbl.pack(padx=20, pady=(20,0))

        # Creating a frame for user details on the left side
        self.details_frame = tk.CTkFrame(self.main_frame, corner_radius=10,fg_color="transparent")
        self.details_frame.grid(row=1, column=0, padx=20, pady=(20),sticky="nsew")

        # Adding some dummy user details to the self.details_frame
        tk.CTkLabel(self.details_frame, text="Name",justify="left", text_color=BLACK, font=FONT).grid(row=0,column=0,pady=(20,0))
        self.name = tk.CTkLabel(self.details_frame, text=usr.get_acc_name(),justify="left", text_color=BLACK, font=FONT2)
        self.name.grid(row=0,column=1,padx=20,pady=(20,0))
        
        tk.CTkLabel(self.details_frame, text="Balance",justify="left", text_color=BLACK, font=FONT).grid(row=1,column=0,pady=(20,0))
        self.acc_bal = tk.CTkLabel(self.details_frame, text=balance,justify="left", text_color=BLACK, font=FONT2)
        self.acc_bal.grid(row=1,column=1,padx=20,pady=(20,0))
        
        tk.CTkLabel(self.details_frame, text="Acc Number",justify="left", text_color=BLACK, font=FONT).grid(row=2,column=0,pady=(20,0))
        self.acc_num = tk.CTkLabel(self.details_frame, text=usr.get_acc_num(),justify="left", text_color=BLACK, font=FONT2)
        self.acc_num.grid(row=2,column=1,padx=20,pady=(20,0))
        
        tk.CTkLabel(self.details_frame, text="Account Type",justify="left", text_color=BLACK, font=FONT).grid(row=3,column=0,pady=(20,0))
        self.acc_type = tk.CTkLabel(self.details_frame, text=usr.get_acc_type(),justify="left", text_color=BLACK, font=FONT2)
        self.acc_type.grid(row=3,column=1,padx=20,pady=(20,0))
        
        tk.CTkLabel(self.details_frame, text="Email",justify="left", text_color=BLACK, font=FONT).grid(row=4,column=0,pady=(20,0))
        self.email = tk.CTkLabel(self.details_frame, text=usr.get_email(),justify="left", text_color=BLACK, font=FONT2)
        self.email.grid(row=4,column=1,padx=20,pady=(20,0))

        self.button_fram = tk.CTkFrame(self.main_frame, corner_radius=10,fg_color="transparent")
        # Adding the buttons to the buttons_frame in a 2x2 grid
        self.transfer_btn = tk.CTkButton(self.button_fram, text="Transfer", width=300, height=200, corner_radius=8,font=("Consolas",40,'bold'),fg_color=PURPLE,hover_color=BLACK,text_color=WHITE,command=self.transfer_page)
        self.transfer_btn.grid(row=0, column=0, padx=(3,20), pady=(5,10))  # Positioning in a 2x2 grid
        self.withdraw_btn = tk.CTkButton(self.button_fram, text="Withdraw", width=300, height=200, corner_radius=8,font=("Consolas",40,'bold'),fg_color=VIOLET,hover_color=BLACK,text_color=WHITE,command=self.withdraw_page)
        self.withdraw_btn.grid(row=0, column=1, padx=(3), pady=(5,10))  # Positioning in a 2x2 grid
        self.deposit_btn = tk.CTkButton(self.button_fram, text="Deposit", width=300, height=200, corner_radius=8,font=("Consolas",40,'bold'),fg_color=VIOLET,hover_color=BLACK,text_color=WHITE,command=self.deposit_page)
        self.deposit_btn.grid(row=1, column=0, padx=(3,20), pady=(5))  # Positioning in a 2x2 grid
        self.settings_btn = tk.CTkButton(self.button_fram, text="Settings", width=300, height=200, corner_radius=8,font=("Consolas",40,'bold'),fg_color=PURPLE,hover_color=BLACK,text_color=WHITE,command=self.settings_page)
        self.settings_btn.grid(row=1, column=1, padx=(3), pady=(5))  # Positioning in a 2x2 grid
        self.button_fram.grid(row=1,column=1,padx=(10,30),pady=(15))


if __name__ == "__main__":
    root = tk.CTk()
    app = BankApp(root)
    root.mainloop()

