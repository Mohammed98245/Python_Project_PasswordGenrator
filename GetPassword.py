import pickle  #The pickle module implements binary protocols for serializing and de-serializing
import pyperclip  #Pyperclip is a cross-platform Python module for copy and paste clipboard functions
m_password= input("Enter the master password")
if(m_password =="mohammed"):
    account_name = input("enter account name:")
    with open("game.p", "br") as readfile: #opening the file in read mode
        info = pickle.load(readfile)

    if account_name in info:
        pyperclip.copy(info[account_name])  #copying the password
        print("password copied")