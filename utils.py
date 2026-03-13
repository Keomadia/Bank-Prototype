import time
import random
import json
from tkinter import messagebox
import os

MAXDEPOSIT = 10000001
MINDEPOSIT = 99
MAXWITHDRAW = 500001
MINWITHDRAW = 500
MAXBALCURRENT = 200000000
MAXBALSAVINGS = 20000000


THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR  = os.path.dirname(THIS_FILE_PATH)
FP = os.path.join(BASE_DIR,"database\\database.json")
ENTIRE_PROJECT_DIR  = os.path.dirname(BASE_DIR)

class SignUp:
    def __init__(self,type,fname,lname,email,password,gender,phone,dob) -> None:
        self.__fname = fname
        self.__lname = lname
        self.__fullname = self.__fname + " " +self.__lname
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__dob = dob
        self.__account_num ="3" + str(random.randrange(111111111,999999999))
        self.__account_bal = 0.00
        self.__active = False
        self.__has_pin = False
        self.__pin = 0
        self.__transaction_count = {'withdraw':0, 'transfer':0,'deposit':0}
        self.__acc_type = type
        self.__gender = gender
        self.__date_created = time.ctime(time.time())[slice(0,-13)]

    def check_email(self):
        with open(FP,'r') as file:
            data_a = json.load(file)
            user_fnd =False
            for dct in data_a:
                if dct["email"] == self.__email:
                    user_fnd = True
            return user_fnd
        
    def add_user(self):
        with open(FP,'r') as db:
            data_c = json.load(db)
            new_user = {
                "fname": self.__fname,
                "lname": self.__lname,
                "fullname": self.__fullname,
                "email": self.__email,
                "account_number": self.__account_num,
                "phone":self.__phone,
                "dob":self.__dob,
                "account_balance": self.__account_bal,
                "active" : self.__active,
                "acc_type" : self.__acc_type,
                "password": self.__password,
                "has_pin": self.__has_pin ,
                "pin": self.__pin,
                "date_created":self.__date_created,
                "gender":self.__gender,
                "transaction_count": self.__transaction_count
                }
            if not self.check_email():
                data_c.append(new_user)
                with open(file=FP,mode='w') as update:
                    json.dump(data_c,update,indent=4)
                return f"Successfully created account for {self.__fullname}"
            else: 
                return f" Email already exists (Try and Login instead)"       
      
class Login:
    def __init__(self,email,password) -> None:
        with open(FP,'r') as file:
            data_a = json.load(file)
        for dct in data_a:
            if dct['email'] == email:
                if dct["password"] == password:
                    self.__fname = dct['fname']
                    self.__lname = dct['lname']
                    self.__fullname = dct['fullname']
                    self.__email = dct['email']
                    self.__password = dct['password']
                    self.__account_num = dct['account_number']
                    self.__account_bal = dct['account_balance']
                    self.__active = dct['active']
                    self.__haspin = dct['has_pin']
                    self.__phone = dct['phone']
                    self.__dob = dct['dob']
                    self.__pin = dct['pin']
                    self.__date_created = dct["date_created"]
                    self.__gender = dct["gender"]
                    self.__transaction_count = dct['transaction_count']
                    self.__acc_type = dct['acc_type']
                                 
    def get_user(self):
        if self.__acc_type == "Current" or self.__acc_type == "Savings":
            if self.__acc_type  == "Current":
                user = Current(self.__acc_type,self.__fname,self.__lname,self.__email,self.__password,self.__account_num,self.__account_bal,self.__active,self.__haspin,self.__pin,self.__transaction_count,self.__fullname , self.__gender,self.__date_created,self.__phone,self.__dob)
            elif self.__acc_type  == "Savings":
                user = Savings(self.__acc_type,self.__fname,self.__lname,self.__email,self.__password,self.__account_num,self.__account_bal,self.__active,self.__haspin,self.__pin,self.__transaction_count,self.__fullname , self.__gender,self.__date_created,self.__phone,self.__dob)
            return user      

class Current():
    def __init__(self,type,fname,lname,email,password,account_num,account_bal,active,haspin,pin,transaction_count,fullname,gender,date,phone,dob) -> None:
        self.__type = type
        self.__fname = fname
        self.__lname = lname
        self.__fullname = fullname
        self.__email = email
        self.__password = password
        self.__account_num = account_num
        self.__account_bal = account_bal
        self.__phone = phone
        self.__dob = dob
        self.__active = active
        self.__has_pin = haspin
        self.__pin = pin
        self.__date_created = date
        self.__gender = gender
        self.__transaction_count = transaction_count
        self.__acc_type = type
        
    def check_email(self):
        with open(FP,'r') as file:
            data_a = json.load(file)
            userFnd =False
            for dct in data_a:
                if dct["email"] == self.__email:
                    userFnd = True
            return userFnd
        
    def greet(self):
        if self.__gender  == "Male":
            return f"Welcome back Mr {self.__fullname}"
        elif self.__gender  == "Female":
            return f"Welcome back Ms {self.__fullname}"
        else:
            return f"Welcome back {self.__fullname}"

    def get_email(self):
        return self.__email
        
    def get_acc_num(self):
        return self.__account_num
  
    def get_acc_bal(self):
        with open(FP,'r') as file:
            data_d = json.load(file)
            for dct in data_d:
                if dct['email'] == self.__email:
                    self.__account_bal = dct["account_balance"]        
        return f"₦{self.__account_bal:,}"
  
    def get_acc_type(self):       
        return self.__acc_type
         
    def get_acc_name(self):
        return self.__fullname

    def get_first_name(self):
        return self.__fname
    
    def check_password(self,password):
        with open(FP,'r') as file:
            data_d = json.load(file)
            pass_match =False
            for dct in data_d:
                if dct["password"] == password:
                    pass_match = True
            return pass_match

    def logout(self):
        with open(FP,'r') as file:
            data_h = json.load(file)
            for dct in data_h:
                if dct['email'] == self.__email:
                    dct["active"] = False
        with open(FP,'w') as nw_file:
            json.dump(data_h,nw_file,indent=4)
            return f"{self.__fname}, you have logged out Successfullly"

    def del_account(self):
        with open(FP,'r') as file:
            data_h = json.load(file)
            for dct in data_h:
                if dct['email'] == self.__email:
                    data_h.remove(dct)
        with open(FP,'w') as nw_file:
            json.dump(data_h,nw_file,indent=4)
            return f"{self.__fname}, you have deleted your account Successfullly"
           
    def log_in(self):
        with open(FP,'r') as file:
            data_h = json.load(file)
            for dct in data_h:
                if dct['email'] == self.__email:
                    dct["active"] = True
        with open(FP,'w') as nw_file:
            json.dump(data_h,nw_file,indent=4)
            return "Login Successful"
    
    def deposit(self,amount,pin ,email=None):
        has_deposited = False
        if email == None:
            if MINDEPOSIT < amount < MAXDEPOSIT:
                with open(FP,'r') as file:
                    data_g = json.load(file)
                    for dct in data_g:
                        if dct['email'] == self.__email:
                            if dct['pin'] == int(pin):
                                if dct['account_balance'] < MAXBALCURRENT:
                                    if (dct['account_balance'] + amount) > MAXBALCURRENT:
                                        messagebox.showinfo("Sorry 🙁🙁",f"You can't exceed your balance limit  ₦{MAXBALCURRENT:,}")
                                    else:
                                        dct['account_balance'] += amount
                                        for transaction_type in dct["transaction_count"]:
                                            if transaction_type == "deposit":
                                                dct["transaction_count"][transaction_type] += 1
                                                messagebox.showinfo("Success 🎉🎉",f"Successfully deposited ₦{amount:,}") 
                                                with open(FP,'w') as nw_file:
                                                    json.dump(data_g,nw_file,indent=4)
                                                    has_deposited = True
                                else:
                                    messagebox.showinfo("Sorry 🙁🙁",f"You have exceeded your balance limit  ₦{dct['account_balance']:,}")
                                    has_deposited = False
                            else:
                                messagebox.showinfo("Error","Your Pin is not Correct")
                                has_deposited = False

            else:
                messagebox.showinfo("Error",f"Amount must be within ₦{MINDEPOSIT:,} - ₦{MAXDEPOSIT:,}")
            return has_deposited
            
        else:
            return has_deposited          
        
    def set_withdraw_pin(self,pin):
        pin_set =False
        if pin.isdigit():
            if len(pin) == 4:
                pin = int(pin)
                with open(FP,'r') as file:
                    data_e = json.load(file)
                    for dct in data_e:
                        if dct['email'] == self.__email:
                            if dct['has_pin'] == False:
                                dct["pin"] = pin
                                pin_set = "Successful"
                                dct["has_pin"] = True
                            else:
                                pin_set = "Already have a pin so you'll have to change instead"
                with open(FP,'w') as nw_file:
                    json.dump(data_e,nw_file,indent=4)
            else:
                pin_set = "Pin must be 4 digits"
        else:
            pin_set = "Pin must be numerical"
        return pin_set

    def pin_exists(self):
        with open(FP,'r') as file:
            data_i = json.load(file)
            for dct in data_i:
                if dct['email'] == self.__email:
                    if dct['has_pin'] == True:
                        return True
                    else:
                        return False

    def change_pin(self,pin):
        with open(FP,'r') as file:
            data_i = json.load(file)
            for dct in data_i:
                if dct['email'] == self.__email:
                    if dct['has_pin'] == True:
                        pin_changed =False
                        if pin.isdigit():
                            if len(pin) == 4:
                                pin = int(pin)
                                dct["pin"] = pin
                                dct["has_pin"] = True
                                with open(FP,'w') as nw_file:
                                    json.dump(data_i,nw_file,indent=4)
                                    pin_changed = "Successful"
                                    return pin_changed
                            else:
                                pin_changed = "Pin must be 4 digits"
                                return pin_changed
                        else:
                            pin_changed = "Pin must be numerical"
                            return pin_changed
                    else:
                        return "You do not have a pin to be changed"
                        
    def get_deposit_count(self):
        with open(FP,'r' )as file:
            data_g = json.load(file)
        for dct in data_g:
            if dct['email'] == self.__email:
                for transaction_type in dct["transaction_count"]:
                    if transaction_type == "deposit":
                        return dct["transaction_count"][transaction_type]
                    
    def get_transfer_count(self):
        with open(FP,'r' )as file:
            data_g = json.load(file)
        for dct in data_g:
            if dct['email'] == self.__email:
                for transaction_type in dct["transaction_count"]:
                    if transaction_type == "transfer":
                        return dct["transaction_count"][transaction_type]

    def get_beneficiary(self,account_num):
        with open(FP, 'r') as file:
            data_w = json.load(file)
        for dct in data_w:
            if dct["account_number"] == account_num:
                return dct["email"],dct["fullname"]
        else:
            return "NOT FOUND"
    
       
    def transfer(self,amount,pin,acc_num):
        with open(FP, 'r') as file:
            data_t = json.load(file)
            has_transferred = False
            if amount != '':
                if amount.isdigit():
                    amount =  float(amount)   
                    email_of_ben,_ = self.get_beneficiary(acc_num)
                    if email_of_ben != "NOT FOUND" or email_of_ben != self.__email:
                        for dct_main in data_t:
                            if dct_main["email"] == self.__email:
                                pin = int(pin)
                                if dct_main["pin"] == pin:
                                    if MINWITHDRAW < amount < MAXWITHDRAW:
                                        if dct_main["account_balance"] > amount:
                                            dct_main["account_balance"] -= amount
                                            has_withdrawn = True
                                            if has_withdrawn:
                                                for dct in data_t:
                                                    if dct['email'] == email_of_ben:
                                                        if dct['email'] == email_of_ben:
                                                            if dct['acc_type'] == "Current":
                                                                if dct['account_balance'] < MAXBALCURRENT:
                                                                    if (dct['account_balance'] + amount) > MAXBALCURRENT:
                                                                        messagebox.showinfo("Sorry 🙁🙁",f"You can't transfer more than their limit  ₦{MAXBALCURRENT:,}")
                                                                    else:
                                                                        dct['account_balance'] += amount
                                                                        for transaction_type in dct_main["transaction_count"]:
                                                                            if transaction_type == "transfer":
                                                                                dct_main["transaction_count"][transaction_type] += 1
                                                                                messagebox.showinfo("Success 🎉🎉",f"Successfully Transferred ₦{amount:,}") 
                                                                                with open(FP,'w') as nw_file:
                                                                                    json.dump(data_t,nw_file,indent=4)
                                                                                    has_transferred = True
                                                                else:
                                                                    has_transferred = f"You have exceeded their balance limit"
                                                            elif dct['acc_type'] == "Savings":
                                                                if dct['account_balance'] < MAXBALSAVINGS:
                                                                    if (dct['account_balance'] + amount) > MAXBALSAVINGS:
                                                                        messagebox.showinfo("Sorry 🙁🙁",f"You can't transfer more than their limit  ₦{MAXBALSAVINGS:,}")
                                                                    else:
                                                                        dct['account_balance'] += amount
                                                                        for transaction_type in dct_main["transaction_count"]:
                                                                            if transaction_type == "transfer":
                                                                                dct_main["transaction_count"][transaction_type] += 1
                                                                                messagebox.showinfo("Success 🎉🎉",f"Successfully Transferred ₦{amount:,}") 
                                                                                with open(FP,'w') as nw_file:
                                                                                    json.dump(data_t,nw_file,indent=4)
                                                                                    has_transferred = True
                                                                else:
                                                                    has_transferred = f"You have exceeded their balance limit"
                                                else:
                                                    has_transferred = "Your Pin is not Correct"
                                            else:
                                                has_transferred = "An error occured"
                                    else:
                                        has_transferred = "Exceeding the transfer limit"
                                else:
                                    has_transferred = "Incorrect Pin"
                        else:
                            has_transferred = "An error Occured"
                    else:
                        has_transferred = "Confirm the user first"
                else:
                    has_transferred = "Amount must be in numbers"
            else:
                has_transferred = "Amount can't be empty"
        return has_transferred
                    
class Savings(Current):
    def __init__(self,type,fname,lname,email,password,account_num,account_bal,active,haspin,pin,transaction_count,fullname,gender,date,phone,dob) -> None:
        super().__init__(type,fname,lname,email,password,account_num,account_bal,active,haspin,pin,transaction_count,fullname,gender,date,phone,dob)
        self.__type = type
        self.__fname = fname
        self.__lname = lname
        self.__fullname = fullname
        self.__email = email
        self.__password = password
        self.__account_num = account_num
        self.__phone = phone
        self.__dob = dob
        self.__account_bal = account_bal
        self.__active = active
        self.__has_pin = haspin
        self.__pin = pin
        self.__date_created = date
        self.__gender = gender
        self.__transaction_count = transaction_count
        self.__acc_type = type
        
    def deposit(self,amount,pin):
        has_deposited = False
        if MINDEPOSIT < amount < MAXDEPOSIT:
            with open(FP,'r') as file:
                data_g = json.load(file)
                for dct in data_g:
                    if dct['email'] == self.__email:
                        if dct['pin'] == pin:
                            if dct['account_balance'] < MAXBALSAVINGS:
                                if (dct['account_balance'] + amount) > MAXBALSAVINGS:
                                 messagebox.showinfo("Sorry 🙁🙁",f"You can't exceed your balance limit  ₦{MAXBALSAVINGS:,}")
                                else:
                                    dct['account_balance'] += amount
                                    for transaction_type in dct["transaction_count"]:
                                        if transaction_type == "deposit":
                                            dct["transaction_count"][transaction_type] += 1
                                            messagebox.showinfo("Success 🎉🎉",f"Successfully deposited ₦{amount:,}")
                            else:
                                 messagebox.showinfo("Sorry 🙁🙁",f"You have exceeded your balance limit  ₦{dct['account_balance']:,}")
                        else:
                            messagebox.showinfo("Error","Your Pin is not Correct")
                        with open(FP,'w') as nw_file:
                            json.dump(data_g,nw_file,indent=4)
                            has_deposited = True
        else:
            messagebox.showinfo("Error",f"Amount must be within ₦{MINDEPOSIT:,} - ₦{MAXDEPOSIT:,}")
        return has_deposited
    
